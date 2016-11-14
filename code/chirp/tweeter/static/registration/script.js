$(function() {
    // Nav Tab stuff
    $('.nav-tabs > li > a').click(function() {
        if($(this).hasClass('disabled')) {
            return false;
        } else {
            var linkIndex = $(this).parent().index() - 1;
            $('.nav-tabs > li').each(function(index, item) {
                $(item).attr('rel-index', index - linkIndex);
            });
        }
    });
    $('#step-1-next').click(function() {
        // Check values here
        var isValid = true;

        if(isValid) {
            $('.nav-tabs > li:nth-of-type(2) > a').removeClass('disabled').click();
        }
    });
    $('#step-2-next').click(function() {
        // Check values here
        var isValid = true;

        if(isValid) {
            $('.nav-tabs > li:nth-of-type(3) > a').removeClass('disabled').click();
        }
    });
    $('#step-3-next').click(function() {
        // Check values here
        var isValid = true;

        if(isValid) {
            $('.nav-tabs > li:nth-of-type(4) > a').removeClass('disabled').click();
        }
    });
});

$(function()
{
	$('#step-4-next').click(function()
	{
		$form = $('#form-custom');
		$form.attr('method', 'POST');
		$form.attr('action', 'success.html');
		$form.append('<input name="email" type="email" value=' + $('#email').val() + ' />');
		$form.append('<input name="pass" type="password" value=' + $('#pwd').val() + ' />');
		$form.append('<input name="handle" type="text" value=' + $('#handle').val() + ' />');
		$form.append('<input name="dob" type="date" value=' + $('#dob').val() + ' />');
		$form.append('<input name="gender" type="text" value=' + $('#gender').val() + ' />');
		console.log($form);
		$form.submit();
		// $.post('success.html', $form.serialize());
	});
});
