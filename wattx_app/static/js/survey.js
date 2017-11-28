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
        window.location.href = "checklist.html";
    } else if (questionNumber == 0) {
        $.ajax({
            url: "/api/responses",
            type: "GET",
            contentType: "application/json",
            dataType: "json",
            success: function (responses) {
                qNumber = responses.length;
                if (qNumber >= numQuestions) {
                    window.location.href = "checklist.html";
                } else {
                  getQuestion(qNumber + 1);  
                }
            },
            error: function (){
            }
        });
    } else {
        questionNumber++;
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
    questionNumber = qNumber;
    form_div.empty();
    if (qNumber == 1) {
        $.getJSON("api/questions/" + qNumber, function(question){
            $(`<div class="question">`
                + `<h2>`
                + question.section_name
                + `</h2>`
                + `<div id="ques">`
                + question.order
                + `. `
                + question.question
                + `</div>`
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
                + question.section_name
                + `</h2>`
                + `<div id="ques">`
                + question.order
                + `. `
                + question.question
                + `</div>`
                + `<form id="privacyField">`
                + `<input type="radio" name="response" value="true"> Yes<br>`
                + `<input type="radio" name="response" value="false"> No<br>`
                + `<button type="submit" onClick="saveData(); return false;">Continue</button>`
                + `<button onClick="goBack(); return false;">Back</button>`
                
                + `</form>`
                + `</div>`).appendTo("#form");
        });
    }
    $.ajax({
        url: "/api/responses/" + qNumber,
        type: "GET",
        contentType: "application/json",
        dataType: "json",
        success: function (response) {
           if (response.response == "true") {
                checkRadio("true");
            } else {
                checkRadio("false");
            }
        },
        error: function (){
           // console.log("nope");
//            alert("Your receipt entry was not properly processed. Please resubmit your receipt information.");
        }
    });
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

(function($) {    
  if ($.fn.style) {
    return;
  }

  // Escape regex chars with \
  var escape = function(text) {
    return text.replace(/[-[\]{}()*+?.,\\^$|#\s]/g, "\\$&");
  };

  // For those who need them (< IE 9), add support for CSS functions
  var isStyleFuncSupported = !!CSSStyleDeclaration.prototype.getPropertyValue;
  if (!isStyleFuncSupported) {
    CSSStyleDeclaration.prototype.getPropertyValue = function(a) {
      return this.getAttribute(a);
    };
    CSSStyleDeclaration.prototype.setProperty = function(styleName, value, priority) {
      this.setAttribute(styleName, value);
      var priority = typeof priority != 'undefined' ? priority : '';
      if (priority != '') {
        // Add priority manually
        var rule = new RegExp(escape(styleName) + '\\s*:\\s*' + escape(value) +
            '(\\s*;)?', 'gmi');
        this.cssText =
            this.cssText.replace(rule, styleName + ': ' + value + ' !' + priority + ';');
      }
    };
    CSSStyleDeclaration.prototype.removeProperty = function(a) {
      return this.removeAttribute(a);
    };
    CSSStyleDeclaration.prototype.getPropertyPriority = function(styleName) {
      var rule = new RegExp(escape(styleName) + '\\s*:\\s*[^\\s]*\\s*!important(\\s*;)?',
          'gmi');
      return rule.test(this.cssText) ? 'important' : '';
    }
  }


  // The style function
  $.fn.style = function(styleName, value, priority) {
    // DOM node
    var node = this.get(0);
    // Ensure we have a DOM node
    if (typeof node == 'undefined') {
      return this;
    }
    // CSSStyleDeclaration
    var style = this.get(0).style;
    // Getter/Setter
    if (typeof styleName != 'undefined') {
      if (typeof value != 'undefined') {
        // Set style property
        priority = typeof priority != 'undefined' ? priority : '';
        style.setProperty(styleName, value, priority);
        return this;
      } else {
        // Get style property
        return style.getPropertyValue(styleName);
      }
    } else {
      // Get CSSStyleDeclaration
      return style;
    }
  };
})(jQuery);

function goBack() {
    questionNumber = questionNumber - 2;
    displayNextQuestion ();
}

function checkRadio (value) {
    $('input[name=response][value=' + value + ']').attr('checked', 'checked');
 }

