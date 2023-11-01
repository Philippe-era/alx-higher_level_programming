#!/usr/bin/node

document.addEventListener('DOMContentLoaded', function() {
	const redHeader = document.getElementById('red_header');
	redHeader.addEventListener('click', function() {
		const head = document.querySelectorAll('header');
		head.forEach(function(head) {
			head.style.color = '#FF0000';
		});
	});
});

