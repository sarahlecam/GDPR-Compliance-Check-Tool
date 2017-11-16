// Form Processing

// Form div on page
var form_div;

// Keep track of progress
var questionNumber;
var numQuestions;

$(function(){
    form_div = $("#form");
    questionNumber = 1;

    // set total number of questions
    getNumQuestions();

    displayNextQuestion();
});

function displayNextQuestion () {
    if (questionNumber > numQuestions) {
        window.location.href = "index.html";
    } else {
        form_div.empty();
        getQuestion(questionNumber);
        questionNumber++;
    }
}

function setNumQs (numQs) {
    numQuestions = numQs;
}

function getNumQuestions() {
    $.getJSON("api/questions", function(questions){
        setNumQs(questions.length);
    });
}

function getQuestion(qNumber) {
    $.getJSON("api/questions/" + qNumber, function(question){
        $(`<div class="question">`
            + question.question
            + `<form id="privacyField">`
            + `<button type="submit" onClick="saveData(); return false;">Continue</button>`
            + `</form>`
            + `</div>`).appendTo("#form");
        // TODO: Figure out what to print
    });
}

function saveData() {

//     $.ajax({
//         url: "/api/responses",
//         type: "POST",
//         data: JSON.stringify({"companyName": companyName, "address": address, "contact" : contact,"website" : website, "dataType": type, "reason": reason, "shared": share,"dopName": dpoName,"dopContact" : dpoContact,"companyType": companyType}),
//         contentType: "application/json",
//         dataType: "json",
//         success: function (id) {
// //            console.log("success");
//             getInputs(id);
//         },
//         error: function (){
// //            alert("Your receipt entry was not properly processed. Please resubmit your receipt information.");
//         }
//     });
    displayNextQuestion();
    return false;
}

