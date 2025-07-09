$(document).ready(function () {
  $.ajax({
    url: "http://localhost:5000/api/v1/authcheck",
    type: "GET",
    xhrFields: {
      withCredentials: true,
    },
    success: function (res) {
      const data = res.data;
      $("footer").append(
        '<button id="logout" onclick="logout()">logout</button>'
      );
      if (data.image_url) {
        $("#profilePic").attr("src", data.image_url);
      }
      $("footer").append(
        '<button id="logout" onclick="logout()">logout</button>'
      );
    },
    error: function () {
      $("footer").append(
        '<a  href="http://localhost:5001/signin"> <button >sign in</button> <a>'
      );
    },
  });

  const form = $("#reservation-form");

  form.on("submit", function (e) {
    e.preventDefault();

    const payload = {
      reservation_time: form.find("[name='reservation_time']").val(),
      party_size: parseInt(form.find("[name='party_size']").val()),
      special_request: form.find("[name='special_request']").val(),
      contact: form.find("[name='contact']").val(),
    };

    $.ajax({
      url: "http://localhost:5000/api/v1/reserve",
      type: "POST",
      contentType: "application/json",
      xhrFields: {
        withCredentials: true,
      },
      data: JSON.stringify(payload),
      success: function (response) {
        console.log(response);
        alert(response.message || response.error);
        form[0].reset();
      },
      error: function (err) {
        alert(err.responseJSON.Error);
      },
    });
  });

  $("#view-reservations-btn").on("click", function () {
    window.location.href = "/my-reservations";
  });
});

function logout() {
  $.ajax({
    url: "http://localhost:5000/api/v1/logout",
    type: "GET",
    xhrFields: {
      withCredentials: true,
    },
    success: function (response) {
      alert(response.message);
      $("#logout").remove();
      $("footer").append(
        '<a href="http://localhost:5001/signin"> <button id="signin_after">sign in</button> <a>'
      );
    },
    error: function (error) {
      console.log(error);
    },
  });
}

function takemepfp() {
  window.location = "/profile";
}
