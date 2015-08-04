$(document).ready(function() {
  	$('select').chosen();
	$('input.number').keyup(function(event) {

	  	// skip for arrow keys
	  	if(event.which >= 37 && event.which <= 40) return;

	  	// format number
	  	$(this).val(function(index, value) {
	    	return value
	      	.replace(/\D/g, "")
	      	.replace(/\B(?=(\d{3})+(?!\d))/g, ",");
	  	});
	});
	bindPostCommentHandler();
});

function bindPostCommentHandler() {
    $('#form-comment input.submit-preview').remove();
    $('#form-comment').submit(function() {
        $.ajax({
            type: "POST",
            data: $('#form-comment').serialize(),
            url: "/comments/post/",
            cache: false,
            dataType: "html",
            success: function(html, textStatus) {
                $('#response-comment').replaceWith(html);
                bindPostCommentHandler();
                $('#id_comment').val('');
                var comment = $('#id_comment').val();
                $('#comments').append(comment);
            },
            error: function (XMLHttpRequest, textStatus, errorThrown) {
                $('#response-comment').replaceWith('Your comment was unable to be posted at this time.  We apologise for the inconvenience.');
            }
        });
        return false;
    });
}