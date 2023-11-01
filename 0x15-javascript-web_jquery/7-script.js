#!/usr/bin/node

$(document).ready(function () {
	$.getJSON('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (info) {
		$('div#character').text(info.name);
	});
});

