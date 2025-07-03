$(document).ready(function () {
  $.ajax({
    url: "http://localhost:5000/api/v1/authcheck",
    type: "GET",
    xhrFields: {
      withCredentials: true
    },
    success: function (res) {
      processViews(res.data)
      $("footer").append('<button id="logout" onclick="logout()">logout</button>')
    },
    error: function () {
      $("footer").append('<a  href="http://localhost:5001/signin"> <button >sign in</button> <a>')
    }
  }) 
})

function processViews (data) {
    console.log(data) 
}