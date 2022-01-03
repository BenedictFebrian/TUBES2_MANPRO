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
				<a href="landingPage.php"><img src="Gambar/logo.png">
			</div>
			<div class="topnav-right">
				<a href="landingPage.php" class="w3-bar-item w3-button home"><b>Home<b></a>
			  	<a href="#" class="w3-bar-item w3-button data">Weather Data</a>
			  	<a href="predictNow.php" class="w3-bar-item w3-button predict">Weather Prediction</a>
			</div>
		</div>

		<div class="judul">
			<p>Predict Your Weather</p>
		</div>

		<div class="predict1">
			<form class="kelas" action="controller.php" method="GET">
			
				<label for="rain">Rainfall:</label>
	  			<input type="text" class="satu" id="rainfall" name="atribut1" placeholder="Nilai Prediction (mm)"><br>

	  			<label for="huma1">Humidity at 9AM:</label>
	  			<input type="text" class="satu" id="humidity9" name="atribut2" placeholder="Nilai Prediction (%)"><br>

	  			<label for="huma2">Humidity at 3PM:</label>
	  			<input type="text" class="satu" id="humidity3" name="atribut3" placeholder="Nilai Prediction (%)">

	  			<br>
	  			<input type="submit" name="Submit" value="Predict" style="width: 20%; margin-left: 20%;">
			</form>

			<br><br><br><br>

			<div class="predictResult">
				<?php
					if (isset($_GET['resultToday'])) {
						if ($_GET['resultToday'] == 1) {
							echo "
							<img src=\"Gambar/todayPredict.png\" style=\"width: 150%\">
							";
						}
						else if ($_GET['resultToday'] == 0){
							echo "
							<img src=\"Gambar/todayPrediction.png\" style=\"width: 150%\">
							";
						}
					}

					echo"<br><br><br><br>";

					if(isset($_GET['resultTommorow'])){
						if ($_GET['resultTommorow'] == 0){
							echo "
							<img src=\"Gambar/tommorowPredict.png\" style=\"width: 150%\">
							";
						}
						else if ($_GET['resultTommorow'] == 1) {
							echo "
							<img src=\"Gambar/tommorowPrediction.png\" style=\"width: 150%\">
							";
						}
					}
				?>
			</div>
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
	</body>
</html>