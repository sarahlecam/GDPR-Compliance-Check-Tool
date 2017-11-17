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
			$(`<div class="rec">`
	            + `<h2>`
	            + recommendation.section
	            + `. `
	            + recommendation.section_name
	            + `</h2>`
	            + recommendation.rec_text
	            + `</div>`).appendTo("#recommendations");

			if (recommendation.flagged == 0) {
				$(`<div class="rec">`
		            + `<h2>`
		            + recommendation.section
		            + `. `
		            + recommendation.section_name
		            + `</h2>`
		            + recommendation.rec_text
		            + `</div>`).appendTo("#recommendations");
			} else {

			}
		}
    });
}

