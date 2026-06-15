#!/bin/bash

# CodeCraftHub API - Bash Test Script
# Run this script to quickly test all API endpoints

BASE_URL="http://localhost:5000"
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}CodeCraftHub API - Quick Test Script${NC}"
echo -e "${BLUE}========================================${NC}"

# Check if API is running
echo -e "\n${YELLOW}Checking if API is running...${NC}"
if curl -s "$BASE_URL/" > /dev/null 2>&1; then
    echo -e "${GREEN}✓ API is running${NC}"
else
    echo -e "${RED}✗ API is not running. Please start it with: python app.py${NC}"
    exit 1
fi

# Test 1: Health Check
echo -e "\n${BLUE}Test 1: Health Check${NC}"
curl -s "$BASE_URL/" | python -m json.tool

# Test 2: Get All Courses
echo -e "\n${BLUE}Test 2: Get All Courses${NC}"
curl -s "$BASE_URL/api/courses" | python -m json.tool

# Test 3: Get Statistics
echo -e "\n${BLUE}Test 3: Get Course Statistics${NC}"
curl -s "$BASE_URL/api/courses/stats" | python -m json.tool

# Test 4: Create New Course
echo -e "\n${BLUE}Test 4: Create New Course${NC}"
RESPONSE=$(curl -s -X POST "$BASE_URL/api/courses" \
  -H "Content-Type: application/json" \
  -d '{"name":"Bash Test Course","description":"Created by test script","target_date":"2026-12-31","status":"Not Started"}')
echo "$RESPONSE" | python -m json.tool

# Extract course ID (requires jq or python)
if command -v jq &> /dev/null; then
    COURSE_ID=$(echo "$RESPONSE" | jq -r '.data.id')
    echo -e "${GREEN}Created course with ID: $COURSE_ID${NC}"
    
    # Test 5: Get Specific Course
    echo -e "\n${BLUE}Test 5: Get Course by ID ($COURSE_ID)${NC}"
    curl -s "$BASE_URL/api/courses/$COURSE_ID" | python -m json.tool
    
    # Test 6: Update Course
    echo -e "\n${BLUE}Test 6: Update Course Status${NC}"
    curl -s -X PUT "$BASE_URL/api/courses/$COURSE_ID" \
      -H "Content-Type: application/json" \
      -d '{"status":"In Progress"}' | python -m json.tool
    
    # Test 7: Search Courses
    echo -e "\n${BLUE}Test 7: Search Courses${NC}"
    curl -s "$BASE_URL/api/courses/search?q=bash" | python -m json.tool
    
    # Test 8: Delete Course
    echo -e "\n${BLUE}Test 8: Delete Course${NC}"
    curl -s -X DELETE "$BASE_URL/api/courses/$COURSE_ID" | python -m json.tool
    
    # Test 9: Verify Deletion (should return 404)
    echo -e "\n${BLUE}Test 9: Verify Deletion (should return 404)${NC}"
    curl -s "$BASE_URL/api/courses/$COURSE_ID" | python -m json.tool
else
    echo -e "${YELLOW}Note: Install 'jq' for automatic ID extraction and additional tests${NC}"
fi

# Test 10: Error Scenario - Missing Fields
echo -e "\n${BLUE}Test 10: Error Scenario - Missing Required Field${NC}"
curl -s -X POST "$BASE_URL/api/courses" \
  -H "Content-Type: application/json" \
  -d '{"name":"Incomplete Course"}' | python -m json.tool

# Test 11: Error Scenario - Invalid Status
echo -e "\n${BLUE}Test 11: Error Scenario - Invalid Status${NC}"
curl -s -X POST "$BASE_URL/api/courses" \
  -H "Content-Type: application/json" \
  -d '{"name":"Invalid Course","description":"Test","target_date":"2026-12-31","status":"Pending"}' | python -m json.tool

# Test 12: Error Scenario - Course Not Found
echo -e "\n${BLUE}Test 12: Error Scenario - Course Not Found${NC}"
curl -s "$BASE_URL/api/courses/99999" | python -m json.tool

# Final Statistics
echo -e "\n${BLUE}Final Statistics${NC}"
curl -s "$BASE_URL/api/courses/stats" | python -m json.tool

echo -e "\n${GREEN}========================================${NC}"
echo -e "${GREEN}All tests completed!${NC}"
echo -e "${GREEN}========================================${NC}\n"
