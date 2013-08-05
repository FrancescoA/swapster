
$(function(){
	var obj_name;
	var obj_owner;
	$(".detail-trigger").click(function(handler){
		obj_name = this.getAttribute('name');
		obj_owner = this.getAttribute('owner');
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
			var object = responseObj['object'];
			//console.log(owner)
			modal.find("#owner_thumb").attr('src', owner['imgURL']);
			modal.find(".modal-title").html(obj_name);
			modal.find('#picture-full').attr('src', object['imgURL']);
			modal.find("#object-summary").html(object['summary']);
			modal.find("#object-description").html(object['description']);
			modal.find("#owner").attr('href', "/traders/"+obj_owner);
			modal.find("#want").attr('href', '/traders/'+obj_owner+"/trade");
			console.log(response);
		});
	});
});