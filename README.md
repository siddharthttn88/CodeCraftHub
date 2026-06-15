# CodeCraftHub - Course Management REST API

> 🎓 **A beginner-friendly Python Flask REST API for managing learning courses**

Perfect for learning REST API concepts, CRUD operations, and backend development!

---

## 📚 Table of Contents

1. [What is This Project?](#what-is-this-project)
2. [What You'll Learn](#what-youll-learn)
3. [Features](#features)
4. [Technology Stack](#technology-stack)
5. [Project Structure Explained](#project-structure-explained)
6. [Installation (Step-by-Step)](#installation-step-by-step)
7. [How to Run the Application](#how-to-run-the-application)
8. [Understanding REST APIs](#understanding-rest-apis)
9. [API Endpoints Documentation](#api-endpoints-documentation)
10. [Testing the API](#testing-the-api)
11. [Troubleshooting](#troubleshooting)
12. [Common Beginner Mistakes](#common-beginner-mistakes)
13. [Learning Resources](#learning-resources)
14. [Next Steps](#next-steps)

---

## What is This Project?

**CodeCraftHub** is a complete REST API (Application Programming Interface) built with Python and Flask. It helps you manage learning courses - think of it as a backend system for tracking your educational journey.

### Why is this useful for beginners?

- 📖 **Learn REST API Basics**: Understand how web APIs work
- 🔧 **Practice CRUD Operations**: Create, Read, Update, Delete data
- 🐍 **Python & Flask**: Learn the popular Flask web framework
- 💾 **JSON Storage**: Simple file-based storage (no database complexity)
- 🧪 **Complete Test Suite**: Learn API testing best practices
- 📝 **Well-Commented Code**: Every function explained in detail

### What Can You Do With It?

- Create courses (e.g., "Python Basics", "Web Development")
- Track course status (Not Started, In Progress, Completed)
- Set target completion dates
- Search through your courses
- View statistics about your learning progress
- Update course information
- Delete courses you no longer need

---

## What You'll Learn

By studying and using this project, you'll understand:

✅ **REST API Concepts**
- What is an API and how does it work?
- HTTP methods (GET, POST, PUT, DELETE)
- Status codes (200, 201, 400, 404, 500)
- JSON data format

✅ **Flask Framework**
- Setting up a Flask application
- Creating routes/endpoints
- Handling requests and responses
- Error handling

✅ **CRUD Operations**
- **C**reate: Add new data
- **R**ead: Retrieve existing data
- **U**pdate: Modify existing data
- **D**elete: Remove data

✅ **API Testing**
- Using curl commands
- Automated testing with Python
- Error scenario testing

✅ **Best Practices**
- Code organization
- Input validation
- Consistent response format
- Proper error messages

---

## Features

### Core Functionality
- ✅ **Complete CRUD Operations** - All basic database operations
- ✅ **RESTful Design** - Follows REST API conventions
- ✅ **JSON Storage** - Simple file-based storage (no database needed)
- ✅ **Auto-generated IDs** - Unique ID for each course
- ✅ **Timestamps** - Tracks when courses were created
- ✅ **Input Validation** - Prevents invalid data entry

### Bonus Features
- ✅ **Course Search** - Find courses by name or description
- ✅ **Statistics Dashboard** - View course counts by status
- ✅ **CORS Enabled** - Ready for frontend integration
- ✅ **Error Handling** - Proper error messages for debugging
- ✅ **Consistent Responses** - All endpoints return same JSON format

### For Learners
- ✅ **Beginner-Friendly Code** - Extensive comments explaining everything
- ✅ **Complete Documentation** - 6 documentation files included
- ✅ **Test Suite** - 30+ test cases with multiple testing methods
- ✅ **Examples** - Ready-to-copy curl commands
- ✅ **Troubleshooting Guide** - Solutions for common issues

---

## Technology Stack

### Core Technologies

| Technology | Version | Purpose |
|------------|---------|---------|
| **Python** | 3.7+ | Programming language |
| **Flask** | 3.0.0 | Web framework for building APIs |
| **Flask-CORS** | 4.0.0 | Handles Cross-Origin Resource Sharing |
| **JSON** | Built-in | Data storage format |

### Why These Technologies?

**Python**: 
- Easy to learn and read
- Great for beginners
- Large community and resources

**Flask**:
- Lightweight and simple
- Perfect for learning APIs
- Minimal setup required

**JSON**:
- Human-readable data format
- Standard for web APIs
- No database installation needed

---

## Project Structure Explained

Here's what each file does in the project:

```
codecrafthub/
│
├── 📄 app.py                    # Main application file (START HERE!)
│   └── Contains all API endpoints and helper functions
│
├── 📊 courses.json              # Data storage file
│   └── Stores all course data in JSON format
│
├── 📋 requirements.txt          # Python dependencies
│   └── Lists packages to install (Flask, Flask-CORS)
│
├── 📖 README.md                 # This file! Main documentation
│
├── 🚀 QUICKSTART.md            # Get started in 3 steps
│
├── 🧪 TESTING_GUIDE.md         # Complete testing guide
│   └── Explains 6 different ways to test the API
│
├── 📝 TEST_CASES.md            # 30+ specific test cases
│   └── Ready-to-copy curl commands
│
├── 🐍 test_api.py              # Automated Python test script
│   └── Run with: python test_api.py
│
├── 🐚 test_api.sh              # Bash test script (Mac/Linux)
│   └── Run with: ./test_api.sh
│
├── 💻 test_api.ps1             # PowerShell script (Windows)
│   └── Run with: .\test_api.ps1
│
├── 📁 FILES_OVERVIEW.md        # Detailed file reference
│
└── 🚫 .gitignore               # Git ignore configuration
    └── Files to exclude from version control
```

### File Sizes Reference

| File | Size | Purpose |
|------|------|---------|
| `app.py` | ~12 KB | Main application logic |
| `courses.json` | <1 KB | Sample data storage |
| `README.md` | ~13 KB | Main documentation |
| `TEST_CASES.md` | ~21 KB | Test documentation |
| `test_api.py` | ~14 KB | Automated tests |

---

## Installation (Step-by-Step)

Follow these steps carefully to set up the project on your computer.

### Prerequisites (What You Need First)

Before starting, make sure you have:

1. **Python 3.7 or higher** installed
   - Check your version: `python --version` or `python3 --version`
   - Download from: https://www.python.org/downloads/

2. **pip** (Python package installer)
   - Usually comes with Python
   - Check if installed: `pip --version`

3. **Text Editor or IDE** (optional but recommended)
   - VS Code, PyCharm, or any code editor
   - For viewing and editing code

4. **Terminal/Command Prompt**
   - Command Prompt (Windows)
   - Terminal (Mac/Linux)
   - PowerShell (Windows)

### Step 1: Download the Project

**Option A: If you have Git**
```bash
git clone <repository-url>
cd CodeCraftHub
```

**Option B: If you don't have Git**
1. Download the project ZIP file
2. Extract it to a folder
3. Open terminal/command prompt
4. Navigate to the folder:
   ```bash
   cd path/to/CodeCraftHub
   ```

### Step 2: Verify You're in the Right Directory

Check that you see the project files:

**Windows:**
```bash
dir
```

**Mac/Linux:**
```bash
ls
```

You should see files like `app.py`, `requirements.txt`, `README.md`, etc.

### Step 3: Create a Virtual Environment

A virtual environment keeps your project dependencies separate from other Python projects.

**Why is this important?**
- Prevents package conflicts
- Makes your project portable
- Follows Python best practices

**On Windows:**
```bash
# Create virtual environment
python -m venv venv

# Activate it
venv\Scripts\activate
```

**On Mac/Linux:**
```bash
# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate
```

**How do I know it worked?**
- Your terminal prompt should show `(venv)` at the beginning
- Example: `(venv) C:\Users\YourName\CodeCraftHub>`

### Step 4: Install Dependencies

With your virtual environment activated, install the required packages:

```bash
pip install -r requirements.txt
```

**What this installs:**
- Flask (web framework)
- Flask-CORS (for handling cross-origin requests)

**Expected output:**
```
Successfully installed Flask-3.0.0 Flask-CORS-4.0.0
```

**Troubleshooting:**
- If `pip` doesn't work, try `pip3`
- If you get permission errors, use `pip install --user -r requirements.txt`

### Step 5: Verify Installation

Check that packages are installed correctly:

```bash
pip list
```

You should see Flask and Flask-CORS in the list.

---

## How to Run the Application

Now that everything is installed, let's start the API server!

### Starting the Server

**Step 1: Make sure your virtual environment is activated**
- You should see `(venv)` in your terminal prompt
- If not, activate it again (see Step 3 in Installation)

**Step 2: Run the application**
```bash
python app.py
```

**Step 3: Look for success messages**

You should see output similar to this:

```
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://192.168.1.x:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: xxx-xxx-xxx
```

**Step 4: Test that it's working**

Open your web browser and go to:
```
http://localhost:5000
```

You should see a JSON response:
```json
{
    "success": true,
    "message": "CodeCraftHub API is running!",
    "version": "1.0.0"
}
```

### What Just Happened?

1. **Flask started a web server** on your computer
2. **Port 5000** is now listening for HTTP requests
3. **The API is ready** to receive requests at `http://localhost:5000`
4. **courses.json** will be created automatically (if it doesn't exist)

### Stopping the Server

To stop the server:
- Press `Ctrl+C` in the terminal
- The server will shut down gracefully

### Restarting the Server

To restart after making code changes:
1. Stop the server (`Ctrl+C`)
2. Run `python app.py` again

**Note:** Debug mode is enabled, so the server auto-restarts when you save changes to `app.py`!

---

## Understanding REST APIs

Before we dive into the endpoints, let's understand what a REST API is.

### What is an API?

**API** = **A**pplication **P**rogramming **I**nterface

Think of an API as a waiter in a restaurant:
- **You (Client)**: Order food
- **Waiter (API)**: Takes your order to the kitchen
- **Kitchen (Server)**: Prepares the food
- **Waiter (API)**: Brings food back to you

### What is REST?

**REST** = **RE**presentational **S**tate **T**ransfer

REST is a set of rules for building APIs. A RESTful API uses:
- **HTTP Methods** (GET, POST, PUT, DELETE)
- **URLs** (endpoints like `/api/courses`)
- **JSON** (data format)

### HTTP Methods Explained

| Method | Purpose | Example |
|--------|---------|---------|
| **GET** | Retrieve data | Get all courses |
| **POST** | Create new data | Create a new course |
| **PUT** | Update existing data | Update course status |
| **DELETE** | Remove data | Delete a course |

### CRUD Operations

**CRUD** is a concept in data management:

| Operation | HTTP Method | What It Does | Example |
|-----------|-------------|--------------|---------|
| **C**reate | POST | Add new data | Add a new course |
| **R**ead | GET | Retrieve data | Get course list |
| **U**pdate | PUT | Modify data | Change course status |
| **D**elete | DELETE | Remove data | Delete a course |

### URL Structure (Endpoints)

Our API uses this URL pattern:

```
http://localhost:5000/api/courses
     │              │    │      │
     │              │    │      └─ Resource (what you're accessing)
     │              │    └──────── API prefix
     │              └───────────── Port number
     └──────────────────────────── Base URL (your computer)
```

### Status Codes

HTTP status codes tell you if your request succeeded or failed:

| Code | Meaning | When You See It |
|------|---------|-----------------|
| **200** | OK | Request succeeded |
| **201** | Created | New resource created |
| **400** | Bad Request | Invalid data sent |
| **404** | Not Found | Resource doesn't exist |
| **500** | Server Error | Something broke on server |

### JSON Format

All our API responses use JSON (JavaScript Object Notation):

```json
{
    "key": "value",
    "number": 123,
    "boolean": true,
    "array": [1, 2, 3],
    "object": {
        "nested": "data"
    }
}
```

**Why JSON?**
- Human-readable
- Easy to parse
- Standard for web APIs
- Supported by all programming languages

---

## API Endpoints Documentation

### Base URL

All endpoints start with:
```
http://localhost:5000
```

### Standard Response Format

Every endpoint returns JSON in this format:

**✅ Success Response:**
```json
{
    "success": true,
    "message": "Descriptive message",
    "data": {
        "actual": "response data here"
    }
}
```

**❌ Error Response:**
```json
{
    "success": false,
    "message": "Error description"
}
```

**Why this format?**
- **Consistent**: All endpoints return same structure
- **Clear**: Easy to check if request succeeded
- **Informative**: Message explains what happened

### Course Object Schema

This is what a course object looks like:

```json
{
    "id": 1,
    "name": "Python Basics",
    "description": "Learn Python fundamentals including variables, data types, and functions",
    "target_date": "2025-12-31",
    "status": "In Progress",
    "created_at": "2025-11-04 10:30:00"
}
```

**Field Explanations:**

| Field | Type | Description | Required? |
|-------|------|-------------|-----------|
| `id` | Number | Unique identifier (auto-generated) | No (created automatically) |
| `name` | String | Course name | Yes |
| `description` | String | Course description | Yes |
| `target_date` | String | Target completion date (YYYY-MM-DD) | Yes |
| `status` | String | Current status (see allowed values below) | Yes |
| `created_at` | String | Creation timestamp (auto-generated) | No (created automatically) |

**Allowed Status Values:**
- `"Not Started"` - Haven't begun the course yet
- `"In Progress"` - Currently learning
- `"Completed"` - Finished the course

---

## Endpoint Details

### 1️⃣ Health Check

**What it does:** Check if the API is running

**When to use:** When you first start the server or troubleshooting

**Endpoint:** `GET /`

**Example Request:**
```bash
curl http://localhost:5000/
```

**Expected Response (200 OK):**
```json
{
    "success": true,
    "message": "CodeCraftHub API is running!",
    "version": "1.0.0"
}
```

**What this tells you:**
- ✅ Server is running
- ✅ API is accessible
- ✅ Ready to handle requests

---

### 2️⃣ Create a New Course

**What it does:** Add a new course to your learning list

**When to use:** When you start learning something new

**Endpoint:** `POST /api/courses`

**Required Fields:**
- `name` - Course name (string)
- `description` - Course description (string)
- `target_date` - When you want to finish (string, format: YYYY-MM-DD)
- `status` - Current status (string: "Not Started", "In Progress", or "Completed")

**Example Request:**
```bash
curl -X POST http://localhost:5000/api/courses \
  -H "Content-Type: application/json" \
  -d '{"name":"React Fundamentals","description":"Learn React hooks and components","target_date":"2026-03-15","status":"Not Started"}'
```

**Breakdown of the command:**
- `-X POST` - Use POST method
- `-H "Content-Type: application/json"` - Tell server we're sending JSON
- `-d '{...}'` - The actual JSON data

**Expected Response (201 Created):**
```json
{
    "success": true,
    "message": "Course created successfully",
    "data": {
        "id": 4,
        "name": "React Fundamentals",
        "description": "Learn React hooks and components",
        "target_date": "2026-03-15",
        "status": "Not Started",
        "created_at": "2026-06-15 22:00:00"
    }
}
```

**What happened:**
1. API received your course data
2. Validated all required fields
3. Generated a unique ID (4 in this example)
4. Added a timestamp
5. Saved to `courses.json`
6. Returned the complete course object

**Error Example - Missing Field:**

Request:
```bash
curl -X POST http://localhost:5000/api/courses \
  -H "Content-Type: application/json" \
  -d '{"name":"Incomplete Course"}'
```

Response (400 Bad Request):
```json
{
    "success": false,
    "message": "Missing required field: description"
}
```

**Error Example - Invalid Status:**

Request:
```bash
curl -X POST http://localhost:5000/api/courses \
  -H "Content-Type: application/json" \
  -d '{"name":"Test","description":"Test","target_date":"2026-12-31","status":"Maybe Later"}'
```

Response (400 Bad Request):
```json
{
    "success": false,
    "message": "Invalid status. Allowed values: Not Started, In Progress, Completed"
}
```

---

### 3️⃣ Get All Courses

**What it does:** Retrieve a list of all your courses

**When to use:** View your complete learning catalog

**Endpoint:** `GET /api/courses`

**Example Request:**
```bash
curl http://localhost:5000/api/courses
```

**Expected Response (200 OK):**
```json
{
    "success": true,
    "message": "Courses retrieved successfully",
    "data": [
        {
            "id": 1,
            "name": "Python Basics",
            "description": "Learn Python fundamentals",
            "target_date": "2025-12-31",
            "status": "In Progress",
            "created_at": "2025-11-04 10:30:00"
        },
        {
            "id": 2,
            "name": "Flask Web Development",
            "description": "Master Flask framework",
            "target_date": "2026-01-15",
            "status": "Not Started",
            "created_at": "2025-11-04 11:00:00"
        },
        {
            "id": 3,
            "name": "JavaScript ES6+",
            "description": "Modern JavaScript features",
            "target_date": "2025-11-30",
            "status": "Completed",
            "created_at": "2025-11-04 11:15:00"
        }
    ]
}
```

**What you get:**
- Array of all courses
- Each course has complete information
- Courses in order they were added

**If no courses exist:**
```json
{
    "success": true,
    "message": "Courses retrieved successfully",
    "data": []
}
```

---

### 4️⃣ Get a Specific Course

**What it does:** Retrieve details of one specific course

**When to use:** View detailed information about a particular course

**Endpoint:** `GET /api/courses/<id>`

Replace `<id>` with the actual course ID number.

**Example Request:**
```bash
curl http://localhost:5000/api/courses/1
```

**Expected Response (200 OK):**
```json
{
    "success": true,
    "message": "Course retrieved successfully",
    "data": {
        "id": 1,
        "name": "Python Basics",
        "description": "Learn Python fundamentals",
        "target_date": "2025-12-31",
        "status": "In Progress",
        "created_at": "2025-11-04 10:30:00"
    }
}
```

**Error Response - Course Not Found (404):**
```bash
curl http://localhost:5000/api/courses/999
```

Response:
```json
{
    "success": false,
    "message": "Course not found"
}
```

**When you get 404:**
- The course ID doesn't exist
- Check the ID number
- Use GET `/api/courses` to see all available IDs

---

### 5️⃣ Update a Course

**What it does:** Modify an existing course

**When to use:** Change course status, extend deadline, update description

**Endpoint:** `PUT /api/courses/<id>`

**Note:** All fields are optional - only send what you want to change!

**Example 1: Update Status Only**
```bash
curl -X PUT http://localhost:5000/api/courses/1 \
  -H "Content-Type: application/json" \
  -d '{"status":"Completed"}'
```

**Example 2: Update Multiple Fields**
```bash
curl -X PUT http://localhost:5000/api/courses/1 \
  -H "Content-Type: application/json" \
  -d '{"status":"In Progress","target_date":"2026-02-28"}'
```

**Example 3: Update Everything**
```bash
curl -X PUT http://localhost:5000/api/courses/1 \
  -H "Content-Type: application/json" \
  -d '{"name":"Advanced Python","description":"Deep dive into Python","target_date":"2026-03-31","status":"In Progress"}'
```

**Expected Response (200 OK):**
```json
{
    "success": true,
    "message": "Course updated successfully",
    "data": {
        "id": 1,
        "name": "Python Basics",
        "description": "Learn Python fundamentals",
        "target_date": "2025-12-31",
        "status": "Completed",
        "created_at": "2025-11-04 10:30:00"
    }
}
```

**Key Points:**
- Only specified fields are updated
- Other fields remain unchanged
- `id` and `created_at` cannot be changed
- Returns the updated course object

**Error Response - Course Not Found (404):**
```json
{
    "success": false,
    "message": "Course not found"
}
```

**Error Response - Invalid Status (400):**
```json
{
    "success": false,
    "message": "Invalid status. Allowed values: Not Started, In Progress, Completed"
}
```

---

### 6️⃣ Delete a Course

**What it does:** Remove a course from your list

**When to use:** Course no longer needed or added by mistake

**Endpoint:** `DELETE /api/courses/<id>`

**⚠️ Warning:** This action cannot be undone!

**Example Request:**
```bash
curl -X DELETE http://localhost:5000/api/courses/1
```

**Expected Response (200 OK):**
```json
{
    "success": true,
    "message": "Course deleted successfully",
    "data": {
        "id": 1,
        "name": "Python Basics",
        "description": "Learn Python fundamentals",
        "target_date": "2025-12-31",
        "status": "Completed",
        "created_at": "2025-11-04 10:30:00"
    }
}
```

**What happened:**
1. API found the course with ID 1
2. Removed it from `courses.json`
3. Returned the deleted course data (so you have a record)

**Error Response - Course Not Found (404):**
```bash
curl -X DELETE http://localhost:5000/api/courses/999
```

Response:
```json
{
    "success": false,
    "message": "Course not found"
}
```

**Verify Deletion:**
```bash
# Try to get the deleted course - should return 404
curl http://localhost:5000/api/courses/1
```

---

### 7️⃣ Get Course Statistics (Bonus)

**What it does:** Get a summary of your courses by status

**When to use:** View your learning progress at a glance

**Endpoint:** `GET /api/courses/stats`

**Example Request:**
```bash
curl http://localhost:5000/api/courses/stats
```

**Expected Response (200 OK):**
```json
{
    "success": true,
    "message": "Statistics retrieved successfully",
    "data": {
        "total_courses": 5,
        "not_started": 2,
        "in_progress": 2,
        "completed": 1
    }
}
```

**What the numbers mean:**
- `total_courses`: Total number of courses you have
- `not_started`: Courses you haven't begun yet
- `in_progress`: Courses you're currently learning
- `completed`: Courses you've finished

**Use Case Example:**
```
You have 5 courses:
- 2 you haven't started
- 2 you're working on
- 1 you've completed

Progress: 20% complete (1 out of 5)
```

---

### 8️⃣ Search Courses (Bonus)

**What it does:** Find courses by name or description

**When to use:** Quickly find courses containing specific keywords

**Endpoint:** `GET /api/courses/search?q=<keyword>`

**Features:**
- ✅ Case-insensitive (Python = python = PYTHON)
- ✅ Searches both name and description
- ✅ Returns all matching courses

**Example 1: Search for "python"**
```bash
curl "http://localhost:5000/api/courses/search?q=python"
```

**Expected Response (200 OK):**
```json
{
    "success": true,
    "message": "Found 2 course(s)",
    "data": [
        {
            "id": 1,
            "name": "Python Basics",
            "description": "Learn Python fundamentals",
            "target_date": "2025-12-31",
            "status": "In Progress",
            "created_at": "2025-11-04 10:30:00"
        },
        {
            "id": 4,
            "name": "Advanced Python",
            "description": "Master Python programming",
            "target_date": "2026-03-15",
            "status": "Not Started",
            "created_at": "2025-11-05 09:00:00"
        }
    ]
}
```

**Example 2: Search for "web"**
```bash
curl "http://localhost:5000/api/courses/search?q=web"
```

**Example 3: No Results Found**
```bash
curl "http://localhost:5000/api/courses/search?q=blockchain"
```

Response:
```json
{
    "success": true,
    "message": "Found 0 course(s)",
    "data": []
}
```

**Error Response - Missing Query (400):**
```bash
curl "http://localhost:5000/api/courses/search"
```

Response:
```json
{
    "success": false,
    "message": "Search query parameter \"q\" is required"
}
```

**Important Note:**
- Always include the query parameter `?q=`
- Use quotes around the URL if it contains special characters
- Search is case-insensitive

---

## Testing the API

There are multiple ways to test the API. Choose the method that works best for you!

### Method 1: Automated Python Script (Recommended for Beginners)

**Why this method?**
- ✅ Runs all tests automatically
- ✅ Colored output (easy to see results)
- ✅ No manual typing
- ✅ Tests both success and error scenarios

**Prerequisites:**
```bash
pip install requests
```

**Run Tests:**
```bash
python test_api.py
```

**What you'll see:**
```
==============================================================
CodeCraftHub API - Automated Test Suite
==============================================================
Base URL: http://localhost:5000
Started at: 2026-06-15 22:00:00

==============================================================
Test: Health Check
==============================================================
ℹ INFO: Status Code: 200
✓ PASS: Health check passed

==============================================================
Test: Create Course - Success
==============================================================
ℹ INFO: Status Code: 201
✓ PASS: Course created successfully with ID: 4

==============================================================
TEST SUMMARY
==============================================================
Total Tests: 14
Passed: 14
Failed: 0

🎉 All tests passed!
```

---

### Method 2: Quick Test Scripts

**For Mac/Linux/Unix:**
```bash
chmod +x test_api.sh
./test_api.sh
```

**For Windows (PowerShell):**
```powershell
.\test_api.ps1
```

These scripts run 12 comprehensive tests covering all endpoints.

---

### Method 3: Manual Testing with curl

**Perfect for learning!** Test each endpoint one by one.

See `TEST_CASES.md` for 30+ ready-to-copy curl commands.

**Quick Example:**
```bash
# 1. Check API is running
curl http://localhost:5000/

# 2. Get all courses
curl http://localhost:5000/api/courses

# 3. Create a course
curl -X POST http://localhost:5000/api/courses \
  -H "Content-Type: application/json" \
  -d '{"name":"Test Course","description":"Testing API","target_date":"2026-12-31","status":"Not Started"}'

# 4. Get statistics
curl http://localhost:5000/api/courses/stats
```

---

### Method 4: Testing with Postman (GUI)

**Good for visual learners!**

1. Download [Postman](https://www.postman.com/downloads/)
2. Create a new request
3. Set the method (GET, POST, PUT, DELETE)
4. Enter URL: `http://localhost:5000/api/courses`
5. For POST/PUT:
   - Click "Body" tab
   - Select "raw" and "JSON"
   - Enter JSON data
6. Click "Send"

---

### Method 5: Testing with Python Code

**Example Script:**
```python
import requests

BASE_URL = "http://localhost:5000"

# Test 1: Get all courses
response = requests.get(f"{BASE_URL}/api/courses")
print("All Courses:", response.json())

# Test 2: Create a course
new_course = {
    "name": "Docker Basics",
    "description": "Learn containerization",
    "target_date": "2026-12-31",
    "status": "Not Started"
}
response = requests.post(f"{BASE_URL}/api/courses", json=new_course)
print("Created:", response.json())

# Test 3: Get statistics
response = requests.get(f"{BASE_URL}/api/courses/stats")
print("Stats:", response.json())
```

Save as `my_test.py` and run: `python my_test.py`

---

### Method 6: Testing with Web Browser

**Only works for GET requests!**

Open your browser and visit:
- http://localhost:5000/
- http://localhost:5000/api/courses
- http://localhost:5000/api/courses/1
- http://localhost:5000/api/courses/stats
- http://localhost:5000/api/courses/search?q=python

**Note:** Browsers can only do GET requests, not POST/PUT/DELETE.

---

## Troubleshooting

Common issues and how to fix them.

### Issue 1: "Connection Refused" or "Cannot connect"

**Problem:** The API server is not running.

**Solution:**
```bash
# Start the server
python app.py

# You should see:
# * Running on http://127.0.0.1:5000
```

**Check:**
- Is your virtual environment activated? (Look for `(venv)` in prompt)
- Did the server start without errors?
- Are you in the correct directory?

---

### Issue 2: "Port 5000 is already in use"

**Problem:** Another program is using port 5000.

**Solution A - Change the port:**

Edit `app.py`, last line:
```python
# Change from:
app.run(debug=True, host='0.0.0.0', port=5000)

# To:
app.run(debug=True, host='0.0.0.0', port=5001)
```

Then use `http://localhost:5001` instead.

**Solution B - Find and stop the other program:**

**Windows:**
```bash
netstat -ano | findstr :5000
taskkill /PID <process_id> /F
```

**Mac/Linux:**
```bash
lsof -ti:5000 | xargs kill -9
```

---

### Issue 3: "Module not found" errors

**Problem:** Required packages not installed.

**Solution:**
```bash
# Make sure virtual environment is activated
# Look for (venv) in prompt

# Reinstall dependencies
pip install -r requirements.txt

# Verify installation
pip list
```

---

### Issue 4: "JSON parsing error" or "No data provided"

**Problem:** Invalid JSON in your request.

**Common Mistakes:**
❌ Missing quotes around strings
❌ Using single quotes instead of double quotes in JSON
❌ Missing commas between fields
❌ Trailing commas

**Bad:**
```json
{
    'name': 'Test',
    status: "Not Started",
}
```

**Good:**
```json
{
    "name": "Test",
    "status": "Not Started"
}
```

**Solution:**
- Use a JSON validator: https://jsonlint.com/
- Copy examples from documentation exactly
- Check for typos

---

### Issue 5: "Missing required field" errors

**Problem:** You didn't include all required fields.

**When creating a course, you MUST include:**
- ✅ name
- ✅ description
- ✅ target_date
- ✅ status

**Example of correct request:**
```bash
curl -X POST http://localhost:5000/api/courses \
  -H "Content-Type: application/json" \
  -d '{"name":"Test","description":"Description here","target_date":"2026-12-31","status":"Not Started"}'
```

---

### Issue 6: "Course not found" (404)

**Problem:** The course ID doesn't exist.

**Solution:**
```bash
# Get list of all courses to see available IDs
curl http://localhost:5000/api/courses

# Then use a valid ID
curl http://localhost:5000/api/courses/1
```

---

### Issue 7: "Invalid status" error

**Problem:** You used a status value that's not allowed.

**Only these are valid:**
- ✅ "Not Started"
- ✅ "In Progress"
- ✅ "Completed"

**Case-sensitive and must be exact!**

❌ Wrong: "not started", "Not started", "NotStarted", "Pending"

✅ Correct: "Not Started"

---

### Issue 8: courses.json is corrupted

**Problem:** The JSON file has invalid data.

**Solution:**
```bash
# Option 1: Delete the file (it will be recreated)
rm courses.json        # Mac/Linux
del courses.json       # Windows

# Option 2: Fix manually
# Open courses.json in a text editor
# Make sure it's valid JSON: []
```

---

### Issue 9: CORS errors from frontend

**Problem:** Frontend can't connect due to CORS policy.

**Solution:**
- Flask-CORS is already enabled in the code
- Make sure you're using the exact same domain:
  - ✅ Both use `localhost`, OR
  - ✅ Both use `127.0.0.1`
  - ❌ Don't mix `localhost` and `127.0.0.1`

---

### Issue 10: Virtual environment won't activate

**Problem:** Cannot activate venv.

**Windows Solution:**
```bash
# If venv\Scripts\activate doesn't work, try:
.\venv\Scripts\Activate.ps1

# If you get execution policy error:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**Mac/Linux Solution:**
```bash
# Make sure you use source
source venv/bin/activate

# If you get permission error:
chmod +x venv/bin/activate
```

---

## Common Beginner Mistakes

Learn from these common pitfalls!

### ❌ Mistake 1: Not activating virtual environment

**Problem:**
```bash
pip install -r requirements.txt
python app.py
# Error: Module 'flask' not found
```

**Why it happens:** Packages installed globally, not in venv.

**Solution:**
```bash
# Always activate first!
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux

# Then install and run
pip install -r requirements.txt
python app.py
```

---

### ❌ Mistake 2: Forgetting Content-Type header

**Problem:**
```bash
curl -X POST http://localhost:5000/api/courses \
  -d '{"name":"Test"}'
```

**Result:** 400 error - "No data provided"

**Solution:**
```bash
# Always include Content-Type for POST/PUT
curl -X POST http://localhost:5000/api/courses \
  -H "Content-Type: application/json" \
  -d '{"name":"Test","description":"Test","target_date":"2026-12-31","status":"Not Started"}'
```

---

### ❌ Mistake 3: Using wrong quotes in JSON

**Problem:**
```bash
# Single quotes in JSON - WRONG!
curl -X POST http://localhost:5000/api/courses \
  -H "Content-Type: application/json" \
  -d "{'name':'Test'}"
```

**Solution:**
```bash
# Use double quotes in JSON, single quotes for shell
curl -X POST http://localhost:5000/api/courses \
  -H "Content-Type: application/json" \
  -d '{"name":"Test"}'
```

---

### ❌ Mistake 4: Not checking if server is running

**Problem:**
```bash
curl http://localhost:5000/api/courses
# Error: Connection refused
```

**Solution:**
```bash
# Always check server is running first!
python app.py
# Should see: * Running on http://127.0.0.1:5000
```

---

### ❌ Mistake 5: Mixing up IDs

**Problem:**
```bash
# Created course with ID 1, deleted it, now try to update:
curl -X PUT http://localhost:5000/api/courses/1
# Error: Course not found
```

**Why:** Deleted courses are gone! IDs aren't reused.

**Solution:**
```bash
# Always check current courses first
curl http://localhost:5000/api/courses
# Use IDs from the response
```

---

### ❌ Mistake 6: Case-sensitive status values

**Problem:**
```bash
# Using "completed" instead of "Completed"
curl -X POST http://localhost:5000/api/courses \
  -H "Content-Type: application/json" \
  -d '{"name":"Test","description":"Test","target_date":"2026-12-31","status":"completed"}'
```

**Error:** "Invalid status. Allowed values: Not Started, In Progress, Completed"

**Solution:** Use exact capitalization:
- ✅ "Not Started"
- ✅ "In Progress"
- ✅ "Completed"

---

## Learning Resources

### Understanding REST APIs
- 📖 [REST API Tutorial](https://restfulapi.net/) - Comprehensive guide
- 🎥 [What is REST API?](https://www.youtube.com/results?search_query=what+is+rest+api) - YouTube tutorials
- 📝 [HTTP Methods Explained](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods) - MDN Web Docs

### Learning Flask
- 📖 [Official Flask Documentation](https://flask.palletsprojects.com/)
- 📖 [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) - Excellent for beginners
- 🎥 [Flask Tutorial on YouTube](https://www.youtube.com/results?search_query=flask+tutorial+for+beginners)

### Python Basics
- 📖 [Python.org Tutorial](https://docs.python.org/3/tutorial/)
- 📖 [Learn Python](https://www.learnpython.org/) - Interactive tutorial
- 🎓 [Python for Everybody](https://www.py4e.com/) - Free course

### JSON Format
- 📖 [JSON Introduction](https://www.json.org/)
- 🧪 [JSON Formatter](https://jsonformatter.org/) - Validate and format JSON
- 📝 [Working with JSON in Python](https://realpython.com/python-json/)

### Testing APIs
- 📖 [Postman Learning Center](https://learning.postman.com/)
- 📖 [curl Documentation](https://curl.se/docs/manual.html)
- 🧪 [Python Requests Library](https://requests.readthedocs.io/)

---

## Next Steps

Now that you understand the basics, here's what to do next:

### 1. Practice with the API (Beginner)
✅ Run all test cases manually
✅ Create 5 different courses
✅ Practice UPDATE and DELETE operations
✅ Try the search functionality
✅ Get familiar with error messages

### 2. Read the Code (Intermediate)
✅ Open `app.py` and read through it
✅ Understand each helper function
✅ Study how endpoints are defined
✅ Learn about Flask decorators (`@app.route`)

### 3. Modify the Code (Intermediate)
✅ Add a new field to courses (e.g., "difficulty")
✅ Create a new endpoint (e.g., GET courses by status)
✅ Add more validation rules
✅ Change the response format

### 4. Build a Frontend (Advanced)
✅ Create HTML forms to interact with the API
✅ Build a React or Vue.js frontend
✅ Use JavaScript fetch/axios to call endpoints
✅ Create a full-stack application

### 5. Add More Features (Advanced)
✅ User authentication (JWT tokens)
✅ Database integration (PostgreSQL, MongoDB)
✅ Pagination for large datasets
✅ File uploads for course materials
✅ Email notifications for deadlines

### 6. Deploy to Production (Advanced)
✅ Use Gunicorn/uWSGI for production server
✅ Deploy to Heroku, AWS, or DigitalOcean
✅ Set up HTTPS with SSL certificates
✅ Implement logging and monitoring
✅ Add rate limiting

---

## Project Documentation Files

| File | Purpose | When to Read |
|------|---------|--------------|
| `README.md` | Main documentation (this file!) | First! |
| `QUICKSTART.md` | Get started in 3 steps | For quick setup |
| `TESTING_GUIDE.md` | Complete testing guide | Before testing |
| `TEST_CASES.md` | 30+ specific test cases | When testing endpoints |
| `FILES_OVERVIEW.md` | Detailed file reference | To understand structure |
| `TESTING_SUMMARY.md` | Testing suite summary | Overview of tests |

---

## HTTP Status Codes Reference

| Code | Name | Meaning | When You'll See It |
|------|------|---------|-------------------|
| **200** | OK | Success | GET, PUT, DELETE succeeded |
| **201** | Created | Resource created | POST created new course |
| **400** | Bad Request | Invalid data | Missing fields, invalid JSON |
| **404** | Not Found | Resource missing | Course ID doesn't exist |
| **500** | Server Error | Internal error | Something broke (check logs) |

---

## Quick Command Reference

### Setup Commands
```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Mac/Linux)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run server
python app.py
```

### Testing Commands
```bash
# Automated tests
python test_api.py

# Quick scripts
./test_api.sh           # Mac/Linux
.\test_api.ps1          # Windows

# Manual test
curl http://localhost:5000/api/courses
```

### Common curl Commands
```bash
# GET all courses
curl http://localhost:5000/api/courses

# POST create course
curl -X POST http://localhost:5000/api/courses \
  -H "Content-Type: application/json" \
  -d '{"name":"Test","description":"Test","target_date":"2026-12-31","status":"Not Started"}'

# PUT update course
curl -X PUT http://localhost:5000/api/courses/1 \
  -H "Content-Type: application/json" \
  -d '{"status":"Completed"}'

# DELETE course
curl -X DELETE http://localhost:5000/api/courses/1

# GET statistics
curl http://localhost:5000/api/courses/stats

# Search courses
curl "http://localhost:5000/api/courses/search?q=python"
```

---

## Contributing

Want to improve this project?

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## License

This project is open source and available for educational purposes.

---

## Support & Questions

- 📧 **Questions?** Check the [Troubleshooting](#troubleshooting) section
- 🐛 **Found a bug?** Please report it
- 💡 **Have suggestions?** We'd love to hear them!
- 📖 **Need help?** Read through the documentation files

---

## Acknowledgments

- Built with ❤️ for beginners learning REST APIs
- Inspired by real-world API design patterns
- Designed to be educational and practical

---

## Final Words

🎉 **Congratulations on setting up your first REST API!**

Remember:
- ✅ Start small, practice often
- ✅ Read error messages carefully
- ✅ Test each endpoint before moving on
- ✅ Don't be afraid to break things (that's how you learn!)
- ✅ Refer back to this documentation whenever needed

**Happy Learning with CodeCraftHub! 🚀**

---

*Last Updated: June 15, 2026*
