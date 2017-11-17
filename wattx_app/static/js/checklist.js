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
			$(`<div class="rec_" + ${recommendation.id}>`
				// + <>
	            + `<h3>`
	            + recommendation.section
	            + `. `
	            + recommendation.section_name
	            + `</h3>`
	            + `<input type="image" id="flag_${recommendation.section}" src="images/clear_flag.png" onClick="toggle(${recommendation.section}); return false;" width="48" height="48">`
	            + `<br>`
	            + recommendation.rec_text
	            + `</div>`).appendTo("#recommendations");
		}
    });
}

function toggle(id) {
	// console.log(id)
	if ($("#flag_" + id).attr("src") == "images/clear_flag.png") {
		$("#flag_" + id).attr("src","images/flagged.png");
	} else {
		$("#flag_" + id).attr("src","images/clear_flag.png");
	}
}

