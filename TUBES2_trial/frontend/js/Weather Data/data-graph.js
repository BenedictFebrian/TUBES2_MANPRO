async function start() {
  const currentUrl = new URL(window.location.href);

  const response = await fetch(`http://localhost:5000/?${currentUrl.searchParams}`)

  try {
    const data = await response.clone().json()

    if (!data.result && data.result.length) {
      document.querySelector('.content').innerHTML = `<strong>Data tidak ditemukan</strong>`
    } else {
      document.querySelector('.content > h1').innerHTML = `<strong>${data.result[0].Location}</strong> (${data.result[0].Date} - ${data.result[data.result.length - 1].Date})`

      const ctx = document.getElementById('chart');
      const chart = new Chart(ctx, {
        type: 'line',
        data: {
          labels: data.result.map(d => {
            const a = d.Date.split('-')
            return `${a[2]}-${a[1]}`
          }),
          datasets: [{
            label: 'Average Temperature',
            data: data.result.map(d => (d.Temp9am + d.Temp3pm) / 2),
            borderColor: 'red',
            backgroundColor: 'red',
          }, {
            label: 'Humidity',
            data: data.result.map(d => (d.Humidity9am + d.Humidity3pm) / 2),
            borderColor: 'blue',
            backgroundColor: 'blue',
          }]
        }
      });
    }

  } catch (err) {
    console.log(err)
    const data = await response.text()
    document.querySelector('.content').innerHTML = `Error: ${data}`
  }
}

start();