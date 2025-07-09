$.ajax({
  url: "http://localhost:5000/api/v1/authcheckadmin",
  method: "GET",
  xhrFields: {
    withCredentials: true,
  },
})
  .done(function (data) {
    if (data.message == "Logged in") {
      window.location.href = "http://localhost:5001/admin";
    }
  })
  .fail(function (error) {
    console.log(error.status);
  });
$(".form").submit(function (e) {
  e.preventDefault();
  $.ajax({
    url: "http://localhost:5000/api/v1/adminsignin",
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
      window.location.href = "http://localhost:5001/admin";
      alert("Logged in as admin")
    },
    error: function (err) {
      alert(err.responseJSON.error);
    },
  });
});