$(document).ready(function() { 
    var options = { 
       // target:        '#output1',   // target element(s) to be updated with server response 
        beforeSubmit:  disableForm,  // pre-submit callback 
        success:       enableForm  // post-submit callback 
 
        // other available options: 
        //url:       url         // override for form's 'action' attribute 
        //type:      type        // 'get' or 'post', override for form's 'method' attribute 
        //dataType:  null        // 'xml', 'script', or 'json' (expected server response type) 
        //clearForm: true        // clear all form fields after successful submit 
        //resetForm: true        // reset the form after successful submit 
 
        // $.ajax options can be used here too, for example: 
        //timeout:   3000 
    }; 
    
    // bind to the form's submit event 
    $('#editForm').submit(function() { 
        // inside event callbacks 'this' is the DOM element so we first 
        // wrap it in a jQuery object and then invoke ajaxSubmit 
        $(this).ajaxSubmit(options); 
 
        // !!! Important !!! 
        // always return false to prevent standard browser submit and page navigation 
        return false; 
    }); 
}); 

function disableElem(index) {
	$(this).attr('disabled', 'true');
}

function enableElem(index) {
	$(this).attr('disabled', '');
}

//pre-submit callback 
function disableForm(formData, jqForm, options) {
	$('#editForm').find('select').each(disableElem);
	$('#editForm').find('input').each(disableElem);
	$('#editForm').find('textarea').each(disableElem);
	$('#progress').show();
} 
 
// post-submit callback 
function enableForm(responseText, statusText, xhr, $form)  {
	$('#editForm').find('select').each(enableElem);
	$('#editForm').find('input').each(enableElem);
	$('#editForm').find('textarea').each(enableElem);
	$('#progress').hide();
} 