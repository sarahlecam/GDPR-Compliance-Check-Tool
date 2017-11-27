// Login page
var login_div;
var signup_div;


$(function(){
    login_div = $("#login_div");
    signup_div = $("#signup_div");
});

function addUser() {
	var compName = $("#name").val();
	var email = $("#email").val();
	var password = $("#password").val();

	$.ajax({
        url: "/api/users/signup",
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

function logInUser() {
	var email = $("#email_login").val();
  console.log(email)
	var password = $("#password_login").val();
  console.log(password)

	$.ajax({
        url: "/api/users/login",
        type: "POST",
        data: JSON.stringify({"email": email, "password" : password}),
        contentType: "application/json",
        dataType: "json",
        success: function (id) {
           // console.log("success");
           window.location.href = "survey.html";
            // getInputs(id);
        },
        error: function (){
           alert("Email and/or password does not match. Try again.");
        }
    });

}
