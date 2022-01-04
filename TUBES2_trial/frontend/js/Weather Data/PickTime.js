// Tabbed NavBar
function openContent(obj, idContentContainer) {
	var i, x, tablink;

	//Hide all contents
	x = document.getElementsByClassName("tab");
	for (i = 0; i < x.length; i++) {
		x[i].style.display = "none";
	}

	//selected tablink ngilangin .active
	tablink = document.getElementsByClassName("tablink");
	for (i = 0; i < x.length; i++) {
		tablink[i].className = tablink[i].className.replace(" active", "");
	}

	//Show chosen content 
	document.getElementById(idContentContainer).style.display = "block";

	//yg d click tambah class active (text-decoration: underline)
	obj.classList += " active";

}