// Form div on page
var check_div;

// Keep track of progress
// var questionNumber;
// var numQuestions;

$(function(){
    check_div = $("#recommendations");
    getRecommendations();
});

function getRecommendations() {
	$.getJSON("api/recs", function(recs){
		for (var i=0; i < recs.length; i++) {
			var recommendation = recs[i];
			var checkImg;
			var flagImg;
			if (recommendation.flagged == 0) {
				flagImg = "clear_flag.png";
			} else {
				flagImg = "flagged.png";
			}
			if (recommendation.completed == 0) {
				checkImg = "unchecked.png";
			} else {
				checkImg = "checked.png";
			}

			$(`<div class="rec_" + ${recommendation.id}>`
				// + <>
	            + `<h3>`
	            + `<input type="image" id="check_${recommendation.section}" src="images/${checkImg}" onClick="toggleCheck(${recommendation.section}); return false;" width="25" height="25">`
	            // + recommendation.section
	            // + `. `
	            + recommendation.section_name
	            + `</h3>`
	            + `<input type="image" id="flag_${recommendation.section}" src="images/${flagImg}" onClick="toggleFlag(${recommendation.section}); return false;" width="48" height="48">`
	            + `<br>`
	            + recommendation.rec_text
	            + `</div>`).appendTo("#recommendations");
		}
    });
}

function toggleFlag(id) {
	// console.log(id)
	if ($("#flag_" + id).attr("src") == "images/clear_flag.png") {
		$("#flag_" + id).attr("src","images/flagged.png");
		$.ajax({
	        url: "/api/recs/" + id,
	        type: "POST",
	        data: JSON.stringify({"flagged": 1}),
	        contentType: "application/json",
	        dataType: "json",
	        success: function (id) {
	           // console.log("success");
	           
	            // getInputs(id);
	        },
	        error: function (){
	           // alert("Your account was not properly created. Please, try signing up again.");
	        }
    	});
	} else {
		$("#flag_" + id).attr("src","images/clear_flag.png");
		$.ajax({
	        url: "/api/recs/" + id,
	        type: "POST",
	        data: JSON.stringify({"flagged": 0}),
	        contentType: "application/json",
	        dataType: "json",
	        success: function (id) {
	           // console.log("success");
	           
	            // getInputs(id);
	        },
	        error: function (){
	           // alert("Your account was not properly created. Please, try signing up again.");
	        }
    	});
	}
}

function toggleCheck(id) {
	// console.log(id)
	if ($("#check_" + id).attr("src") == "images/unchecked.png") {
		$("#check_" + id).attr("src","images/checked.png");
		$.ajax({
	        url: "/api/recs/" + id,
	        type: "POST",
	        data: JSON.stringify({"completed": 1}),
	        contentType: "application/json",
	        dataType: "json",
	        success: function (id) {
	           // console.log("success");
	           
	            // getInputs(id);
	        },
	        error: function (){
	           // alert("Your account was not properly created. Please, try signing up again.");
	        }
    	});
	} else {
		$("#check_" + id).attr("src","images/unchecked.png");
		$.ajax({
	        url: "/api/recs/" + id,
	        type: "POST",
	        data: JSON.stringify({"completed": 0}),
	        contentType: "application/json",
	        dataType: "json",
	        success: function (id) {
	           // console.log("success");
	           
	            // getInputs(id);
	        },
	        error: function (){
	           // alert("Your account was not properly created. Please, try signing up again.");
	        }
    	});
	}
}

