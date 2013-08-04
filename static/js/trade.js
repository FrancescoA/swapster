

$(function(){

	/*
	var popoptions = {
		trigger : 'hover',
		title : "More Detail",
		placement: 'top',
		delay : { show: 500, hide: 400 },
	}

	$('.draggable').popover(popoptions)
	
	*/

	var dragoptions = {
		snap : ".box",
		zIndex: 100,
	}

	$(".draggable").draggable(dragoptions)



});