$.ajax({
  url: "http://localhost:5000/api/v1/authcheckadmin",
  method: "GET",
  xhrFields: {
    withCredentials: true,
  },
})
  .done(function (data) {
    if (data.message == "Logged in") {
      $("body").show();
    }
  })
  .fail(function (error) {
    console.log(error.status);
    alert("you must be logged in as admin!");
    window.location.href = "http://localhost:5001/adminsignin";
  });

$.ajax({
  url: "http://localhost:5000/api/v1/pendreservations",
  method: "GET",
  xhrFields: {
    withCredentials: true,
  },
  success: function (reservations) {
    let tbody = $("#reservations-body");
    tbody.empty();

    reservations.forEach(function (res) {
      let ownerName = "N/A";
      if (res.user_info) {
        ownerName = `${res.user_info.FirstName} ${res.user_info.LastName}`;
      }

      let row = `
			<tr>
				<td>${res._id}</td>
				<td>${ownerName}</td>
				<td>${res.reservation_time}</td>
				<td>${res.status}</td>
				<td>${res.party_size}</td>
				<td>
					<button id="checkinbtn" class="btn btn-success btn-sm checkin-btn">Check In</button>
					<button id="updatebtn" class="btn btn-primary btn-sm update-btn">Update</button>
					<button id="deletebtn" class="btn btn-danger btn-sm delete-btn">Delete</button>
					<button id="deletebtn" class="btn btn-default btn-sm delete-btn">Add order</button>
				</td>
			</tr>
		`;
      tbody.append(row);
    });
  },
  error: function (err) {
    console.log("Failed to fetch reservations", err);
  },
});

$(document).on("click", ".checkin-btn", function () {
  const resId = $(this).closest("tr").find("td:first").text();
  if (confirm("Are you sure you want to check in this reservation?")) {
    $.ajax({
      url: `http://localhost:5000/api/v1/upres/${resId}`,
      type: "PUT",
      contentType: "application/json",
      data: JSON.stringify({ status: "checked_in" }),
      success: function (response) {
        alert(response.message);
        location.reload();
      },
      error: function () {
        alert("Failed to check in reservation.");
      },
    });
  }
});

$(document).on("click", ".delete-btn", function () {
  const resId = $(this).closest("tr").find("td:first").text();
  if (confirm("Are you sure you want to check in this reservation?")) {
    $.ajax({
      url: `http://localhost:5000/api/v1/delres/${resId}`,
      type: "DELETE",
      contentType: "application/json",
      success: function (response) {
        alert(response.message);
        location.reload();
      },
      error: function (err) {
        alert(err.responseJSON.error);
        location.reload();
      },
    });
  }
});

let selectedResId = "";

$(document).on("click", ".update-btn", function () {
  const row = $(this).closest("tr");
  selectedResId = row.find("td:first").text();
  const time = row.find("td:nth-child(3)").text();
  const status = row.find("td:nth-child(4)").text();
  const partySize = row.find("td:nth-child(5)").text();
  const table_number = row.find("td:nth-child(6)").text();

  $("#update-res-id").val(selectedResId);
  $("#update-time").val(time);
  $("#update-status").val(status);
  $("#update-party").val(partySize);
  $("#table_number").val(table_number);

  $("#updateModal").modal("show");
});

$("#update-form").submit(function (e) {
  e.preventDefault();

  const updatedData = {
    reservation_time: $("#update-time").val(),
    status: $("#update-status").val(),
    party_size: $("#update-party").val(),
    table_number: $("#table_number").val(),
  };

  $.ajax({
    url: `http://localhost:5000/api/v1/upres/${selectedResId}`,
    type: "PUT",
    contentType: "application/json",
    data: JSON.stringify(updatedData),
    success: function (response) {
      alert(response.message);
      location.reload();
    },
    error: function () {
      alert("Failed to update reservation.");
    },
  });
});

function logout() {
  if (confirm("Are you sure you want to logout?")) {
    $.ajax({
      url: "http://localhost:5000/api/v1/logout",
      type: "GET",
      xhrFields: {
        withCredentials: true,
      },
      success: function (response) {
        alert(response.message);
        window.location.href = "http://localhost:5001/adminsignin";
      },
      error: function (error) {
        console.log(error);
      },
    });
  }
}

function clearOrders() {
  $(".clearOrders").css("display", "none");
  $(".clearReservations").css("display", "block");
}

function clearReservations() {
  $(".clearReservations").css("display", "none");
  $(".clearOrders").css("display", "block");
}

function showAll() {
  $(".clearReservations").css("display", "block");
  $(".clearOrders").css("display", "block");
}
