# Week 1 Foundation: Python and REST APIs

## Objective

Build the basic Python and REST API foundation that will later become
the protected resource in the AI Agent Identity and Zero Trust project.

## Python Concepts Covered

- Virtual environments
- Python modules and packages
- Functions
- Classes and data models
- Dictionaries
- Exceptions
- Import statements
- Type hints
- Running Python modules

## REST API Concepts

### HTTP Methods

| Method | Purpose |
|---|---|
| GET | Retrieve information |
| POST | Submit or create information |
| PUT | Replace an existing resource |
| PATCH | Partially update a resource |
| DELETE | Remove a resource |

### HTTP Status Codes

| Status Code | Meaning |
|---|---|
| 200 | Request successful |
| 201 | Resource created |
| 400 | Bad request |
| 401 | Authentication required or failed |
| 403 | Access forbidden |
| 404 | Resource not found |
| 500 | Server-side error |

### HTTP Headers

HTTP headers carry metadata about a request or response.

Examples:

- `Content-Type`
- `Authorization`
- `Accept`
- `User-Agent`

The `Authorization` header will become important in later milestones
when JWT-based identity is implemented.

### JSON

JSON is used to exchange structured data between the client and API.

Example:

```json
{
  "agent_id": "soc-analyst-agent",
  "status": "active"
}