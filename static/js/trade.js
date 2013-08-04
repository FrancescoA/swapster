

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
		stop: snapTrack,
	}

	$(".draggable1").draggable(dragoptions1)

	var dragoptions2 = {
		snap : ".snap2",
		zIndex: 5,
		snapMode: "inner",
		stop: snapTrack,
	}

	$(".draggable2").draggable(dragoptions2)

	var snapmap = {}
	function snapTrack(){

		/* Get the possible snap targets: */
		var snapped = $(this).data('ui-draggable').snapElements;

		/* Pull out only the snap targets that are "snapping": */
		var snappedTo = $.map(snapped, function(element) {
			return element.snapping ? element.item : null;
		});
		//Basically snappedTo is the span element that this word "snappedTo"
					
		//Every time map:
		// the id of the blank we snapped to (which is equal to the correct word) 
		 //     to
		// the inner html of "this" (the word). To check for correctness we just make sure that key == value
		for(var i = 0 ; i < snappedTo.length ; i++){
			snapmap[this.getAttribute('name')] = snappedTo[i].getAttribute('class')
		}
	}

	function makeOffer(){

		
	}

				



});