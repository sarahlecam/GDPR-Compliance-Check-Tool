// Form Processing


var windowed;
// var companyName;
// var companyDescription;
// var address;
// var contact;
// var website;
// var dpoName;
// var dpoContact;
// var companyType;
var questionNumber;
var numQuestions;


$(function(){
    windowed = $("#form");
    questionNumber = 1;
    getNumQuestions();
    displayNextQuestion();
});

function displayNextQuestion () {
    if (questionNumber > numQuestions) {
        window.location.href = "index.html";
    } else {
        windowed.empty();
        getQuestion(questionNumber);
        // $(`<form action="" onsubmit="displayNextQuestion(); return false;">`
        //     + `<button type="submit">Continue</button>`
        //     + `</form>`).appendTo(windowed);
        questionNumber++;

    }
}

function setNumQs (numQs) {
    numQuestions = numQs;
}

function getNumQuestions() {
    $.getJSON("/questions/", function(questions){
        setNumQs(questions.length);
    });
}

function getQuestion(qNumber) {
    $.getJSON("/questions/" + qNumber, function(question){
        $(`<div class="question">`
            + question.question
            + `</div>`
            + `<button type="submit" onClick="displayNextQuestion(); return false;">Continue</button>`).appendTo("#form");
        // TODO: Figure out what to print
    });
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
