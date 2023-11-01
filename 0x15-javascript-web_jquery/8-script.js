#!/usr/bin/node

$(document).ready(function () {
	$.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
		const collection = [];
		$.each(data.results, function (index, value) {
			collection.push('<li>' + value.title + '</li>');
		});
		$.each(collection, function (index, value) {
			$('ul#list_movies').append(value);
		});
	});
});

