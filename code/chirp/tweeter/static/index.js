function init()
{
	console.log('working');
	loginbtn = $('#login');
	splashdiv = $('#splash');
	logindiv = $('#signin');

	loginbtn.bind('click', loginClick);
}

function loginClick()
{
	// splashdiv.replaceWith(logindiv);
	splashdiv.fadeOut(300, function()
	{
	    $(this).replaceWith(logindiv);
		logindiv.css('display', 'block');
		splashdiv.css('display', 'none');
	});
}

function backClick()
{
	// splashdiv.replaceWith(logindiv);
	logindiv.fadeOut(300, function()
	{
	    $(this).replaceWith(splashdiv);
		splashdiv.css('display', 'block');
		logindiv.css('display', 'none');
	});
}
