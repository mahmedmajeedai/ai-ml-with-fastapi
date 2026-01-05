# 📌 Path Parameters in FastAPI

## What is a Path Parameter?

A **path parameter** is a variable part of the URL path used to uniquely identify a resource.  
Path parameters are **always required** in FastAPI.

### Example URL

/users/5
Here, `5` is a path parameter.

# 📌 HTTP Status Codes — Quick Revision Notes

## 🔹 What are HTTP Status Codes?

- HTTP status codes are **numbers returned by the server** after a request.
- They tell the **client (browser/app)**:
  - Whether the request was successful
  - Whether something went wrong
  - Who caused the issue (client or server)

---

## 🔹 Client–Server Flow

1. **Client** sends an HTTP request
2. **Server** processes the request
3. **Server** sends back:
   - Response data
   - **HTTP status code**

---

## 🔢 Status Code Categories (Very Important)

### ✅ **2xx — Success**

- Request was received and processed successfully.

**Common codes:**

- **200 OK** → Request successful
- **201 Created** → Resource created (after POST)
- **204 No Content** → Success, but no data returned (often DELETE)

👉 Meaning: _Everything worked fine_

---

### 🔁 **3xx — Redirection**

- Client must take further action.

**Common codes:**

- **301 Moved Permanently**
- **302 Found**

👉 Meaning: _Resource moved or redirect required_

---

### ❌ **4xx — Client Error**

- Problem is **on the client side**.

**Common codes:**

- **400 Bad Request** → Invalid request
- **401 Unauthorized** → Authentication required
- **403 Forbidden** → Access denied
- **404 Not Found** → Resource not found

👉 Meaning: _Client did something wrong_

---

### 💥 **5xx — Server Error**

- Problem is **on the server side**.

**Common codes:**

- **500 Internal Server Error**
- **502 Bad Gateway**
- **503 Service Unavailable**

👉 Meaning: _Server failed to process a valid request_

---

## 🧠 Easy Way to Remember

| Code Range | Meaning      | Who is wrong? |
| ---------- | ------------ | ------------- |
| 2xx        | Success      | Nobody        |
| 3xx        | Redirect     | Depends       |
| 4xx        | Client Error | Client        |
| 5xx        | Server Error | Server        |

---

## 🔑 Most Common Status Codes (Must Remember)

- **200** → OK
- **201** → Created
- **400** → Bad Request
- **401** → Unauthorized
- **403** → Forbidden
- **404** → Not Found
- **500** → Internal Server Error

---

## 🧪 Real-World Examples

- API returns **200** → Data fetched successfully
- API returns **404** → Wrong URL or missing resource
- API returns **500** → Backend crashed or bug

---

## 📝 One-Line Definition (Interview Ready)

> HTTP status codes are standardized response codes sent by a server to indicate the result of a client’s request.

4xx = Client mistake  
5xx = Server mistake\*\*

# 📌 Query Parameters (HTTP & FastAPI)

## What is a Query Parameter?

- Query parameters are **optional key–value pairs** appended to the **end of a URL**.
- They are used to pass **additional data** to the server in an HTTP request.
- Query parameters **do not change the endpoint path**.

They are commonly used for:

- Filtering
- Sorting
- Searching
- Pagination

---

## Example URL

/patients?city=Delhi&sort_by=age

---

## How Query Parameters Work

- `?` marks the **start of query parameters**
- Each parameter is written as a **key=value** pair
- Multiple parameters are separated using `&`

---

## Breakdown of Example

/patients?city=Delhi&sort_by=age

- `city=Delhi` → query parameter used for **filtering**
- `sort_by=age` → query parameter used for **sorting**

---

## Key Characteristics of Query Parameters

- Optional (not required by default)
- Appear **after `?`** in the URL
- Do not affect route matching
- Used for **refining results**, not identifying resources

---

## Query Parameters vs Path Parameters

| Feature  | Query Parameter        | Path Parameter    |
| -------- | ---------------------- | ----------------- |
| Position | After `?`              | Inside URL path   |
| Required | Optional               | Always required   |
| Purpose  | Filter / sort / search | Identify resource |
| Example  | `?page=2`              | `/users/5`        |

---

## Query Parameters in FastAPI

### What is `Query()`?

- `Query()` is a utility function provided by **FastAPI**
- It is used to:
  - Declare query parameters
  - Validate input
  - Add documentation metadata

Import:

```python
from fastapi import Query

Query parameters are optional key–value pairs appended to a URL to pass additional filtering, sorting, or search information to the server.
```
