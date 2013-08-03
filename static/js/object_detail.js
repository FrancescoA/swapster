


$(function(){
	$(".detail-trigger").click(function(handler){
		var obj_name = this.getAttribute('name');
		var obj_owner = this.getAttribute('owner');
		//var path = window.location.pathname;
		var path= "http://127.0.0.1:8000/objects/detail/";
		console.log(obj_name);
		console.log(obj_owner);
		var message = {
			name : obj_name,
			owner : obj_owner,
		}
		$.get(path, message, function(response){
			var responseObj = JSON.parse(response);
			var modal = $("#detail-view");
			modal.modal();
			var owner = responseObj['owner'];
			//console.log(owner)
			modal.find("#owner_thumb").attr('src', owner['imgURL']);



			console.log(response);

		});


			



	});


});