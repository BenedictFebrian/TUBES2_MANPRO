from flask import Flask, request, g
from flask_cors import CORS
import datetime
import sqlite3
import pickle

pkl_filename = "Model_Naive_Weather_Today.pkl"
with open(pkl_filename, 'rb') as file:
    loaded_model_Naive_Weather = pickle.load(file)

db_filename = 'database.db'

app = Flask(__name__)
CORS(app)


def make_dicts(cursor, row):
    return dict((cursor.description[idx][0], value)
                for idx, value in enumerate(row))


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(db_filename)

    db.row_factory = make_dicts
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    print(query)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


def validate_date(date_text, tipe):
    try:
        if (tipe == 'complete'):
            datetime.datetime.strptime(date_text, '%Y-%m-%d')
            return True
        elif (tipe == 'month'):
            datetime.datetime.strptime(date_text, '%Y-%m')
            return True
    except ValueError:
        return False


@app.route('/', methods=['GET'])
def index():
    date = request.args.get('date')
    city = request.args.get('city')

    if (date is not None and city is not None):
        result = None
        if (validate_date(date, 'complete')):
            result = query_db(
                'SELECT * FROM cuaca WHERE Date = ? AND Location = ?',
                [date, city],
                one=True
            )
        elif (validate_date(date, 'month')):
            result = query_db(
                'SELECT * FROM cuaca WHERE Date LIKE \'' + date + '%\' AND Location = ?',
                [city]
            )
        else:  # week
            try:
                [year, weekNum] = [s for s in date.split('-')]
                year = int(year)
                weekNum = int(weekNum[1:])

                if (weekNum == 1 or weekNum == 53):
                    b = weekNum == 1
                    result1 = query_db(
                        'SELECT *, strftime(\'%W\', cuaca.Date)+1 AS WeekNum, strftime(\'%Y\', cuaca.Date) AS Year FROM cuaca WHERE Year = \'' + str(
                            year if b else year+1) + '\' AND WeekNum = 1 AND Location = ?',
                        [city]
                    )
                    result53 = query_db(
                        'SELECT *, strftime(\'%W\', cuaca.Date)+1 AS WeekNum, strftime(\'%Y\', cuaca.Date) AS Year FROM cuaca WHERE Year = \'' + str(
                            year-1 if b else year) + '\' AND WeekNum = 53 AND Location = ?',
                        [city]
                    )
                    result = result53 + result1
                else:
                    result = query_db(
                        'SELECT *, strftime(\'%W\', cuaca.Date)+1 AS WeekNum, strftime(\'%Y\', cuaca.Date) AS Year FROM cuaca WHERE Year = \'' + str(year) + '\' AND WeekNum = ' +
                        str(weekNum) + ' AND Location = ?',
                        [city]
                    )
            except:
                return "Incorrect data format, should be YYYY-MM-DD or YYYY-MM or YYYY-WXX"

        return {
            'result': result if result else None
        }

    else:
        return {
            'result': None
        }


@app.route('/predict', methods=['GET'])
def predict():
    rainfall = request.args.get('r')
    humid9am = request.args.get('h9am')
    humid3pm = request.args.get('h3pm')

    if (rainfall is None or not rainfall or humid3pm is None or not humid3pm):
        return 'Rainfall and humid3pm required'

    try:
        X_new = [[float(rainfall), float(humid3pm)]]

        # if (not humid9am or humid9am is not None):
        #     X_new = [[float(rainfall), float(humid9am), float(humid3pm)]]
    except:
        return 'Invalid data'

    Y_pred_new = loaded_model_Naive_Weather.predict(X_new)[0]

    return {
        'result': 'raining' if Y_pred_new == 1 else 'not raining'
    }
