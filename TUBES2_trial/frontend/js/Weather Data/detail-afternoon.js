async function start() {
  const currentUrl = new URL(window.location.href);

  const response = await fetch(`http://localhost:5000/?${currentUrl.searchParams}`)

  try {
    const data = await response.clone().json()

    if (!data.result) {
      document.querySelector('.content').innerHTML = `<strong>Data tidak ditemukan</strong>`
    } else {
      document.querySelector('.content > h1').innerHTML = `<strong>${data.result.Location}</strong> (${data.result.Date})`;

      document.querySelector('.content > .details.left > h1').innerHTML = `${data.result.Temp3pm}°`;

      document.querySelector('.content > .details.left > .info-right').innerHTML = `
        <strong>
          <br>
					<br>
					${data.result.WindDir3pm} ${data.result.WindSpeed3pm} km/h<br>
					${data.result.WindGustDir} ${data.result.WindGustSpeed} km/h<br> 
					${data.result.Humidity3pm}%<br>
					${data.result.Pressure3pm} Pa<br>
					${data.result.Cloud3pm * 8}%<br>
					${data.result.Evaporation}mm<br>
        </strong>
      `;

      document.querySelector('.content > .details.right img').src = data.result.RainToday == 'Yes' ? '../../images/Rain.png' : '../../images/Sun-full.png';
    }

  } catch (_) {
    const data = await response.text()
    document.querySelector('.content').innerHTML = `Error: ${data}`
  }
}

start();