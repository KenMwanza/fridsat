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

    $(".vote_form").submit(function(e) 
    {
        e.preventDefault(); 
        var btn = $(".upvote span");
        var l_id = $(".hidden_id", this).val();
        btn.attr('disabled', true);
        $.post("/reviews/vote/", $(this).serializeArray(),
        function(data) {
            if(data["voteobj"]) {
                btn.text("Downvote");
            }
            else {
                btn.text("Upvote");
            }
        });
        btn.attr('disabled', false);
    });
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
                var comment = $('#id_comment').val();
                $('#id_comment').val('');
                $('.comments #comments').prepend('<dd>' + '<p>' + comment + '</p>' + '</dd>');
            },
            error: function (XMLHttpRequest, textStatus, errorThrown) {
                $('#response-comment').replaceWith('Your comment was unable to be posted at this time.  We apologise for the inconvenience.');
            }
        });
        return false;
    });
}