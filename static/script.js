$(document).ready(function () {
	console.log('Test!');

	$(document).ajaxStart(function () {
		$('#fidget-spinner').css('display', 'block');
		$('#resultsList').css('display', 'none');
	});

	$(document).ajaxStop(function () {
		$('#fidget-spinner').css('display', 'none');
		$('#resultsList').css('display', 'block');
	});

	$('#btn').click(function () {
		var school = $('#search').val() || 'Arizona State University';
		console.log('School: ' + encodeURIComponent(school));

		$('#resultsList').html('');

		$.getJSON('/get_profiles?school=' + school, function (data) {
			var users = data.users;

			$('#resultsList').html(users);

			console.log(users);

			for (var i = 0; i < users.length; i++) {
				console.log(users[i].html_url);

				var email = users[i].email || '';

				var html = '<li class="list-group-item">';
				html += '<img src="' + users[i].avatar_url + '" class="img-circle" width="50" height="50">';

				var linkText = '';

				if (!users[i].name) {
					linkText = users[i].html_url.split('/')[3];
				} else {
					linkText = users[i].name;
				}

				html += '<a href="' + users[i].html_url + '">' + linkText + '</a>';
				html += '<span class="badge">Followers: ' + users[i].followers + '</span>';
				html += '<span class="badge">Repos: ' + users[i].repos + '</span>';
				html += '</li>';

				//var html = $('#listTemplate').html();
				//console.log(html);

				$('#resultsList').append(html);
			}
		});
	});
});
