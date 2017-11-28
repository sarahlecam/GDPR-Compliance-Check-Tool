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
           window.location.href = "checklist.html";
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


function log() {
    if (!login_div.is(":visible")) {
        signup_div.hide();
        login_div.show();
        $("#title").text("Login");
        $("#switch2").style("background", "transparent", "important");
        $("#switch2").style("color", "#ffffff", "important");
        $("#switch2").style("border-color", "#ffffff", "important");
        $("#switch1").style("background", "#ffffff", "important");
        $("#switch1").style("color", "#6e7d93", "important");
        $("#switch1").style("border-color", "#6e7d93", "important");
    }
}

function sign() {
    if (login_div.is(":visible")) {
        login_div.hide();
        signup_div.show();
        $("#title").text("Sign Up");
        $("#switch1").style("background", "transparent", "important");
        $("#switch1").style("color", "#ffffff", "important");
        $("#switch1").style("border-color", "#ffffff", "important");
        $("#switch2").style("background", "#ffffff", "important");
        $("#switch2").style("color", "#6e7d93", "important");
        $("#switch2").style("border-color", "#6e7d93", "important");
        // $("#switch2").css("background", "#ffffff");
    }
}


