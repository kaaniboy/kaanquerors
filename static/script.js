$(document).ready(function () {
	console.log('Test!');
	
	$('#btn').click(function () {
		var school = $('#search').val() || 'Arizona State University';
		console.log('School: ' + encodeURIComponent(school));
		
		$('#resultsList').html('');
		
		$.getJSON('/get_profiles?school=' + school, function (data) {
			var users = data.users;
			
			$('#resultsList').html(users);
			
			console.log(users);
			
			for (var i = 0; i < users.length; i++) {
				console.log(users[i].name);
				
				var email = users[i].email || '';
				
				var html = '<li class="list-group-item">';
				html += '<img src="' + users[i].avatar_url + '" class="img-circle" width="50" height="50">';
				html += '<a href="mailto:' + email + '">' + users[i].name + '</a>';
				html += '<span class="badge">Followers: ' + users[i].followers + '</span>';
				html += '<span class="badge">Repos: ' + users[i].repos + '</span>';
				// html += '<span class="badge"><a href="#">AYLMAO</a></span>';
				html += '</li>';
				
				//var html = $('#listTemplate').html();
				//console.log(html);
				
				$('#resultsList').append(html);
			}
		});
	});
});