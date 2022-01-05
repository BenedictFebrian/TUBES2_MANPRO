async function start() {
  const currentUrl = new URL(window.location.href);

  const response = await fetch(`http://localhost:5000/?${currentUrl.searchParams}`)

  try {
    const data = await response.clone().json()

    if (!data.result && data.result.length) {
      document.querySelector('.content').innerHTML = `<strong>Data tidak ditemukan</strong>`
    } else {
      document.querySelector('.content > div > h1').innerHTML = data.result[0].Location;

      let res = ``;

      for (const d of data.result) {
        res += `
          <div class="data-daily" style="display: block;">
              <span class="date">${d.Date}</span>
              ${d.RainToday == 'Yes' ?
              '<img src="../../images/Rain.png" style="width: 20px; height: auto;">' :
              '<img src="../../images/Sun-full.png" style="width: 20px; height: auto;">'
              }
              <strong>${d.Temp9am}°/${d.Temp3pm}°</strong>
              <button>
                  <a href="DataDaily.html?city=${currentUrl.searchParams.get('city')}&date=${d.Date}">More Details</a>
              </button>
          </div>
        `
      }

      document.querySelector('.content > .data-monthly').innerHTML = res;
      document.querySelector('.content > div > button > a').href = `DataGraph.html?${currentUrl.searchParams}`;
    }

  } catch (_) {
    const data = await response.text()
    document.querySelector('.content').innerHTML = `Error: ${data}`
  }
}

start();