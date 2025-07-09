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
    alert("you must be logged in as admin!")
    window.location.href = "http://localhost:5001/adminsignin";
  });

$.ajax({
	url: "http://localhost:5000/api/v1/pendreservations",
	method: "GET",
	xhrFields: {
		withCredentials: true
	},
	success: function (reservations) {
		let tbody = $("#reservations-body");
		tbody.empty();

		reservations.forEach(function (res) {
			let row = `
				<tr>
					<td>${res._id}</td>
					<td>${res.owner_id || "N/A"}</td>
					<td>${res.reservation_time}</td>
					<td>${res.status}</td>
					<td>${res.party_size}</td>
					<td>
                    <button id="checkinbtn" class="btn btn-success btn-sm checkin-btn">Check In</button>
                    <button id="updatebtn" class="btn btn-primary btn-sm update-btn">Update</button>
                    <button id="deletebtn" class="btn btn-danger btn-sm delete-btn">Delete</button>
                    </td>
				</tr>
			`;
			tbody.append(row);
		});
	},
	error: function (err) {
		console.log("Failed to fetch reservations", err);
	}
});

$(document).on('click', '.checkin-btn', function () {
  const resId = $(this).closest('tr').find('td:first').text();
  if (confirm('Are you sure you want to check in this reservation?')) {
    $.ajax({
      url: `http://localhost:5000/api/v1/upres/${resId}`,
      type: 'PUT',
      contentType: 'application/json',
      data: JSON.stringify({ status: 'checked_in' }),
      success: function (response) {
        alert(response.message);
        location.reload();
      },
      error: function () {
        alert('Failed to check in reservation.');
      },
    });
  }
});

$("#updatebtn").click(function() {
    // when this button is clicked, a floating window to enter all the data to update, i don't know how you'll do that
    // api endpoint is the same
})
$("#deletebtn").click(function() {
    // ('/delres/<res_id>', methods=['DELETE'],
})
