$(document).ready(function() {
    var options = {
        target:        '#editForm1',   // target element(s) to be updated with server response
        beforeSubmit:  disableForm,  // pre-submit callback
        success:       enableForm,  // post-submit callback
    };
    $('#editForm1').ajaxForm(options);
});

function disableElem(index) {
    $(this).attr('disabled', 'true');
}

//pre-submit callback
function disableForm(formData, jqForm, options) {
    $('#editForm1').find('input').each(disableElem);
    $('#editForm1').find('textarea').each(disableElem);
    $('#progress').show();
    return true;
}

// post-submit callback
function enableForm(responseText, statusText, xhr, $form)  {
    $('#editForm1').find('input').removeAttr('disabled');
    $('#editForm1').find('textarea').removeAttr('disabled');
    $('#progress').hide();
}
