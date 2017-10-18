/*
	Profile Page -- element size according to screen size
*/
$(window).resize(function(){
	var width = $(window).width();
	if(width < 768){
		$("#self-content").css('width','100%');
		$("#profile").css('width','100%');
		$("#profile").css('height','35%');
		$("#self-image").css('width','100px');
		$("#self-image").css('height','100px');
	}else{
		$("#self-content").css('width','50%');
		$("#profile").css('width','30%');
		$("#profile").css('height','100%');
		$("#self-image").css('width','150px');
		$("#self-image").css('height','150px');
	}
});
$(document).ready(function(){
	var width = $(window).width();
	if(width < 768){
		$("#self-content").css('width','100%');
		$("#profile").css('width','100%');
		$("#profile").css('height','35%');
		$("#self-image").css('width','100px');
		$("#self-image").css('height','100px');
	}else{
		$("#self-content").css('width','50%');
		$("#profile").css('width','30%');
		$("#profile").css('height','100%');
		$("#self-image").css('width','150px');
		$("#self-image").css('height','150px');
	}
});

/*
	In home page -- writing post function
*/
$(document).ready(function(){
	var width = $(window).width();
	if(width < 600){
		$("div#post-form").css('width','100%')
	}else{
		$("div#post-form").css('width','50%')
	}

	$("textarea#content").focus(function(){
		$("input#tags").css('display','none');
		$("input#location").css('display','none');
		$("#marker").css('display','none');
	});
});
$(window).resize(function(){
	var width = $(window).width();
	if(width < 600){
		$("div#post-form").css('width','100%')
	}else{
		$("div#post-form").css('width','50%')
	}
});

var showLocation = function(){
	if($("input#location").css('display') == 'none'){
		$("input#location").css('display','initial');
		$("#marker").css('display','initial');
		$("input#tags").css('display','none');
	}else{
		$("input#location").css('display','none');
		$("#marker").css('display','none');
	}
}
var showTag = function(){
	if($("input#tags").css('display') == 'none'){
		$("input#tags").css('display','initial');
		$("input#location").css('display','none');
		$("#marker").css('display','none');
	}else{
		$("input#tags").css('display','none');
	}
}

/*
	When mouse hover to div#post, show config and delete button
*/
$(document).ready(function(){
	$("div.post").hover(function(){
		$('#delete',this).css('display','initial');
		$('#mod',this).css('display','initial');
	}, function(){
		$('#delete',this).css('display','none');
		$('#mod',this).css('display','none');
	});
});