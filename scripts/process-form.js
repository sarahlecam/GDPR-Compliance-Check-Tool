$( document ).ready(function() {
    console.log("RExADY");
    // var newDiv = makeElement();
    // $( "#nameMsg" ).hide();
    // $(newDiv).hide();
    // $( "#name" ).focusin(function() {
    //     show(newDiv);
    // });
    // $( "#name" ).focusout(function() {
    //     hide(newDiv);
    // });
});


function show(dived) {
    $(dived).show();
}

function hide(dived) {
    $(dived).hide();
}

function makeElement() {
    var nameBox = document.createElement("div");
    nameBox.setAttribute("id", "nameMsg");
    // nameBox.setAttribute("");
    nameBox.innerHTML = "Your name is being collected to able to murder you in the future !!!";
    $(nameBox).appendTo(document.body);
}