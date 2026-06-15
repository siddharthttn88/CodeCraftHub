# CodeCraftHub API - Complete Testing Guide

This guide provides multiple ways to test the CodeCraftHub API, from beginner-friendly methods to advanced automated testing.

## Quick Start - Choose Your Testing Method

### Method 1: Python Automated Test Script ⭐ Recommended
**Best for:** Complete automated testing with colored output and detailed results

```bash
# Install requests library if not already installed
pip install requests

# Run the automated test suite
python test_api.py
```

**Features:**
- ✅ Runs all 14 test cases automatically
- ✅ Colored output (green for pass, red for fail)
- ✅ Detailed test summary
- ✅ No manual input required

---

### Method 2: Bash Script (Mac/Linux/Unix)
**Best for:** Quick testing with curl commands

```bash
# Make the script executable
chmod +x test_api.sh

# Run the script
./test_api.sh
```

**Requirements:** curl, python (for JSON formatting), optionally jq

---

### Method 3: PowerShell Script (Windows)
**Best for:** Windows users who prefer PowerShell

```powershell
# Run the script
.\test_api.ps1
```

**Note:** PowerShell may require execution policy changes:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

### Method 4: Manual curl Commands
**Best for:** Learning API endpoints, debugging specific requests

See `TEST_CASES.md` for over 30 ready-to-use curl commands organized by endpoint.

**Quick Examples:**

```bash
# Health check
curl http://localhost:5000/

# Get all courses
curl http://localhost:5000/api/courses

# Create a course
curl -X POST http://localhost:5000/api/courses \
  -H "Content-Type: application/json" \
  -d '{"name":"Test Course","description":"Testing","target_date":"2026-12-31","status":"Not Started"}'

# Get statistics
curl http://localhost:5000/api/courses/stats
```

---

### Method 5: Postman Collection
**Best for:** GUI-based testing, saving requests, team collaboration

