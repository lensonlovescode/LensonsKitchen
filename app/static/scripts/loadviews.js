$(document).ready(function () {
  $("#burger").click(function () {
    $("nav").toggleClass("show");
  });
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
    },
    error: function () {
      $("footer").append(
        '<a  href="http://localhost:5001/signin"> <button id="signin_after">sign in</button> <a>'
      );
      $("#profilePic").attr("onclick", "takemesignin()");
    },
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
      $('.loadviews').html('<a href="http://localhost:5001/signin"> <button id="signin_after">sign in</button> <a>')
      $("#profilePic").attr("src", "");
      $("#profilePic").attr("onclick", "takemesignin()");
    },
    error: function (error) {
      console.log(error);
    },
  });
}


function takemepfp() {
    window.location = "/profile"
}

function takemesignin() {
    window.location = "/signin"
}

