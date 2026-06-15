# CodeCraftHub API - Comprehensive Test Cases

This document provides ready-to-use test cases for all CodeCraftHub API endpoints. Simply copy and paste the curl commands into your terminal.

## Prerequisites

- Make sure the Flask API is running: `python app.py`
- The API should be accessible at `http://localhost:5000`
- Open a new terminal window for running these tests

---

## Table of Contents

1. [Health Check Endpoint](#1-health-check-endpoint)
2. [Create Course (POST)](#2-create-course-post)
3. [Get All Courses (GET)](#3-get-all-courses-get)
4. [Get Specific Course (GET)](#4-get-specific-course-get)
5. [Update Course (PUT)](#5-update-course-put)
6. [Delete Course (DELETE)](#6-delete-course-delete)
7. [Get Statistics (GET)](#7-get-statistics-get)
8. [Search Courses (GET)](#8-search-courses-get)
9. [Error Scenarios](#9-error-scenarios)

---

## 1. Health Check Endpoint

### Test 1.1: Check API is Running

**Request:**
```bash
curl http://localhost:5000/
```

**Expected Response:**
```json
{
    "success": true,
    "message": "CodeCraftHub API is running!",
    "version": "1.0.0"
}
```

**Expected Status Code:** `200 OK`

---

## 2. Create Course (POST)

### Test 2.1: Create Course - Success (Python Course)

**Request:**
```bash
curl -X POST http://localhost:5000/api/courses \
  -H "Content-Type: application/json" \
  -d "{\"name\":\"Advanced Python\",\"description\":\"Master decorators, generators, and metaclasses\",\"target_date\":\"2026-09-30\",\"status\":\"Not Started\"}"
```

**Expected Response:**
```json
{
    "success": true,
    "message": "Course created successfully",
    "data": {
        "id": 4,
        "name": "Advanced Python",
        "description": "Master decorators, generators, and metaclasses",
        "target_date": "2026-09-30",
        "status": "Not Started",
        "created_at": "2026-06-15 21:56:00"
    }
}
```

**Expected Status Code:** `201 Created`

---

### Test 2.2: Create Course - Success (Web Development)

**Request:**
```bash
curl -X POST http://localhost:5000/api/courses \
  -H "Content-Type: application/json" \
  -d "{\"name\":\"Node.js Fundamentals\",\"description\":\"Build backend APIs with Node.js and Express\",\"target_date\":\"2026-10-15\",\"status\":\"Not Started\"}"
```

**Expected Status Code:** `201 Created`

---

### Test 2.3: Create Course - Success (Database)

**Request:**
```bash
curl -X POST http://localhost:5000/api/courses \
  -H "Content-Type: application/json" \
  -d "{\"name\":\"PostgreSQL Mastery\",\"description\":\"Learn advanced SQL queries and database optimization\",\"target_date\":\"2026-11-20\",\"status\":\"In Progress\"}"
```

**Expected Status Code:** `201 Created`

---

### Test 2.4: Create Course - Error (Missing Required Field)

**Request:**
```bash
curl -X POST http://localhost:5000/api/courses \
  -H "Content-Type: application/json" \
  -d "{\"name\":\"Incomplete Course\",\"description\":\"Missing status and target_date\"}"
```

**Expected Response:**
```json
{
    "success": false,
    "message": "Missing required field: target_date"
}
```

**Expected Status Code:** `400 Bad Request`

---

### Test 2.5: Create Course - Error (Empty Name)

**Request:**
```bash
curl -X POST http://localhost:5000/api/courses \
  -H "Content-Type: application/json" \
  -d "{\"name\":\"\",\"description\":\"Course with empty name\",\"target_date\":\"2026-12-31\",\"status\":\"Not Started\"}"
```

**Expected Response:**
```json
{
    "success": false,
    "message": "Missing required field: name"
}
```

**Expected Status Code:** `400 Bad Request`

---

### Test 2.6: Create Course - Error (Invalid Status)

**Request:**
```bash
curl -X POST http://localhost:5000/api/courses \
  -H "Content-Type: application/json" \
  -d "{\"name\":\"Test Course\",\"description\":\"Testing invalid status\",\"target_date\":\"2026-12-31\",\"status\":\"Pending\"}"
```

**Expected Response:**
```json
{
    "success": false,
    "message": "Invalid status. Allowed values: Not Started, In Progress, Completed"
}
```

**Expected Status Code:** `400 Bad Request`

---

### Test 2.7: Create Course - Error (No JSON Data)

**Request:**
```bash
curl -X POST http://localhost:5000/api/courses \
  -H "Content-Type: application/json"
```

**Expected Response:**
```json
{
    "success": false,
    "message": "No data provided"
}
```

**Expected Status Code:** `400 Bad Request`

---

### Test 2.8: Create Course - Error (Malformed JSON)

**Request:**
```bash
curl -X POST http://localhost:5000/api/courses \
  -H "Content-Type: application/json" \
  -d "{\"name\":\"Test\",\"description:\"Missing quote\"}"
```

**Expected Response:**
```json
{
    "success": false,
    "message": "No data provided"
}
```

**Expected Status Code:** `400 Bad Request`

---

## 3. Get All Courses (GET)

### Test 3.1: Get All Courses - Success

**Request:**
```bash
curl http://localhost:5000/api/courses
```

**Expected Response:**
```json
{
    "success": true,
    "message": "Courses retrieved successfully",
    "data": [
        {
            "id": 1,
            "name": "Python Basics",
            "description": "Learn Python fundamentals including variables, data types, control structures, and functions",
            "target_date": "2025-12-31",
            "status": "In Progress",
            "created_at": "2025-11-04 10:30:00"
        },
        {
            "id": 2,
            "name": "Flask Web Development",
            "description": "Master Flask framework to build REST APIs and web applications",
            "target_date": "2026-01-15",
            "status": "Not Started",
            "created_at": "2025-11-04 11:00:00"
        }
    ]
}
```

**Expected Status Code:** `200 OK`

---

### Test 3.2: Get All Courses - Pretty Print (Formatted Output)

**Request:**
```bash
curl http://localhost:5000/api/courses | python -m json.tool
```

**Note:** This formats the JSON output for easier reading in the terminal.

**Expected Status Code:** `200 OK`

---

## 4. Get Specific Course (GET)

### Test 4.1: Get Course by ID - Success (ID 1)

**Request:**
```bash
curl http://localhost:5000/api/courses/1
```

**Expected Response:**
```json
{
    "success": true,
    "message": "Course retrieved successfully",
    "data": {
        "id": 1,
        "name": "Python Basics",
        "description": "Learn Python fundamentals including variables, data types, control structures, and functions",
        "target_date": "2025-12-31",
        "status": "In Progress",
        "created_at": "2025-11-04 10:30:00"
    }
}
```

**Expected Status Code:** `200 OK`

---

### Test 4.2: Get Course by ID - Success (ID 2)

**Request:**
```bash
curl http://localhost:5000/api/courses/2
```

**Expected Status Code:** `200 OK`

---

### Test 4.3: Get Course by ID - Error (Course Not Found)

**Request:**
```bash
curl http://localhost:5000/api/courses/999
```

**Expected Response:**
```json
{
    "success": false,
    "message": "Course not found"
}
```

**Expected Status Code:** `404 Not Found`

---

### Test 4.4: Get Course by ID - Error (Invalid ID Format)

**Request:**
```bash
curl http://localhost:5000/api/courses/abc
```

**Expected Response:**
```html
<!doctype html>
<html>
<!-- 404 Page Not Found -->
```

**Expected Status Code:** `404 Not Found`

**Note:** Flask returns HTML 404 for invalid route patterns.

---

## 5. Update Course (PUT)

### Test 5.1: Update Course Status - Success

**Request:**
```bash
curl -X PUT http://localhost:5000/api/courses/1 \
  -H "Content-Type: application/json" \
  -d "{\"status\":\"Completed\"}"
```

**Expected Response:**
```json
{
    "success": true,
    "message": "Course updated successfully",
    "data": {
        "id": 1,
        "name": "Python Basics",
        "description": "Learn Python fundamentals including variables, data types, control structures, and functions",
        "target_date": "2025-12-31",
        "status": "Completed",
        "created_at": "2025-11-04 10:30:00"
    }
}
```

**Expected Status Code:** `200 OK`

---

### Test 5.2: Update Multiple Fields - Success

**Request:**
```bash
curl -X PUT http://localhost:5000/api/courses/2 \
  -H "Content-Type: application/json" \
  -d "{\"status\":\"In Progress\",\"target_date\":\"2026-02-28\"}"
```

**Expected Response:**
```json
{
    "success": true,
    "message": "Course updated successfully",
    "data": {
        "id": 2,
        "name": "Flask Web Development",
        "description": "Master Flask framework to build REST APIs and web applications",
        "target_date": "2026-02-28",
        "status": "In Progress",
        "created_at": "2025-11-04 11:00:00"
    }
}
```

**Expected Status Code:** `200 OK`

---

### Test 5.3: Update All Fields - Success

**Request:**
```bash
curl -X PUT http://localhost:5000/api/courses/3 \
  -H "Content-Type: application/json" \
  -d "{\"name\":\"JavaScript ES6+ Advanced\",\"description\":\"Deep dive into modern JavaScript features and patterns\",\"target_date\":\"2026-03-31\",\"status\":\"In Progress\"}"
```

**Expected Status Code:** `200 OK`

---

### Test 5.4: Update Course - Error (Course Not Found)

**Request:**
```bash
curl -X PUT http://localhost:5000/api/courses/999 \
  -H "Content-Type: application/json" \
  -d "{\"status\":\"Completed\"}"
```

**Expected Response:**
```json
{
    "success": false,
    "message": "Course not found"
}
```

**Expected Status Code:** `404 Not Found`

---

### Test 5.5: Update Course - Error (Invalid Status)

**Request:**
```bash
curl -X PUT http://localhost:5000/api/courses/1 \
  -H "Content-Type: application/json" \
  -d "{\"status\":\"Almost Done\"}"
```

**Expected Response:**
```json
{
    "success": false,
    "message": "Invalid status. Allowed values: Not Started, In Progress, Completed"
}
```

**Expected Status Code:** `400 Bad Request`

---

### Test 5.6: Update Course - Error (No Data Provided)

**Request:**
```bash
curl -X PUT http://localhost:5000/api/courses/1 \
  -H "Content-Type: application/json"
```

**Expected Response:**
```json
{
    "success": false,
    "message": "No data provided"
}
```

**Expected Status Code:** `400 Bad Request`

---

## 6. Delete Course (DELETE)

### Test 6.1: Delete Course - Success

**Request:**
```bash
curl -X DELETE http://localhost:5000/api/courses/3
```

**Expected Response:**
```json
{
    "success": true,
    "message": "Course deleted successfully",
    "data": {
        "id": 3,
        "name": "JavaScript ES6+",
        "description": "Modern JavaScript features including arrow functions, promises, async/await, and modules",
        "target_date": "2025-11-30",
        "status": "Completed",
        "created_at": "2025-11-04 11:15:00"
    }
}
```

**Expected Status Code:** `200 OK`

---

### Test 6.2: Delete Course - Error (Course Not Found)

**Request:**
```bash
curl -X DELETE http://localhost:5000/api/courses/999
```

**Expected Response:**
```json
{
    "success": false,
    "message": "Course not found"
}
```

**Expected Status Code:** `404 Not Found`

---

### Test 6.3: Delete Course - Error (Already Deleted)

**Request:**
```bash
curl -X DELETE http://localhost:5000/api/courses/3
```

**Expected Response:**
```json
{
    "success": false,
    "message": "Course not found"
}
```

**Expected Status Code:** `404 Not Found`

**Note:** This assumes you already deleted course ID 3 in Test 6.1.

---

## 7. Get Statistics (GET)

### Test 7.1: Get Course Statistics - Success

**Request:**
```bash
curl http://localhost:5000/api/courses/stats
```

**Expected Response:**
```json
{
    "success": true,
    "message": "Statistics retrieved successfully",
    "data": {
        "total_courses": 3,
        "not_started": 1,
        "in_progress": 1,
        "completed": 1
    }
}
```

**Expected Status Code:** `200 OK`

**Note:** The actual numbers will depend on your current data.

---

### Test 7.2: Get Statistics - With Pretty Print

**Request:**
```bash
curl http://localhost:5000/api/courses/stats | python -m json.tool
```

**Expected Status Code:** `200 OK`

---

## 8. Search Courses (GET)

### Test 8.1: Search Courses - Success (Found Results)

**Request:**
```bash
curl "http://localhost:5000/api/courses/search?q=python"
```

**Expected Response:**
```json
{
    "success": true,
    "message": "Found 1 course(s)",
    "data": [
        {
            "id": 1,
            "name": "Python Basics",
            "description": "Learn Python fundamentals including variables, data types, control structures, and functions",
            "target_date": "2025-12-31",
            "status": "In Progress",
            "created_at": "2025-11-04 10:30:00"
        }
    ]
}
```

**Expected Status Code:** `200 OK`

---

### Test 8.2: Search Courses - Success (Multiple Results)

**Request:**
```bash
curl "http://localhost:5000/api/courses/search?q=learn"
```

**Expected Status Code:** `200 OK`

**Note:** Returns all courses where "learn" appears in name or description.

---

### Test 8.3: Search Courses - Success (No Results Found)

**Request:**
```bash
curl "http://localhost:5000/api/courses/search?q=blockchain"
```

**Expected Response:**
```json
{
    "success": true,
    "message": "Found 0 course(s)",
    "data": []
}
```

**Expected Status Code:** `200 OK`

---

### Test 8.4: Search Courses - Case Insensitive

**Request:**
```bash
curl "http://localhost:5000/api/courses/search?q=PYTHON"
```

**Expected Response:**
```json
{
    "success": true,
    "message": "Found 1 course(s)",
    "data": [
        {
            "id": 1,
            "name": "Python Basics",
            "description": "Learn Python fundamentals including variables, data types, control structures, and functions",
            "target_date": "2025-12-31",
            "status": "In Progress",
            "created_at": "2025-11-04 10:30:00"
        }
    ]
}
```

**Expected Status Code:** `200 OK`

---

### Test 8.5: Search Courses - Error (Missing Query Parameter)

**Request:**
```bash
curl "http://localhost:5000/api/courses/search"
```

**Expected Response:**
```json
{
    "success": false,
    "message": "Search query parameter \"q\" is required"
}
```

**Expected Status Code:** `400 Bad Request`

---

### Test 8.6: Search Courses - Empty Query Parameter

**Request:**
```bash
curl "http://localhost:5000/api/courses/search?q="
```

**Expected Response:**
```json
{
    "success": false,
    "message": "Search query parameter \"q\" is required"
}
```

**Expected Status Code:** `400 Bad Request`

---

## 9. Error Scenarios

### Test 9.1: Invalid HTTP Method

**Request:**
```bash
curl -X PATCH http://localhost:5000/api/courses/1
```

**Expected Status Code:** `405 Method Not Allowed`

---

### Test 9.2: Invalid Endpoint

**Request:**
```bash
curl http://localhost:5000/api/invalid-endpoint
```

**Expected Status Code:** `404 Not Found`

---

### Test 9.3: Missing Content-Type Header (POST)

**Request:**
```bash
curl -X POST http://localhost:5000/api/courses \
  -d "{\"name\":\"Test\",\"description\":\"Test\",\"target_date\":\"2026-12-31\",\"status\":\"Not Started\"}"
```

**Expected Response:**
```json
{
    "success": false,
    "message": "No data provided"
}
```

**Expected Status Code:** `400 Bad Request`

**Note:** Without Content-Type header, Flask may not parse the JSON properly.

---

## 10. Complete Test Workflow

Here's a complete workflow to test all functionality in sequence:

```bash
# Step 1: Check API is running
curl http://localhost:5000/

# Step 2: Get all existing courses
curl http://localhost:5000/api/courses

# Step 3: Get statistics
curl http://localhost:5000/api/courses/stats

# Step 4: Create a new course
curl -X POST http://localhost:5000/api/courses \
  -H "Content-Type: application/json" \
  -d "{\"name\":\"Docker Fundamentals\",\"description\":\"Learn containerization with Docker\",\"target_date\":\"2026-07-31\",\"status\":\"Not Started\"}"

# Step 5: Get the newly created course (use the ID from Step 4 response)
curl http://localhost:5000/api/courses/4

# Step 6: Update the course status
curl -X PUT http://localhost:5000/api/courses/4 \
  -H "Content-Type: application/json" \
  -d "{\"status\":\"In Progress\"}"

# Step 7: Search for the course
curl "http://localhost:5000/api/courses/search?q=docker"

# Step 8: Get updated statistics
curl http://localhost:5000/api/courses/stats

# Step 9: Delete the course
curl -X DELETE http://localhost:5000/api/courses/4

# Step 10: Verify deletion (should return 404)
curl http://localhost:5000/api/courses/4

# Step 11: Get final statistics
curl http://localhost:5000/api/courses/stats
```

---

## 11. Testing with Variables (Advanced)

For easier testing, you can use shell variables:

```bash
# Set base URL
BASE_URL="http://localhost:5000"

# Test health check
curl $BASE_URL/

# Create course and capture response
RESPONSE=$(curl -s -X POST $BASE_URL/api/courses \
  -H "Content-Type: application/json" \
  -d "{\"name\":\"Test Course\",\"description\":\"Testing\",\"target_date\":\"2026-12-31\",\"status\":\"Not Started\"}")

# Display response
echo $RESPONSE

# Extract ID (requires jq - JSON processor)
COURSE_ID=$(echo $RESPONSE | jq -r '.data.id')

# Use the ID
curl $BASE_URL/api/courses/$COURSE_ID
```

---

## 12. PowerShell Commands (Windows Users)

If you're using PowerShell instead of bash, use these commands:

### Get All Courses:
```powershell
Invoke-RestMethod -Uri "http://localhost:5000/api/courses" -Method Get
```

### Create Course:
```powershell
$body = @{
    name = "Docker Fundamentals"
    description = "Learn containerization"
    target_date = "2026-07-31"
    status = "Not Started"
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:5000/api/courses" -Method Post -Body $body -ContentType "application/json"
```

### Update Course:
```powershell
$body = @{
    status = "Completed"
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:5000/api/courses/1" -Method Put -Body $body -ContentType "application/json"
```

### Delete Course:
```powershell
Invoke-RestMethod -Uri "http://localhost:5000/api/courses/1" -Method Delete
```

---

## 13. Tips for Testing

1. **Check Status Codes**: Add `-i` flag to curl to see HTTP headers:
   ```bash
   curl -i http://localhost:5000/api/courses
   ```

2. **Pretty Print JSON**: Pipe output through `python -m json.tool`:
   ```bash
   curl http://localhost:5000/api/courses | python -m json.tool
   ```

3. **Save Response to File**: Use `-o` flag:
   ```bash
   curl http://localhost:5000/api/courses -o response.json
   ```

4. **Verbose Output**: Use `-v` flag for debugging:
   ```bash
   curl -v http://localhost:5000/api/courses
   ```

5. **Silent Mode**: Use `-s` flag to suppress progress bar:
   ```bash
   curl -s http://localhost:5000/api/courses
   ```

---

## 14. Expected Error Messages Summary

| Scenario | Status Code | Error Message |
|----------|-------------|---------------|
| Missing required field | 400 | "Missing required field: [field_name]" |
| Invalid status | 400 | "Invalid status. Allowed values: Not Started, In Progress, Completed" |
| No data provided | 400 | "No data provided" |
| Course not found | 404 | "Course not found" |
| Missing query parameter | 400 | "Search query parameter \"q\" is required" |
| Internal error | 500 | "Internal server error: [error details]" |

---

## 15. Automated Test Script

Save this as `test_api.sh` (Unix/Linux/Mac) or `test_api.ps1` (Windows):

### Bash Script (`test_api.sh`):
```bash
#!/bin/bash

BASE_URL="http://localhost:5000"

echo "Testing CodeCraftHub API..."
echo "============================"

echo -e "\n1. Health Check"
curl -s $BASE_URL/ | python -m json.tool

echo -e "\n2. Get All Courses"
curl -s $BASE_URL/api/courses | python -m json.tool

echo -e "\n3. Get Statistics"
curl -s $BASE_URL/api/courses/stats | python -m json.tool

echo -e "\n4. Create New Course"
curl -s -X POST $BASE_URL/api/courses \
  -H "Content-Type: application/json" \
  -d "{\"name\":\"Test Course\",\"description\":\"Automated test\",\"target_date\":\"2026-12-31\",\"status\":\"Not Started\"}" \
  | python -m json.tool

echo -e "\n5. Search Courses"
curl -s "$BASE_URL/api/courses/search?q=test" | python -m json.tool

echo -e "\nAll tests completed!"
```

Make it executable:
```bash
chmod +x test_api.sh
./test_api.sh
```

---

## Conclusion

You now have comprehensive test cases covering:
- ✅ All 8 API endpoints
- ✅ Success scenarios
- ✅ Error scenarios
- ✅ Edge cases
- ✅ Different testing methods (curl, PowerShell)
- ✅ Automated test scripts

**Happy Testing! 🧪**
