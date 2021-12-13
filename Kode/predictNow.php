<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title>Predict Now</title>
		<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
		<link href="style/stylePredictNow.css" type="text/css" rel="stylesheet">
	</head>
	<body>
		<div class="topnav">
			<div class="gambar">
				<a href="landingPage.html"><img src="Gambar/logo.png">
			</div>
			<div class="topnav-right">
				<a href="landingPage.html" class="w3-bar-item w3-button home"><b>Home<b></a>
			  	<a href="#" class="w3-bar-item w3-button data">Weather Data</a>
			  	<a href="predictNow.html" class="w3-bar-item w3-button predict">Weather Prediction</a>
			</div>
		</div>

		<div class="judul">
			<p>Predict Your Weather</p>
		</div>

		<form class="kelas">
			<label for="atribut"></label><br>
  			<input type="text" id="atribut" name="atribut" placeholder="Prediction Data Atribut">
  			<input type="text" id="atribut" name="atribut" placeholder="Prediction Data Atribut">
  			<input type="text" id="atribut" name="atribut" placeholder="Prediction Data Atribut">
  			<input type="text" id="atribut" name="atribut" placeholder="Prediction Data Atribut">
  			<input type="text" id="atribut" name="atribut" placeholder="Prediction Data Atribut">
  			<input type="text" id="atribut" name="atribut" placeholder="Prediction Data Atribut">
  			<input type="text" id="atribut" name="atribut" placeholder="Prediction Data Atribut">
  			<input type="text" id="atribut" name="atribut" placeholder="Prediction Data Atribut">
		</form>

		<div id="list1" class="dropdown-check-list" tabindex="100">
		  <span class="anchor">Choose Minimal 2</span>
		  <ul class="items">
		  	<li><b>Prediction Data</b></li>
		    <li><input type="checkbox" /> Rainfall </li>
		    <li><input type="checkbox" /> Humidity at 9AM</li>
		    <li><input type="checkbox" /> Humidity at 3PM </li>
		    <li><input type="checkbox" /> Pressure </li>
		    <li><input type="checkbox" /> Sunshine </li>
		    <li><input type="checkbox" /> Cloud 9AM </li>
		    <li><input type="checkbox" /> Cloud 3PM</li>
		    <li><input type="checkbox" /> Evaporation </li>
		  </ul>
		</div>

		<div class="tombol">
			<a href="thePrediction.html"><button>Predict Now!</button></a>
		</div>

		<div class="sun">
			<img src="Gambar/sun2.png">
		</div>

		<div class="footer">
			<img src="Gambar/Footer.png">
		</div>

		<div class="moon">
			<img src="Gambar/moon2.png">
		</div>

		<script>
			var checkList = document.getElementById('list1');
			checkList.getElementsByClassName('anchor')[0].onclick = function(evt) {
			  if (checkList.classList.contains('visible'))
			    checkList.classList.remove('visible');
			  else
			    checkList.classList.add('visible');
			}
		</script>
	</body>
</html>