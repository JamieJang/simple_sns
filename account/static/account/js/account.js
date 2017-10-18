var sel_file;

$(document).ready(function(){
	$("#prof_img").on("change", showImage);
});

function showImage(e){
	var files = e.target.files;
	var filesArr = Array.prototype.slice.call(files);
	filesArr.forEach(function(f){
		if(!f.type.match("image.*")){
			alert("Only Image");
			return;
		}

		sel_file = f;

		var reader = new FileReader();
		reader.onload = function(e){
			$("#profile-image").attr('src',e.target.result);
			$("#profile-image").css('opacity','1');
		}
		reader.readAsDataURL(f);
	});
}

$(window).resize(function(){
	var width = $(window).width();
	if(width < 768){
		$("#change-form").css('width','100%')	;
	}else{
		$("#change-form").css('width','50%')	;
	}
});

$(document).ready(function(){
	var width = $(window).width();
	if(width < 768){
		$("#change-form").css('width','100%')	;
	}else{
		$("#change-form").css('width','50%')	;
	}
});