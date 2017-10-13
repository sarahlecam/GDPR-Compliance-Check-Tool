$(function(){
	windowed = $("#form");
})

var companyName;

function startForm() {
	windowed.empty();
	$(`<form action="" onsubmit="submitComp(); return false;">`
		+ `<h2>Company Information</h2> <br>`
		+ `Company Name: `
		+ `<input type="text" id="companyName"><br>`
		+ `Company Description: <br>`
		+ `<textarea rows="5" cols="60"></textarea><br>`
		+ `<button type="submit">Continue</button>`
		+ `</form>`).appendTo(windowed);
}

function submitComp() {
	// companyName = $()
	DOPInfo();
}

function DOPInfo() {
	windowed.empty();
	$(`<form action="" onsubmit="return false;">`
		+ `DOP Info: <br>`
		+ `DPOs Name: `
		+ `<input type="text" id="companyName"><br>`
		+ `DPOs Contact Info: `
		+ `<input type="text" id="companyName"><br>`
		+ `<button onclick="startForm()">Back</button>`
		+ `<button onclick="individualData()">Continue</button>`
		+ `</form>`).appendTo(windowed);
}

function individualData() {
	windowed.empty();
	$(`<form action="" onsubmit="return false;">`
		+ `Collected Individual User Data: <br>`
		+ `<input type="checkbox" value="email"> Email<br>`
		+ `<input type="checkbox" value="name"> Name<br>`
		+ `<input type="checkbox" value="address"> Address<br>`
		+ `<button onclick="DOPInfo()">Back</button>`
		+ `<button onclick="showResults()">Continue</button>`
		+ `</form>`).appendTo(windowed);
}

function showResults() {
	windowed.empty();

	// $(`Company Name:` +)

}