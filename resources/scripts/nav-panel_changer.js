
window.onscroll = function() {
	var dist = document.body.getBoundingClientRect().top;
	var menu = document.getElementById("nav-panel");
	if (dist < -200){
		menu.style = "box-shadow: 0 5px 5px rgba(120, 120, 120, 0.5)";
		menu.style.background = "#898989";
	}
	else{
		menu.style = "box-shadow: none";
		menu.style.background = "none";
	}
}