# Quick Start Guide - CodeCraftHub

## Get Up and Running in 3 Steps

### Step 1: Create Virtual Environment
```bash
python -m venv venv
```

### Step 2: Activate Virtual Environment

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### Step 3: Install Dependencies and Run
```bash
pip install -r requirements.txt
python app.py
```

## Your API is now running at: http://localhost:5000

## Quick Test

Open a new terminal and try:

```bash
# Get all courses
curl http://localhost:5000/api/courses

# Get statistics
curl http://localhost:5000/api/courses/stats
```

## Next Steps

See `README.md` for complete API documentation and all available endpoints.
