$(document).ready(function () {
  $.ajax({
    url: "http://localhost:5000/api/v1/authcheck",
    method: "GET",
    xhrFields: {
      withCredentials: true,
    },
    success: function (res) {
      const data = res.data;
      renderReservations(data.id);
      $("#Name").text(`${data.FirstName} ${data.LastName}`);
      $("#userEmail").text(data.email);
      $("#legacyPoints").text(data.LegacyPoints);

      if (data.image_url) {
        $("#profilePic").attr("src", data.image_url);
      }
      editProfileForm;
      $("#editFirstName").val(data.FirstName);
      $("#editLastName").val(data.LastName);
    },
    error: function () {
      alert("You must be logged in to view this page.");
      window.location.href = "/";
    },
  });
});

$("#editProfileForm").submit(function (e) {
  e.preventDefault();

  const payload = {
    FirstName: $("#editFirstName").val(),
    LastName: $("#editLastName").val(),
  };

  $.ajax({
    url: "http://localhost:5000/api/v1/editpfp",
    method: "PUT",
    contentType: "application/json",
    xhrFields: {
      withCredentials: true,
    },
    data: JSON.stringify(payload),
    success: function (res) {
      location.reload();
      alert(res.message);
    },
    error: function (error) {
      alert(error.responseJSON.error);
    },
  });
});

$("#uploadForm").submit(function (e) {
  e.preventDefault();

  const formData = new FormData(this);

  $.ajax({
    url: "http://localhost:5000/api/v1/uploadpfp",
    method: "POST",
    data: formData,
    processData: false,
    contentType: false,
    xhrFields: {
      withCredentials: true,
    },
    success: function (res) {
      alert(res.message);
      $("#profilePic").attr("src", res.url);
      console.log(res.url);
      $("#uploadModal").modal("hide");
    },
    error: function (err) {
      alert(err.responseJSON.error);
    },
  });
});

function renderReservations(user_id) {
  $.ajax({
    url: `http://localhost:5000/api/v1/reservations/${user_id}`,
    type: "GET",
    xhrFields: {
      withCredentials: true,
    },
    success: function (reservations) {
      let list = $("#reservationsList");
      list.empty();

      reservations.forEach(function (res) {
        let item = `
            <li class="list-group-item">
                <strong>ID:</strong> ${res._id}<br>
                <strong>Time:</strong> ${res.reservation_time}<br>
                <strong>Status:</strong> ${res.status}<br>
                <strong>Party Size:</strong> ${res.party_size}<br>
                <strong>Special Request:</strong> ${res.special_request || "N/A"}<br>
                <button class="btn btn-primary btn-sm mt-2 update-res-btn">Update</button>
                <button class="btn btn-danger btn-sm mt-2 delete-btn" data-resid="${res._id}">Delete</button>
                <button class="btn btn-success btn-sm mt-2 update-res-btn">Add order +</button>
            </li>
            `;
        list.append(item);
      });
    },
    error: function () {
      $("#reservationsList").html(
        "<li class='list-group-item text-danger'>Failed to load reservations.</li>"
      );
    },
  });
}

$(document).on("click", ".delete-btn", function () {
  const resId = $(this).data("resid");
  if (confirm("Are you sure you want to delete this reservation?")) {
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
