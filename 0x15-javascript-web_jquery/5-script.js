#!/usr/bin/node

$(document).ready(function () {
	$('div#add_item').on('click', function () {
		$('ul.my_list').append('<li>Item</li>');
	});
});
