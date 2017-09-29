$(function () {
	console.log("cool");
	turnFormGreen();
})

function turnFormGreen() {
	$("form").each(function() {
		// console.log(this);
		$("input").each(function () {
			// console.log("hey");

			this.setAttribute("onclick", "showbox();");
			// this.css({"background-color": "blue"});
		});
		// this.setAttribute("style", "brackgroundColor: green;");
	})
}

function showbox() {
	console.log("Hey");
}