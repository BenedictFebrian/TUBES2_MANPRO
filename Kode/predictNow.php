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

		<div>
		<form class="kelas" action={{url_for('predictNow')}} method="POST">
		
			<label for="rain">Rainfall:</label>
  			<input type="text" class="satu" id="atribut" name="atribut1" placeholder="Prediction Data Atribut"><br>

  			<label for="huma1">Humidity at 9AM:</label>
  			<input type="text" class="tiga" id="atribut" name="atribut2" placeholder="Prediction Data Atribut"><br>

  			<label for="huma2">Humidity at 3PM:</label>
  			<input type="text" class="tiga" id="atribut" name="atribut3" placeholder="Prediction Data Atribut"><br>

  			<label for="sunshine">Sunshine:</label>
  			<input type="text" class="dua" id="atribut" name="atribut4" placeholder="Prediction Data Atribut">
		</form>

		<div class="tombol">
			<a href="thePrediction.php"><button type="submit">Predict Now!</button></a>
		</div>

		<!-- <?php
	        // if(isset($_GET["atribut1"]) && isset($_GET["atribut2"]) && isset($_GET["atribut3"]) && isset($_GET["atribut4"])){
	        // 	   $a=$_GET["atribut1"];
	        //     $b=$_GET["atribut2"];
	        //     $c=$_GET["atribut3"];
	        //     $d=$_GET["atribut4"];
	        
	        //     $tmp = exec("C:/xampp/htdocs/catherine/predict/python C:/xampp/htdocs/catherine/predict/model.py 2>&1".$a." ".$b." ".$c." ".$d);
	        // }
	    ?> -->
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