
window.onscroll = function() {
	var dist = document.body.getBoundingClientRect().top;
	var menu = document.getElementById("nav-panel");
	if (dist < -100){
		menu.style = "box-shadow: 0 5px 5px rgba(50, 50, 50, 0.5)";
		menu.style.background = "#323232";
	}
	else{
		menu.style = "box-shadow: none";
		menu.style.background = "none";
	}
}