
var nav = document.getElementById('navb');
window.onscroll = function () {
    if (window.pageYOffset > 300) {
        nav.style.background = "rgba(0,0,0,0.5)";
        nav.style.height = "90px";
        nav.style.width="100%";
    }
    else {
        nav.style.background = "transparent";
    }
}

$(document).ready(function () {
    $('.menu').click(function () {
        $('ul').toggleClass('active');
    })
})


$(document).ready(function () {
    if($('.sideTabs a').length)
		{
			var links = $('.sideTabs a');
	    	links.each(function()
	    	{
                var ele = $(this);
                console.log(ele)
	    		var target = ele.data('scroll-to');
	    		ele.on('click', function(e)
	    		{
                    e.preventDefault();
                    $('html, body').animate({ scrollTop: $(target).offset().top-90});
	    		});
	    	});
		}	
});
