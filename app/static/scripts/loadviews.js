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
      processViews(res.data);
      $("footer").append(
        '<button id="logout" onclick="logout()">logout</button>'
      );
    },
    error: function () {
      UnprocessViews();
      $("footer").append(
        '<a  href="http://localhost:5001/signin"> <button id="signin_after">sign in</button> <a>'
      );
    },
  });
});

function processViews(data) {
	console.log(data);
	const fullName = `${data.FirstName} ${data.LastName}`;
	const userCard = `
		<div class="user-card">
			<img src="{{ url_for('static', filename='images/user.png') }}" alt="User">
			<h3>${fullName}</h3>
			<p>ID: ${data.id}</p>
			<p>Email: ${data.email}</p>
			<p>Status: ${data.status}</p>
			<p>Legacy Points: ${data.LegacyPoints}</p>
		</div>
	`;
	$('.loadviews').html(userCard);
}

function UnprocessViews() {
    $('.loadviews').html('<a  href="http://localhost:5001/signin"> <button id="signin_after">sign in</button> <a>')
}


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

    },
    error: function (error) {
      console.log(error);
    },
  });
}
$('#profile').click(function (e) {
	e.stopPropagation();
	$('.overlay, .loadviews').show();
});

$('.overlay').click(function () {
	$('.overlay, .loadviews').hide();
});

$('.loadviews').click(function (e) {
	e.stopPropagation();
});

