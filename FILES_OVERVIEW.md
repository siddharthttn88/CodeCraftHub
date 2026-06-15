# CodeCraftHub - Files Overview

This document provides a quick reference for all files in the project and their purposes.

## Core Application Files

### `app.py`
**Purpose:** Main Flask application with all API endpoints

**Contains:**
- Helper functions (load_courses, save_courses, get_next_id, validate_course_data)
- 8 API endpoints (POST, GET, PUT, DELETE for courses)
- Bonus endpoints (statistics, search)
- Error handling and CORS configuration

**When to modify:** When adding new endpoints or changing business logic

---

### `courses.json`
**Purpose:** JSON file for storing course data

**Contains:**
- Array of course objects with id, name, description, target_date, status, created_at
- Sample data with 3 example courses

**When to modify:** 
- Automatically modified by the API
- Manually edit to reset test data
- Delete to start fresh (will be auto-created)

---

### `requirements.txt`
**Purpose:** Python package dependencies

**Contains:**
- Flask==3.0.0
- Flask-CORS==4.0.0

**When to modify:** When adding new Python packages to the project

---

## Documentation Files

### `README.md`
**Purpose:** Main project documentation

**Contains:**
- Project overview and features
- Complete installation instructions
- API endpoint documentation with examples
- Sample curl commands for each endpoint
- Troubleshooting guide
- Production deployment tips

**When to read:** First file to read when starting the project

---

### `QUICKSTART.md`
**Purpose:** Get started in 3 simple steps

**Contains:**
- Minimal instructions to run the API
- Quick test commands
- Link to full documentation

**When to read:** When you want to start quickly without reading full docs

---

### `TESTING_GUIDE.md`
**Purpose:** Complete guide to testing the API

**Contains:**
- 6 different testing methods
- Step-by-step instructions for each method
- Test coverage overview
- Troubleshooting test issues
- Advanced testing tips
- CI/CD integration examples

**When to read:** Before testing the API or setting up automated tests

---

### `TEST_CASES.md`
**Purpose:** Comprehensive test cases with curl commands

**Contains:**
- 30+ ready-to-copy curl commands
- Tests for all 8 endpoints
- Success scenarios (8 tests)
- Error scenarios (6 tests)
- Expected responses for each test
- PowerShell alternatives for Windows
- Complete test workflow

**When to read:** When manually testing specific endpoints

---

### `FILES_OVERVIEW.md`
**Purpose:** This file - quick reference for all project files

**Contains:**
- Description of each file
- Purpose and contents
- When to use/modify each file

**When to read:** To understand the project structure

---

## Test Scripts

### `test_api.py`
**Purpose:** Automated Python test script

**Contains:**
- 14 automated test functions
- Colored terminal output
- Test summary with pass/fail counts
- Comprehensive error handling

**How to run:**
```bash
pip install requests
python test_api.py
```

**When to use:**
- Complete automated testing
- CI/CD integration
- Regression testing after changes
- Quick verification that everything works

---

### `test_api.sh`
**Purpose:** Bash script for Unix/Linux/Mac users

**Contains:**
- 12 curl-based tests
- Automatic course creation and cleanup
- JSON formatting with python/jq
- Success/error scenario tests

**How to run:**
```bash
chmod +x test_api.sh
./test_api.sh
```

**When to use:**
- Quick testing on Mac/Linux
- Shell script integration
- Command-line testing

---

### `test_api.ps1`
**Purpose:** PowerShell script for Windows users

**Contains:**
- 12 PowerShell-based tests
- Automatic course creation and cleanup
- JSON conversion and formatting
- Error handling with try-catch blocks

**How to run:**
```powershell
.\test_api.ps1
```

**When to use:**
- Quick testing on Windows
- PowerShell integration
- Windows automation

---

## Configuration Files

### `.gitignore`
**Purpose:** Specifies files Git should ignore

**Contains:**
- Python cache files (__pycache__, *.pyc)
- Virtual environment folders (venv/, env/)
- IDE files (.vscode/, .idea/)
- OS files (.DS_Store, Thumbs.db)
- Environment variables (.env)
- Log files (*.log)

**When to modify:** When adding new types of files that shouldn't be committed

---

## File Dependencies

