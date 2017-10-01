/* function runs when document ready */
$( document ).ready(function() {

    // Making a new page element for showing policy info
    var newDiv = makeElement();

    // when name element is touched, update text and show info display information
    $( "input" ).focusin(function() {
        show(newDiv, this);
    });

    $( "select" ).focusin(function() {
        show(newDiv, this);
    });

    $( "textarea" ).focusin(function() {
        show(newDiv, this);
    });


    // hide when user moves out of input box
    $( "input" ).focusout(function() {
        hide(newDiv);
    });

    $( "select" ).focusout(function() {
        hide(newDiv);
    });

    $( "textarea" ).focusout(function() {
        hide(newDiv);
    });

});


/* Show div */
function show(dived, input) {

    // edit inner html according to input field
    var inputID = input.getAttribute('id');

    if (inputID == "name") {
        dived.innerHTML = "Your name is being collected and will be stored in our data base.";
    } else if (inputID == "mail") {
        dived.innerHTML = "Your email is being collected and will be stored in our data base.";
    } else if (inputID == "password") {
        dived.innerHTML = "Your password is being collected for identification purposes only.";
    } else if (inputID == "under_13" || inputID == "over_13") {
        dived.innerHTML = "Your age range is being collected only to identify your elegibility and will not be stored.";
    } else {
        dived.innerHTML = "This information will be stored and shared with relevant 3rd parties.";
    }

    $(dived).show();
}



/* Hide div */
function hide(dived) {
    dived.innerHTML = "";
    $(dived).hide();
}

/* create empty div to store policy info */
function makeElement() {
    var newDiv = document.createElement("div");
    newDiv.setAttribute("id", "policy-box");
    newDiv.style.display = 'none';
    $(newDiv).appendTo(document.body);
    return newDiv;
}