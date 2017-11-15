// Form Processing


var windowed;
var companyName;
var companyDescription;
var address;
var contact;
var website;
var dpoName;
var dpoContact;
var companyType;

$(function(){
    windowed = $("#form");
    startForm();
});

function startForm() {
    windowed.empty();
    $(`<form action="" onsubmit="submitComp(); return false;">`
        + `<h2>Company Information</h2> <br>`
        + `Company Name: `
        + `<input type="text" id="companyName" value="HelpMeDate"><br>`
        + `Address: `
        + `<input type="text" id="address" value="1 E Loop Rd., New York, New York 10044"><br>`
        + `Contact Number: `
        + `<input type="text" id="contact" value="(310) 254-5740"><br>`
        + `Company Website: `
        + `<input type="text" id="website" value="helpmedate.com"><br>`
        + `Company Type: `
        + `<input type="text" id="companyType" value="Online Dating Service"><br>`
        + `DPO Name: `
        + `<input type="text" id="dpoName" value="James Mariani"><br>`
        + ` DPO Contact: `
        + `<input type="text" id="dpoContact" value="james@me.com"><br>`
        + `Company Description: <br>`
        + `<textarea rows="5" cols="60" id="description">HelpMeDate.com helps you find that perfect someone by using proprietary algorithms and a little magic.</textarea><br>`
        + `<button type="submit">Continue</button>`
        + `</form>`).appendTo(windowed);
}

function submitComp() {
    companyName = $("#companyName").val();
//	console.log(companyName);
    companyDescription = $("#description").val();
    address = $("#address").val();
    contact = $("#contact").val();
    website = $("#website").val();
    companyType = $("#companyType").val();
    dpoName = $("#dpoName").val();
    dpoContact = $("#dpoContact").val();
//    console.log(companyDescription);
    individualData();
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
    $(`<h2>Collected Individual User Data</h2> <br>`
        + `<form id="privacyField">`
        + `<input type="text" id="type" placeholder="Data Type"><br>`
        + `<textarea rows="5" cols="60" id="dataDescription"></textarea><br>`
        + `<input type="checkbox" id="shared" value="share"> Share <br>`
        + `<button id="save-data" onclick="return saveData()">Save</button>`
        + `</form>`
        + `<table style="width:100%" id="inputList">`
        + `</table>`
        + `<form action="" onsubmit="lastPage(); return false;">`
        //		+ `<input type="text" placeholder="email"> <br>`
        + `<button onclick="startForm()">Back</button>`
        + `<button type="submit">Continue</button>`
        + `</form>`).appendTo(windowed);
    getInputs();
}

function showResults() {
    windowed.empty();
    $(`<div>Company Name: ${companyName} </div>`).appendTo(windowed);
    $(`<div>Company Description: ${companyDescription} </div>`).appendTo(windowed);
    $(`<div>Address: ${address} </div>`).appendTo(windowed);
    $(`<button onclick="individualData()">Back</button>`).appendTo(windowed);

}

function saveData() {
    var type = $("#type").val();
    var reason = $("#dataDescription").val();
    var share;
    if ($('#shared').is(":checked")) {
        share = 1;
    } else {
        share = 0;
    }
    $("#type").val("");
    $("#dataDescription").val("");

    $.ajax({
        url: "http://localhost:5000/api/enterprise",
        type: "POST",
        data: JSON.stringify({"companyName": companyName, "address": address, "contact" : contact,"website" : website, "dataType": type, "reason": reason, "shared": share,"dopName": dpoName,"dopContact" : dpoContact,"companyType": companyType}),
        contentType: "application/json",
        dataType: "json",
        success: function (id) {
//            console.log("success");
            getInputs(id);
        },
        error: function (){
//            alert("Your receipt entry was not properly processed. Please resubmit your receipt information.");
        }
    });
    return false;
}

function getInputs() {

    var table = `<tr style='height: 60px'><th>Data Type</th><th>Reason</th><th>Share?</th></tr>`;
    $("#inputList").html(table);
    $.getJSON("/" + companyName, function(inputs){
        for(var i=0; i < inputs.length; i++) {
            var input = inputs[i];

            $(`<tr class="input" style="height: 100px"->`
                + `<td class="type">${input.dataType}</td>`
                + `<td class="reason">${input.reason}</td>`
                + `<td class="share">${input.shared}</td>`
                + `</td>`
                + `</tr>`)
                .appendTo($("#inputList"));
        }
    });

    return false;
}

function lastPage() {
    windowed.empty();
    $(`<h2>Tools</h2> <br>`
        + `<div>`
        + `<a id="button" href="http://localhost:8080/notice/${companyName}" target="_blank">Privacy Notice</a>`
        + `<a id="button" href="http://localhost:8080/policy" target="_blank">Privacy Policy</a>`
        + `<a id="button" href="http://localhost:8080/form/${companyName}" target="_blank">Form</a>`
        + `</div>`
    ).appendTo(windowed);
    getInputs();
}
