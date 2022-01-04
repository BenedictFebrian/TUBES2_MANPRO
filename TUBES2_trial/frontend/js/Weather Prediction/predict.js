async function startPredict(rainfall, humid9am, humid3pm) {
  const params = new URLSearchParams({
    r: rainfall,
    h9am: humid9am,
    h3pm: humid3pm
  })

  const response = await fetch(`http://localhost:5000/predict?${params}`)
  
  try {
    const data = await response.clone().json()
    document.querySelector('#predict-result').textContent = `Today's Prediction: ${data.result}`
  } catch (_) {
    const data = await response.text()
    document.querySelector('#predict-result').textContent = `Error: ${data}`
  }
}

document.querySelector('button[type="submit"]').addEventListener('click', async (e) => {
  e.preventDefault()
  const rainfall = document.querySelector('input[name="Rainfall"]').value;
  const humid9am = document.querySelector('input[name="Humid9am"]').value;
  const humid3pm = document.querySelector('input[name="Humid3pm"]').value;
  await startPredict(rainfall, humid9am, humid3pm)
})