$.ajax({
  url: "http://localhost:5000/api/v1/authcheckadmin",
  method: "GET",
  xhrFields: {
    withCredentials: true,
  },
})
  .done(function (data) {
    if (data.message == "Logged in") {
    }
  })
  .fail(function (error) {
    console.log(error.status);
    alert("you must be logged in as admin!");
    window.location.href = "http://localhost:5001/adminsignin";
  });