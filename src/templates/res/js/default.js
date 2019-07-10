$( document ).ready(function() 
{
	$("#ibm-support").click(function(e) 
	{
		e.preventDefault();
		showModal();
	});

	$(".modal-exit").click(function(e) 
	{
		hideModal();
	});

	$(".modal-bg").click(function(e) 
	{
		hideModal();
	});

	$("#eight-ball-query").on('keyup', function (e)
	{
		if (e.keyCode == 13)
	    	{
			$.get( "/eight-ball", function( data )
			{
		    		$( "#eight-ball-answer" ).html( data );
			});
	    	}
	});
});

function showModal()
{
	$(".modal").addClass("active");
	$(".modal-bg").addClass("active");
	
	$('html, body').css(
	{
		overflow: 'hidden',
		height: '100%'
	});
}

function hideModal()
{
	$(".modal").removeClass("active");
	$(".modal-bg").removeClass("active");

	$('html, body').css(
	{
		overflow: 'auto',
		height: 'auto'
	});	
}
