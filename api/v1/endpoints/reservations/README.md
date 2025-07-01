### 📁 `/api/v1/endpoints/reservations`

This module provides RESTful API endpoints for managing table reservations.

---

### 📌 Endpoints Overview

#### `POST /reserve`

* **Description**: Create a new reservation.
* **Body JSON**:

  ```json
  {
    "owner": "<user_id>",
    "reservation_time": "<ISO 8601 timestamp>",
    "party_size": <number>,
    "special_request": "<optional note>",
    "contact": "<phone number>"
  }
  ```
* **Success Response**:
  `200 OK`

  ```json
  {
    "message": "Reservation created successfully",
    "table_number": <int>,
    "res_id": "<reservation_id>"
  }
  ```
* **Failure Responses**:

  * `400` for missing fields
  * `500` for server errors
  * `200` with error message if no tables are available

---

#### `DELETE /delres/<res_id>`

* **Description**: Delete a reservation by its ID.
* **Success**: `200 OK` with message
* **If not found**: `404 Not Found`

---

#### `PUT /upres/<res_id>`

* **Description**: Update an existing reservation.
* **Body JSON** must include `owner_id` and any fields to update:

  ```json
  {
    "owner_id": "<user_id>",
    "status": "<pending|confirmed|checked_in|cancelled|no_show>",
    "reservation_time": "<timestamp>",
    "party_size": <int>,
    "special_request": "<string>",
    "table_number": <int>,
    "has_order": <bool>,
    "order_id": "<string>"
  }
  ```
* **Success**: `200 OK`
* **If not found or not owned**: `404 Not Found`

---

#### `GET /reservation/<res_id>`

* **Description**: Get a specific reservation by ID.
* **Success**: `200 OK` with reservation object

---

#### `GET /reservations/<user_id>`

* **Description**: Get all reservations for a given user.
* **Success**: `200 OK` with a list of reservations
* **If none found**: `404 Not Found`

