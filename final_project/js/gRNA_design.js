// this function executes our search via an AJAX call
//function runSearch(accession_id) {
//	var formData = {
//		'accession_id': accession_id
//	};

//hide and clear the previous results, if any
//$('#results').hide();
//$('tbody').empty();

// run the javascript once the page is ready
//$(document).ready(function() {
	// add the jQuery UI Selectmenu widget to the PAM sequence select element
//	$('#PAM_seq').selectmenu({
//		classes:{
//			"ui-selectmenu-menu": "highlight"
//		}
//	});

//add tooltip widget to PAM sequence selection label

//var position =$(#PAM_seq).tooltip("option", "position");
//$(#PAM_seq).tooltip("option", "position", { my: "left+15 center", at: "right center" } );


//run the javascript once the page is ready
//$(document).ready(function() {
//	$('#PAM_seq').change(function(){
//		var selectedOption = $(this).val();
//		console.log('Selected PAM sequences:', selectedOption);
//	});
//	$('#accession_id').change(function(){
//		var selectedOption = $(this).val();
//		console.log('Selected accession_id:', selectedOption);
//	});
//});
//$('#gRNA_form').submit(function(event) {
//	event.preventDefault();
//	var formData = $('#gRNA_form').serialize();
//	$.ajax({
//		url: './gRNA_design.cgi',
//		dataType: 'json',
//		data: formData,
//		type: 'POST',
//		success: function(response) {
//			$('#results').html(response.html);
//		},
//		error: function() {
//			alert('An error occurred.');
//			}
//		});
//	});
//}



//The JavaScript file, we use jQuery to listen for the form submit event and prevent the default form submission. We then serialize the form data and use jQuery's ajax method to make an asynchronous POST request to the CGI file. We set the dataType parameter to 'json' so that the response is in JSON format. If the request is successful, we display the response in the results div. If an error occurs, we display an alert message.
