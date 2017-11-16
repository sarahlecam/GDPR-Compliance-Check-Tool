// Login page
var login_div;


$(function(){
    login_div = $("#login_div");
    // questionNumber = 1;
});

function addUser() {
	var compName = $("#name").val();
	var email = $("#email").val();
	var password = $("#password").val();

	$.ajax({
        url: "/api/users",
        type: "POST",
        data: JSON.stringify({"company_name": compName, "email": email, "password" : password}),
        contentType: "application/json",
        dataType: "json",
        success: function (id) {
           // console.log("success");
           window.location.href = "survey.html";
            // getInputs(id);
        },
        error: function (){
           alert("Your account was not properly created. Please, try signing up again.");
        }
    });

}