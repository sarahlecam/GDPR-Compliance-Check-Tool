// Form Processing

// Form div on page
var form_div;

// Keep track of progress
var questionNumber;
var numQuestions;

$(function(){
    form_div = $("#form");
    questionNumber = 0;

    // set total number of questions
    getNumQuestions();

    displayNextQuestion();
});

function displayNextQuestion () {
    if (questionNumber == numQuestions) {
        $.ajax({
            url: "api/recs",
            type: "POST",
        });
        window.location.href = "checklist.html";
    } else {
        questionNumber++;
        form_div.empty();
        getQuestion(questionNumber);
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
    if (qNumber == 1) {
        $.getJSON("api/questions/" + qNumber, function(question){
            $(`<div class="question">`
                + `<h2>`
                + question.section
                + `. `
                + question.section_name
                + `</h2>`
                + question.question
                + `<form id="privacyField">`
                + `<input type="radio" name="response" value="true" id="1"> Yes<br>`
                + `<input type="radio" name="response" value="false" id="2"> No<br>`
                + `<button type="submit" onClick="saveData(); return false;">Continue</button>`
                + `</form>`
                + `</div>`).appendTo("#form");
        });
    } else {
        $.getJSON("api/questions/" + qNumber, function(question){
            $(`<div class="question">`
                + `<h2>`
                + question.section
                + `. `
                + question.section_name
                + `</h2>`
                + question.question
                + `<form id="privacyField">`
                + `<input type="radio" name="response" value="true"> Yes<br>`
                + `<input type="radio" name="response" value="false"> No<br>`
                + `<button onClick="goBack(); return false;">Back</button>`
                + `<button type="submit" onClick="saveData(); return false;">Continue</button>`
                + `</form>`
                + `</div>`).appendTo("#form");
        });
    }
}

function saveData() {
    if ($('input[name=response]:checked').is(':checked')) {
        var response = $('input[name=response]:checked').val();
        // console.log(response);/
        // TODO: fix save
        $.ajax({
            url: "api/responses",
            type: "POST",
            data: JSON.stringify({"question_id": questionNumber, "response": response}),
            contentType: "application/json",
            dataType: "json",
            success: function (stuff) {
               console.log("success");
            },
            error: function (){
               // console.log("nope");
    //            alert("Your receipt entry was not properly processed. Please resubmit your receipt information.");
            }
        });
        displayNextQuestion();
    }
}

function goBack() {
    questionNumber = questionNumber - 2;
    displayNextQuestion ();
}

