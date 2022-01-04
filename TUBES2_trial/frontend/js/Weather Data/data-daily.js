async function start() {
  const currentUrl = new URL(window.location.href);

  const response = await fetch(`http://localhost:5000/?${currentUrl.searchParams}`)

  try {
    const data = await response.clone().json()

    if (!data.result) {
      document.querySelector('.content').innerHTML = `<strong>Data tidak ditemukan</strong>`
    } else {
      document.querySelector('.content > h1').innerHTML = `<strong>${data.result.Location}</strong> (${data.result.Date})`;

      document.querySelector('.content > .morning .more-info > h1').innerHTML = `${data.result.Temp9am}°`;
      document.querySelector('.content > .afternoon .more-info > h1').innerHTML = `${data.result.Temp3pm}°`;

      document.querySelector('.content > .morning img').src = data.result.RainToday == 'Yes' ? '../../images/Rain.png' : '../../images/Sun-full.png';
      document.querySelector('.content > .afternoon img').src = data.result.RainToday == 'Yes' ? '../../images/Rain.png' : '../../images/Sun-full.png';

      document.querySelector('.content > .morning p').innerHTML = data.result.RainToday == 'Yes' ? `<strong>Rainy day to go outside.</strong>` : `<strong>Sunny day to go outside.</strong>`;
      document.querySelector('.content > .afternoon p').innerHTML = data.result.RainToday == 'Yes' ? `<strong>Rainy day to go outside.</strong>` : `<strong>Sunny day to go outside.</strong>`;

      document.querySelector('.content > .morning .more-info a').href = `MoreDetailMorning.html?${currentUrl.searchParams}`;
      document.querySelector('.content > .afternoon .more-info a').href = `MoreDetailAfternoon.html?${currentUrl.searchParams}`;
    }

  } catch (_) {
    const data = await response.text()
    document.querySelector('.content').innerHTML = `Error: ${data}`
  }
}

start();