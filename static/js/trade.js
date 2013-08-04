

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

	var dragoptions1 = {
		snap : ".snap1",
		zIndex: 5,
		snapMode: "inner",
	}

	$(".draggable1").draggable(dragoptions1)

	var dragoptions2 = {
		snap : ".snap2",
		zIndex: 5,
		snapMode: "inner",
	}

	$(".draggable2").draggable(dragoptions2)

});