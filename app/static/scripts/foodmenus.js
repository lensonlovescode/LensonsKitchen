$(document).ready(function () {
	$.ajax({
		url: "http://localhost:5000/api/v1/fooditems",
		type: "GET",
		success: function (foodItems) {
			let foodList = $("#foodItems");
			foodList.empty();
			foodItems.forEach(function (item) {
				let card = `
					<div class="col-md-4 mb-4">
						<div class="card text-center bg-dark text-white border-light">
							<img src="${item.image_url}" class="card-img-top" alt="${item.name}">
							<div class="card-body">
								<h5 class="card-title">${item.name}</h5>
								<p class="card-text">${item.description}</p>
								<button class="btn btn-warning add-to-order-btn" data-id="${item._id}">Add to Order</button>
							</div>
						</div>
					</div>
				`;
				foodList.append(card);
			});
		},
		error: function () {
			alert("Failed to load food items.");
		},
	});

	let selectedFoodId = "";

	$(document).on("click", ".add-to-order-btn", function () {
		selectedFoodId = $(this).data("id");
		$("#reservationSelect").empty().append('<option>Loading...</option>');

		$.ajax({
			url: "http://localhost:5000/api/v1/myreservations",
			type: "GET",
			xhrFields: { withCredentials: true },
			success: function (reservations) {
				let select = $("#reservationSelect");
				select.empty();
				select.append('<option value="">Select Reservation or Pickup</option>');
				reservations.forEach(function (res) {
					select.append(`<option value="${res._id}">Reservation at ${res.reservation_time}</option>`);
				});
				select.append('<option value="pickup">Pickup Order</option>');
			},
			error: function () {
				alert("Failed to load reservations.");
			},
		});

		$("#addOrderModal").modal("show");
	});

	// Handle Confirm Add button
	$("#addOrderModal button.btn-warning").click(function () {
		const reservationId = $("#reservationSelect").val();
		if (!reservationId) {
			alert("Please select a reservation or pickup option.");
			return;
		}

		$.ajax({
			url: "http://localhost:5000/api/v1/addorder",
			type: "POST",
			contentType: "application/json",
			data: JSON.stringify({
				food_id: selectedFoodId,
				reservation_id: reservationId,
			}),
			success: function (res) {
				alert(res.message);
				$("#addOrderModal").modal("hide");
			},
			error: function () {
				alert("Failed to add order.");
			},
		});
	});
});