```
app.py
  ↓ creates/reads
courses.json
  ↓ requires
requirements.txt (Flask, Flask-CORS)

README.md
  ↓ references
TESTING_GUIDE.md
  ↓ references
TEST_CASES.md

test_api.py
test_api.sh   } All test the API at http://localhost:5000
test_api.ps1
```

---

## Quick Reference Table

| File | Type | Size | Read First? | Modify? |
|------|------|------|-------------|---------|
| `README.md` | Docs | Large | ✅ Yes | No |
| `QUICKSTART.md` | Docs | Small | ✅ Yes | No |
| `app.py` | Code | Large | After README | Only for new features |
| `courses.json` | Data | Small | No | Auto-modified |
| `requirements.txt` | Config | Tiny | No | Only for new packages |
| `TESTING_GUIDE.md` | Docs | Large | Before testing | No |
| `TEST_CASES.md` | Docs | Large | When testing | No |
| `test_api.py` | Test | Large | No | Only to add tests |
| `test_api.sh` | Test | Medium | No | Only to add tests |
| `test_api.ps1` | Test | Medium | No | Only to add tests |
| `.gitignore` | Config | Small | No | Rarely |
| `FILES_OVERVIEW.md` | Docs | Medium | For structure | No |

---

## Recommended Reading Order

### For Beginners:
1. `QUICKSTART.md` - Get started fast
2. `README.md` - Understand the full project
3. `TEST_CASES.md` - Learn to test endpoints
4. `app.py` - Study the code

### For Testers:
1. `TESTING_GUIDE.md` - Choose testing method
2. `TEST_CASES.md` - See specific test cases
3. Run `test_api.py` - Automated testing

### For Developers:
1. `README.md` - Project overview
2. `app.py` - Core implementation
3. `requirements.txt` - Dependencies
4. `test_api.py` - Test suite

---

## File Sizes (Approximate)

| File | Lines of Code/Text |
|------|-------------------|
| `app.py` | ~415 lines |
| `README.md` | ~550 lines |
| `TEST_CASES.md` | ~800 lines |
| `TESTING_GUIDE.md` | ~350 lines |
| `test_api.py` | ~420 lines |
| `test_api.sh` | ~150 lines |
| `test_api.ps1` | ~180 lines |
| `courses.json` | ~20 lines |
| `QUICKSTART.md` | ~30 lines |

**Total:** ~2,900 lines of production-ready code and documentation!

---

## What NOT to Commit to Git

These files are already in `.gitignore`:
- `__pycache__/` - Python cache
- `venv/` or `env/` - Virtual environment
- `.env` - Environment variables
- `*.pyc` - Compiled Python files
- `.DS_Store` - macOS system files
- `*.log` - Log files

---

## Files You Can Safely Delete

These files will be auto-recreated:
- ✅ `courses.json` - Will be recreated on first API call
- ✅ `__pycache__/` - Python will recreate as needed

These files you should NOT delete:
- ❌ `app.py` - Core application
- ❌ `requirements.txt` - Needed for dependencies
- ❌ Any documentation files - Helpful references

---

## Adding New Files

If you add new files to the project:

### Python Modules:
```python
# Import in app.py
from my_module import my_function
```

### Configuration Files:
```
# Add to .gitignore if sensitive
config.ini
secrets.json
```

### Documentation:
```
# Update this file and README.md
new_feature_guide.md
```

### Test Files:
```
# Follow naming convention
test_new_feature.py
```

---

## Summary

- **4 Core Files:** app.py, courses.json, requirements.txt, .gitignore
- **5 Documentation Files:** README.md, QUICKSTART.md, TESTING_GUIDE.md, TEST_CASES.md, FILES_OVERVIEW.md  
- **3 Test Scripts:** test_api.py, test_api.sh, test_api.ps1

**Total: 12 files** providing a complete, production-ready API with comprehensive documentation and testing!

---

## Need Help?

- **To get started:** Read `QUICKSTART.md`
- **To understand the API:** Read `README.md`
- **To test the API:** Read `TESTING_GUIDE.md`
- **To debug issues:** Check Flask logs in terminal
- **To understand code:** Read comments in `app.py`
- **To find specific tests:** Search `TEST_CASES.md`

**Happy Coding! 🚀**
