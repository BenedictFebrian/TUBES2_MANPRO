import sys
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn import metrics

# Membaca dataset
df = pd.read_csv("weatherAUS.csv")
df.head()

#==== EKSPLORASI DATA =====

#Melihat atribut/kolom yang dimiliki oleh dataset
df.columns

#Melihat jumlah baris dan kolom yang dimiliki oleh dataset | format : (baris, kolom)
df.shape

#Melihat tipe data yang dimiliki setiap atribut/kolom
df.dtypes

#Melihat banyaknya elemen yang ada pada dataset
df.size

#Melihat apakah terdapat missing value pada dataset
df.isnull().values.any()

#Drop row with missing value
df = df.dropna()

#Buat label dari kolom rainToday
dfRainToday_labels = df[['RainToday']]

# Membuat array Numpy utk kelas/label
rainToday_labels_np = np.array(dfRainToday_labels.values) # numpy array

# Mengubah matriks 1 kolom ke 1 baris (spy dpt jadi parameter le.fit_transform(.))
rainToday_label_np = rainToday_labels_np.ravel()

# Creating labelEncoder
le = preprocessing.LabelEncoder()

# Mengubah label string ke numerik
RainToday_labels_toInt = le.fit_transform(rainToday_label_np)

# Membuat features untuk klasifikasi rain today
df_weather1 = df[['Rainfall','Evaporation', 'Sunshine', 'WindGustSpeed', 'WindSpeed9am', 'WindSpeed3pm', 'Humidity9am', 'Humidity3pm', 'Pressure9am', 'Pressure3pm', 'Cloud9am', 'Cloud3pm']]

# Membuat array Numpy utk features 1
array_features_weather1 = np.array(df_weather1.values)

# Membuat label kelas dari kolom pertama
weather_labels1 = df[['RainToday']]  # hasil: 1 kolom 

# Membuat array Numpy utk kelas/label
weather_labels_np1 = np.array(weather_labels1.values) # numpy array 

# Mengubah matriks 1 kolom ke 1 baris (spy dpt jadi parameter le.fit_transform(.))
label_np1 = weather_labels_np1.ravel()

# Mengubah label string ke numerik
weather_labels_en1 = le.fit_transform(label_np1)

# Memeriksa dimensi
array_features_weather1.shape

# Data yang sudah siap saatnya dilakukan feature extraction dengan chi-square (Rain Today)
X1 = array_features_weather1
Y1 = weather_labels_np1

# Feature extraction: mengambil k atribut prediktor paling signifikan 
# Feature extraction: memilih atribut prediktor (yg paling signifikan)
# k nya dapat diganti dari 2 sampai 12
selector1  = SelectKBest(score_func=chi2, k=3)
selector1.fit(X1, Y1)

# Mengambil kolom yg terpilih (dg koefisien chi-square terbaik)
cols1 = selector1.get_support(indices=True)

# Buat fitur dataframe dgn k kolom paling signifikan
df_features1 = df_weather1.iloc[:,cols1]

array_fitur1 = np.array(df_features1.values)

# Split dataset into training set and test set: 70% training and 30% test
X_train1, X_test1, y_train1, y_test1 = train_test_split(array_fitur1, weather_labels_en1, test_size=0.3, random_state=3) 

df_features1.head

# =========================
# Naive Bayes Classifier (NBC)
# Library untuk algoritma klasifikasi Naive Bayes
from sklearn.naive_bayes import GaussianNB

NBC_model_weather = GaussianNB()

# Train the model using the training sets
NBC_model_weather.fit(X_train1, y_train1)

# Predict the response for test dataset
Y_pred1 = NBC_model_weather.predict(X_test1)

weather_classes1 = weather_labels1.RainToday.unique()
#print(wine_classes)

# Menghitung dan tampilkan metriks evaluator model klasifikasi
from sklearn.metrics import classification_report
print(classification_report(y_test1, Y_pred1, target_names = weather_classes1))

# Model Accuracy, how often is the classifier correct?
print("Akurasi model klasifikasi Weather dgn NBC:",metrics.accuracy_score(y_test1, Y_pred1))

# =========================
# Klasifikasi kelas wine dgn algoritmat kNN
from sklearn.neighbors import KNeighborsClassifier

# Membuat model dgn jumlah neighbor
# n_neighbors bisa diganti dari 5
kNN_model_weather1 = KNeighborsClassifier(n_neighbors=5)

# Train the model using the training sets
kNN_model_weather1.fit(X_train1, y_train1)

# Predict the response for test dataset
y_pred1 = kNN_model_weather1.predict(X_test1)

weather_classes1 = weather_labels1.RainToday.unique()
print(weather_classes1)

# Menghitung dan tampilkan metriks evaluator model klasifikasi
from sklearn.metrics import classification_report
print(classification_report(y_test1, y_pred1, target_names = weather_classes1))

#================Penyimpanan model final Rain Today===============

import pickle

#Simpan model naive terbaik yang dihasilkan
#Simpan model dgn nama: Model_Naive_Weather.pkl
pkl_filename = "Model_Naive_Weather_Today.pkl"  
with open(pkl_filename, 'wb') as file:  
    pickle.dump(NBC_model_weather, file)

#======Pemanfaatan model final Rain Today untuk prediksi label dari data baru=======

# Menggunakan model untuk memprediksi kelas pada data baru
pkl_filename = "Model_Naive_Weather_Today.pkl"  
with open(pkl_filename, 'rb') as file:
    loaded_model_Naive_Weather = pickle.load(file)

predict_dataToday = {'Rainfall' :[sys.argv[1]], 'Humidity9am':[sys.argv[2]], 'Humidity3pm':[sys.argv[3]]}
today = pd.DataFrame(predict_dataToday)
today.head()

y_pred_new_Today = loaded_model_KNN_Today.predict(today)
print(y_pred_new_Today)