1. Download [Postman](https://www.postman.com/downloads/)
2. Create a new collection called "CodeCraftHub API"
3. Import the endpoints from `TEST_CASES.md`
4. Save and reuse your requests

---

### Method 6: Python Requests Library
**Best for:** Integrating API into your Python scripts

```python
import requests

BASE_URL = "http://localhost:5000"

# Get all courses
response = requests.get(f"{BASE_URL}/api/courses")
courses = response.json()
print(courses)

# Create a course
new_course = {
    "name": "Python Testing",
    "description": "Learn to test APIs",
    "target_date": "2026-12-31",
    "status": "Not Started"
}
response = requests.post(f"{BASE_URL}/api/courses", json=new_course)
print(response.json())
```

---

## Test Coverage Overview

All test methods cover these scenarios:

### ✅ Success Scenarios (8 tests)
1. Health check endpoint
2. Get all courses
3. Create new course
4. Get specific course by ID
5. Update course
6. Delete course
7. Get statistics
8. Search courses

### ❌ Error Scenarios (6 tests)
1. Missing required fields
2. Invalid status value
3. Course not found (404)
4. Missing search query parameter
5. No data provided
6. Update/delete non-existent course

---

## Running Tests - Step by Step

### Prerequisites
1. Make sure Python 3.x is installed
2. Make sure Flask API is running:
   ```bash
   python app.py
   ```
3. API should be accessible at `http://localhost:5000`

### Option A: Automated Python Tests

```bash
# Step 1: Install dependencies (if not already installed)
pip install requests

# Step 2: Run tests
python test_api.py

# Expected output: Colored test results with pass/fail indicators
```

### Option B: Bash Script

```bash
# Step 1: Make executable (first time only)
chmod +x test_api.sh

# Step 2: Run script
./test_api.sh

# Optional: Install jq for better JSON parsing
brew install jq  # macOS
sudo apt-get install jq  # Ubuntu/Debian
```

### Option C: PowerShell Script

```powershell
# Step 1: Allow script execution (first time only)
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Step 2: Run script
.\test_api.ps1
```

### Option D: Manual Testing

```bash
# Step 1: Open TEST_CASES.md
# Step 2: Copy any test command
# Step 3: Paste in terminal and press Enter
# Step 4: Compare output with expected response
```

---

## Understanding Test Results

### Python Test Script Output

```
==============================================================
Test: Health Check
==============================================================
ℹ INFO: Status Code: 200
ℹ INFO: Response: {
  "success": true,
  "message": "CodeCraftHub API is running!",
  "version": "1.0.0"
}
✓ PASS: Health check passed
```

**Legend:**
- `✓ PASS` (Green) - Test passed successfully
- `✗ FAIL` (Red) - Test failed
- `ℹ INFO` (Yellow) - Additional information

### curl Output

```json
{
    "success": true,
    "message": "Operation successful",
    "data": {}
}
```

**Check:**
- `success: true` = Operation succeeded
- `success: false` = Operation failed (expected for error tests)
- Status code matches expected value

---

## Common Testing Scenarios

### Scenario 1: Test Complete CRUD Workflow

```bash
# 1. Create
RESPONSE=$(curl -s -X POST http://localhost:5000/api/courses \
  -H "Content-Type: application/json" \
  -d '{"name":"CRUD Test","description":"Testing workflow","target_date":"2026-12-31","status":"Not Started"}')

# Extract ID (requires jq)
ID=$(echo $RESPONSE | jq -r '.data.id')

# 2. Read
curl http://localhost:5000/api/courses/$ID

# 3. Update
curl -X PUT http://localhost:5000/api/courses/$ID \
  -H "Content-Type: application/json" \
  -d '{"status":"Completed"}'

# 4. Delete
curl -X DELETE http://localhost:5000/api/courses/$ID
```

### Scenario 2: Test Error Handling

```bash
# Missing fields
curl -X POST http://localhost:5000/api/courses \
  -H "Content-Type: application/json" \
  -d '{"name":"Test"}'

# Invalid status
curl -X POST http://localhost:5000/api/courses \
  -H "Content-Type: application/json" \
  -d '{"name":"Test","description":"Test","target_date":"2026-12-31","status":"Invalid"}'

# Non-existent course
curl http://localhost:5000/api/courses/99999
```

### Scenario 3: Test Search Functionality

```bash
# Search for Python courses
curl "http://localhost:5000/api/courses/search?q=python"

# Case-insensitive search
curl "http://localhost:5000/api/courses/search?q=FLASK"

# No results
curl "http://localhost:5000/api/courses/search?q=nonexistent"
```

---

## Troubleshooting Test Issues

### Issue: Connection Refused

**Problem:** Cannot connect to API

**Solution:**
```bash
# Make sure Flask is running
python app.py

# Check if running on correct port
netstat -an | grep 5000
```

### Issue: JSON Parsing Error

**Problem:** curl output not formatted

**Solution:**
```bash
# Install python for JSON formatting
# or use jq
brew install jq  # macOS
sudo apt-get install jq  # Linux

# Then use:
curl http://localhost:5000/api/courses | jq
```

### Issue: Script Won't Execute (Bash)

**Problem:** Permission denied

**Solution:**
```bash
chmod +x test_api.sh
./test_api.sh
```

### Issue: Script Won't Execute (PowerShell)

**Problem:** Execution policy restriction

**Solution:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Issue: Module Not Found (Python)

**Problem:** requests module not installed

**Solution:**
```bash
pip install requests
```

---

## Advanced Testing Tips

### 1. Save Test Results to File

```bash
# Save Python test results
python test_api.py > test_results.txt

# Save curl output
curl http://localhost:5000/api/courses > courses.json
```

### 2. Test with Different Data

```bash
# Create multiple courses
for i in {1..5}; do
  curl -X POST http://localhost:5000/api/courses \
    -H "Content-Type: application/json" \
    -d "{\"name\":\"Course $i\",\"description\":\"Test course $i\",\"target_date\":\"2026-12-31\",\"status\":\"Not Started\"}"
done
```

### 3. Measure Response Time

```bash
# Using curl with timing
curl -w "\nTime: %{time_total}s\n" http://localhost:5000/api/courses

# Using time command
time curl http://localhost:5000/api/courses
```

### 4. Test with Invalid JSON

```bash
# Malformed JSON (missing quote)
curl -X POST http://localhost:5000/api/courses \
  -H "Content-Type: application/json" \
  -d '{"name":"Test"invalid}'
```

---

## Test File Reference

| File | Purpose | When to Use |
|------|---------|-------------|
| `test_api.py` | Automated Python test suite | Complete testing, CI/CD |
| `test_api.sh` | Bash script for Unix/Linux/Mac | Quick testing on Unix |
| `test_api.ps1` | PowerShell script for Windows | Quick testing on Windows |
| `TEST_CASES.md` | Manual test documentation | Learning, debugging |
| `TESTING_GUIDE.md` | This file | Understanding testing |

---

## Integration with CI/CD

### GitHub Actions Example

```yaml
name: API Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.9'
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Start API
        run: python app.py &
      - name: Wait for API
        run: sleep 5
      - name: Run tests
        run: python test_api.py
```

---

## Best Practices

1. **Always test on a fresh copy** of courses.json to ensure consistent results
2. **Run tests in order** (especially when IDs are created dynamically)
3. **Check both success and error cases** to ensure proper error handling
4. **Verify status codes** match expected values
5. **Review response data** to ensure correct information is returned
6. **Test edge cases** (empty strings, very long strings, special characters)

---

## Next Steps

After testing the API:

1. ✅ Verify all endpoints work correctly
2. ✅ Understand the request/response format
3. ✅ Build a frontend application
4. ✅ Add authentication
5. ✅ Deploy to production

---

## Need Help?

- See `README.md` for API documentation
- See `TEST_CASES.md` for specific curl commands
- Check Flask logs for detailed error messages
- Review `app.py` code comments for implementation details

**Happy Testing! 🧪**
