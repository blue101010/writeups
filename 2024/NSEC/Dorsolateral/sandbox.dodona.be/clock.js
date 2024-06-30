// https://sandbox.dodona.be/en/activities/527398301/description/sfMaFnqJUWDJNtWC/media/clock.js
//https://dodona.be/en/courses/1/series/279/activities/527398301/

Clock = function(args) {
    
	// process arguments passed to the constructor
    var $clock_display = $(args.clock_display),
	    $clock_info = $(args.clock_info);
    
    var hours = 0,
        minutes = 0;
    
	function display_seconds(sec) {
		$('.second-row > div', $clock_display).toggleClass('on', (sec % 2 === 1));
	};
	
	function display_hours_minutes() { 

		// display hours
		var h2 = hours % 5;
		var h1 = (hours - h2) / 5;
		
		$('.hour-top.row > div', $clock_display).each(function(i) {
			$(this).toggleClass('on', (--h1 >= 0));
		});
		
		$('.hour-bottom.row > div', $clock_display).each(function(i) {
			$(this).toggleClass('on', (--h2 >= 0));
		});
		
		// display minutes
		var m2 = minutes % 5;
		var m1 = (minutes - m2) / 5;
		
		$('.minute-top.row > div', $clock_display).each(function(i) {
			$(this).toggleClass('on', (--m1 >= 0));
		});
		
		$('.minute-bottom.row > div', $clock_display).each(function(i) {
			$(this).toggleClass('on', (--m2 >= 0));
		});
		
	};
	
	// return public interface
	return {
		
		set_time: function(hr, min) {
			hours = hr;
			minutes = min;
			display_hours_minutes();
		},
		
		display_seconds: display_seconds
		
	};
	
};