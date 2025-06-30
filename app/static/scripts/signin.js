$.ajax(
	{
		url: "http://localhost:5000/api/v1/authcheck",
		method: "GET",
		xhrFields: {
			withCredentials: true
		}
	})
  .done(function (data) {
    if (data.message == "Logged in") {
      window.location.href = "http://localhost:5001/";
    }
  })
  .fail(function (error) {
    console.log(error.status);
  });
$(".form").submit(function (e) {
  e.preventDefault();
  $.ajax({
    url: "http://localhost:5000/api/v1/signin",
    method: "POST",
    contentType: "application/json",
    data: JSON.stringify({
      email: $('input[name="email"]').val(),
      password: $('input[name="password"]').val(),
    }),
    xhrFields: {
      withCredentials: true,
    },
    success: function (res) {
      alert(res.message), (window.location.href = "http://localhost:5001/");
    },
    error: function (err) {
      alert(err.responseJSON.error);
    },
  });
});
if (document.cookie.includes("access_token")) {
  window.location.href = "http://localhost:5001/";
}
