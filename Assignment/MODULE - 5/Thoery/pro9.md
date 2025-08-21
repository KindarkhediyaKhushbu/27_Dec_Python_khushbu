##### HTTP request methods (GET, POST, PUT, DELETE).

1. GET

Purpose → Retrieve data from the server.

Does not change data (read-only).

Sent in the URL or query string.

📌 Example:

GET /students/1


Response (JSON):

{"id": 1, "name": "Khushbu", "age": 21, "grade": "A"}

🔑 2. POST

Purpose → Create new data on the server.

Data is sent in the request body (JSON, form-data, etc.).

Commonly used for forms, registrations, adding records.

📌 Example:

POST /students/
Content-Type: application/json

{
  "name": "Rahul",
  "age": 22,
  "grade": "B"
}


Response:

{"id": 2, "name": "Rahul", "age": 22, "grade": "B"}

🔑 3. PUT

Purpose → Update an existing record (replace entire object).

Requires sending all fields of the object.

📌 Example:

PUT /students/2
Content-Type: application/json

{
  "name": "Rahul Sharma",
  "age": 23,
  "grade": "A"
}


Response:

{"id": 2, "name": "Rahul Sharma", "age": 23, "grade": "A"}

🔑 4. DELETE

Purpose → Remove an existing record.

Usually just needs the ID in the URL.

📌 Example:

DELETE /students/2


Response:

{"message": "Student deleted successfully"}
