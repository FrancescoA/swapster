

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
		snap : ".snap",
		zIndex: 5,
		snapMode: "inner",
	}

	$(".draggable").draggable(dragoptions)



});