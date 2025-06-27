$('.form').submit(function(e) {
	e.preventDefault();
	$.ajax({
		url: 'http://localhost:5000/api/v1/signup',
		method: 'POST',
		contentType: 'application/json',
		data: JSON.stringify({
			email: $('input[name="email"]').val(),
			password: $('input[name="password"]').val()
		}),
		success: function(res) {
			alert(res.message);
		},
		error: function(err) {
			alert(err.responseJSON.error);
		}
	});
});
