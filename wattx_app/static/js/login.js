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
         error: function(jqxhr) {
            error_code = jqxhr.status;
            if (error_code == 401)
            {
              $("#error_area").text("Email and/or password does not match. Try again.");
            }
        // error: function (){
        //    alert("Email and/or password does not match. Try again.");
        }
    });

}

function log() {
    if (!login_div.is(":visible")) {
        signup_div.hide();
        login_div.show();
        $("#title").text("Login");
        $("#switch2").css("background", "#transparent");
        $("#switch1").css("background", "#ffffff");
    }
}

function sign() {
    if (login_div.is(":visible")) {
        login_div.hide();
        signup_div.show();
        $("#title").text("Sign Up");
        $("#switch1").css({"background-color": "transparent"});
        // $("#switch2").css("background", "#ffffff");
    }
}


