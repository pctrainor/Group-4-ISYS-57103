# How to Use the Drone Flight Operations API

This API provides access to data about drones, flight plans, pilots, and routes.

## Getting Started

The API is defined using an OpenAPI specification (YAML file). You can use this file with tools like Swagger UI or Redoc to generate interactive documentation and explore the API endpoints.

## For a full list of queries, follow this link:

https://pctrainor.github.io/Group-4-ISYS-57103/

## Running the API

This document assumes you have a running API server that conforms to the provided OpenAPI specification. You'll need to replace `http://localhost:5000` in the server URL with the actual address of your API server.

## Using the API

You can interact with the API using any HTTP client (e.g., curl, Postman, or a web browser).

Here's an example of how to retrieve a list of all drones using the `/drones` endpoint:

- **`/drones` (GET):** Retrieve a list of all drones.
  - **Example Request:** `curl [http://localhost:5000/api/drones](http://localhost:5000/api/drones)`
  - **Example Response:**

```json
[
  {
    "BUNO_ID": "DR-001",
    "Drone_Model": "DJI Phantom 4 Pro",
    "Manufacturer": "DJI Innovations",
    "Purchase_Date": "2022-05-20",
    "Serial": "23456",
    "Status": "Active",
    "Status_Code": "OK"
  },
  {
    "BUNO_ID": "DR-002",
    "Drone_Model": "DJI Mavic 3",
    "Manufacturer": "DJI Innovations",
    "Purchase_Date": "2023-08-15",
    "Serial": "12345",
    "Status": "Maintenance",
    "Status_Code": "MAINT"
  }
]
```
