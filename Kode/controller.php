<?php
	$rainfall = $_GET['atribut1'];
	$humadity9 = $_GET['atribut2'];
	$humadity3 = $_GET['atribut3'];

	$predictToday = exec("python3 predictToday.py $rainfall $humadity9 $humadity3");

	$predictTommorow = exec("python3 predictTommorow.py $rainfall $humadity9 $humadity3");

	header("Location: predictNow.php?resultToday=".$predictToday[1]."&resultTommorow=".$predictTommorow[1]);
?>