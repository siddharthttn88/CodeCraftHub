"""
CodeCraftHub API - Automated Test Script
Run this script to automatically test all API endpoints
"""

import requests
import json
from datetime import datetime

# Configuration
BASE_URL = "http://localhost:5000"
COLORS = {
    'GREEN': '\033[92m',
    'RED': '\033[91m',
    'YELLOW': '\033[93m',
    'BLUE': '\033[94m',
    'END': '\033[0m'
}

# Test counters
tests_passed = 0
tests_failed = 0


def print_test_header(test_name):
    """Print a formatted test header"""
    print(f"\n{COLORS['BLUE']}{'='*60}{COLORS['END']}")
    print(f"{COLORS['BLUE']}Test: {test_name}{COLORS['END']}")
    print(f"{COLORS['BLUE']}{'='*60}{COLORS['END']}")


def print_success(message):
    """Print success message"""
    global tests_passed
    tests_passed += 1
    print(f"{COLORS['GREEN']}✓ PASS: {message}{COLORS['END']}")


def print_failure(message):
    """Print failure message"""
    global tests_failed
    tests_failed += 1
    print(f"{COLORS['RED']}✗ FAIL: {message}{COLORS['END']}")


def print_info(message):
    """Print info message"""
    print(f"{COLORS['YELLOW']}ℹ INFO: {message}{COLORS['END']}")


def test_health_check():
    """Test 1: Health Check Endpoint"""
    print_test_header("Health Check")
    
    try:
        response = requests.get(f"{BASE_URL}/")
        print_info(f"Status Code: {response.status_code}")
        print_info(f"Response: {json.dumps(response.json(), indent=2)}")
        
        if response.status_code == 200 and response.json()['success']:
            print_success("Health check passed")
        else:
            print_failure("Health check failed")
    except Exception as e:
        print_failure(f"Health check error: {str(e)}")


def test_get_all_courses():
    """Test 2: Get All Courses"""
    print_test_header("Get All Courses")
    
    try:
        response = requests.get(f"{BASE_URL}/api/courses")
        print_info(f"Status Code: {response.status_code}")
        
        data = response.json()
        if response.status_code == 200 and data['success']:
            print_success(f"Retrieved {len(data['data'])} courses")
            print_info(f"Courses: {json.dumps(data['data'], indent=2)}")
        else:
            print_failure("Failed to retrieve courses")
    except Exception as e:
        print_failure(f"Get all courses error: {str(e)}")


def test_create_course_success():
    """Test 3: Create Course - Success"""
    print_test_header("Create Course - Success")
    
    course_data = {
        "name": "Automated Test Course",
        "description": "This course was created by the automated test script",
        "target_date": "2026-12-31",
        "status": "Not Started"
    }
    
    try:
        response = requests.post(
            f"{BASE_URL}/api/courses",
            json=course_data
        )
        print_info(f"Status Code: {response.status_code}")
        print_info(f"Response: {json.dumps(response.json(), indent=2)}")
        
        if response.status_code == 201 and response.json()['success']:
            course_id = response.json()['data']['id']
            print_success(f"Course created successfully with ID: {course_id}")
            return course_id
        else:
            print_failure("Failed to create course")
            return None
    except Exception as e:
        print_failure(f"Create course error: {str(e)}")
        return None


def test_create_course_missing_field():
    """Test 4: Create Course - Missing Required Field"""
    print_test_header("Create Course - Missing Required Field")
    
    course_data = {
        "name": "Incomplete Course",
        "description": "Missing target_date and status"
    }
    
    try:
        response = requests.post(
            f"{BASE_URL}/api/courses",
            json=course_data
        )
        print_info(f"Status Code: {response.status_code}")
        print_info(f"Response: {json.dumps(response.json(), indent=2)}")
        
        if response.status_code == 400 and not response.json()['success']:
            print_success("Correctly rejected incomplete course data")
        else:
            print_failure("Should have rejected incomplete course data")
    except Exception as e:
        print_failure(f"Test error: {str(e)}")


def test_create_course_invalid_status():
    """Test 5: Create Course - Invalid Status"""
    print_test_header("Create Course - Invalid Status")
    
    course_data = {
        "name": "Invalid Status Course",
        "description": "Testing invalid status value",
        "target_date": "2026-12-31",
        "status": "Pending"  # Invalid status
    }
    
    try:
        response = requests.post(
            f"{BASE_URL}/api/courses",
            json=course_data
        )
        print_info(f"Status Code: {response.status_code}")
        print_info(f"Response: {json.dumps(response.json(), indent=2)}")
        
        if response.status_code == 400 and not response.json()['success']:
            print_success("Correctly rejected invalid status")
        else:
            print_failure("Should have rejected invalid status")
    except Exception as e:
        print_failure(f"Test error: {str(e)}")


def test_get_course_by_id(course_id):
    """Test 6: Get Course by ID"""
    print_test_header("Get Course by ID")
    
    try:
        response = requests.get(f"{BASE_URL}/api/courses/{course_id}")
        print_info(f"Status Code: {response.status_code}")
        print_info(f"Response: {json.dumps(response.json(), indent=2)}")
        
        if response.status_code == 200 and response.json()['success']:
            print_success(f"Retrieved course ID {course_id}")
        else:
            print_failure(f"Failed to retrieve course ID {course_id}")
    except Exception as e:
        print_failure(f"Get course by ID error: {str(e)}")


def test_get_course_not_found():
    """Test 7: Get Course - Not Found"""
    print_test_header("Get Course - Not Found")
    
    try:
        response = requests.get(f"{BASE_URL}/api/courses/99999")
        print_info(f"Status Code: {response.status_code}")
        print_info(f"Response: {json.dumps(response.json(), indent=2)}")
        
        if response.status_code == 404 and not response.json()['success']:
            print_success("Correctly returned 404 for non-existent course")
        else:
            print_failure("Should have returned 404")
    except Exception as e:
        print_failure(f"Test error: {str(e)}")


def test_update_course(course_id):
    """Test 8: Update Course"""
    print_test_header("Update Course")
    
    update_data = {
        "status": "In Progress"
    }
    
    try:
        response = requests.put(
            f"{BASE_URL}/api/courses/{course_id}",
            json=update_data
        )
        print_info(f"Status Code: {response.status_code}")
        print_info(f"Response: {json.dumps(response.json(), indent=2)}")
        
        if response.status_code == 200 and response.json()['success']:
            print_success(f"Updated course ID {course_id}")
        else:
            print_failure(f"Failed to update course ID {course_id}")
    except Exception as e:
        print_failure(f"Update course error: {str(e)}")


def test_update_course_not_found():
    """Test 9: Update Course - Not Found"""
    print_test_header("Update Course - Not Found")
    
    update_data = {
        "status": "Completed"
    }
    
    try:
        response = requests.put(
            f"{BASE_URL}/api/courses/99999",
            json=update_data
        )
        print_info(f"Status Code: {response.status_code}")
        print_info(f"Response: {json.dumps(response.json(), indent=2)}")
        
        if response.status_code == 404 and not response.json()['success']:
            print_success("Correctly returned 404 for non-existent course")
        else:
            print_failure("Should have returned 404")
    except Exception as e:
        print_failure(f"Test error: {str(e)}")


def test_search_courses():
    """Test 10: Search Courses"""
    print_test_header("Search Courses")
    
    try:
        response = requests.get(f"{BASE_URL}/api/courses/search?q=test")
        print_info(f"Status Code: {response.status_code}")
        
        data = response.json()
        if response.status_code == 200 and data['success']:
            print_success(f"Search completed: {data['message']}")
            print_info(f"Results: {json.dumps(data['data'], indent=2)}")
        else:
            print_failure("Search failed")
    except Exception as e:
        print_failure(f"Search error: {str(e)}")


def test_search_courses_missing_query():
    """Test 11: Search Courses - Missing Query"""
    print_test_header("Search Courses - Missing Query")
    
    try:
        response = requests.get(f"{BASE_URL}/api/courses/search")
        print_info(f"Status Code: {response.status_code}")
        print_info(f"Response: {json.dumps(response.json(), indent=2)}")
        
        if response.status_code == 400 and not response.json()['success']:
            print_success("Correctly rejected search without query parameter")
        else:
            print_failure("Should have rejected search without query")
    except Exception as e:
        print_failure(f"Test error: {str(e)}")


def test_get_statistics():
    """Test 12: Get Statistics"""
    print_test_header("Get Course Statistics")
    
    try:
        response = requests.get(f"{BASE_URL}/api/courses/stats")
        print_info(f"Status Code: {response.status_code}")
        
        data = response.json()
        if response.status_code == 200 and data['success']:
            stats = data['data']
            print_success("Statistics retrieved successfully")
            print_info(f"Total Courses: {stats['total_courses']}")
            print_info(f"Not Started: {stats['not_started']}")
            print_info(f"In Progress: {stats['in_progress']}")
            print_info(f"Completed: {stats['completed']}")
        else:
            print_failure("Failed to retrieve statistics")
    except Exception as e:
        print_failure(f"Get statistics error: {str(e)}")


def test_delete_course(course_id):
    """Test 13: Delete Course"""
    print_test_header("Delete Course")
    
    try:
        response = requests.delete(f"{BASE_URL}/api/courses/{course_id}")
        print_info(f"Status Code: {response.status_code}")
        print_info(f"Response: {json.dumps(response.json(), indent=2)}")
        
        if response.status_code == 200 and response.json()['success']:
            print_success(f"Deleted course ID {course_id}")
        else:
            print_failure(f"Failed to delete course ID {course_id}")
    except Exception as e:
        print_failure(f"Delete course error: {str(e)}")


def test_delete_course_not_found():
    """Test 14: Delete Course - Not Found"""
    print_test_header("Delete Course - Not Found")
    
    try:
        response = requests.delete(f"{BASE_URL}/api/courses/99999")
        print_info(f"Status Code: {response.status_code}")
        print_info(f"Response: {json.dumps(response.json(), indent=2)}")
        
        if response.status_code == 404 and not response.json()['success']:
            print_success("Correctly returned 404 for non-existent course")
        else:
            print_failure("Should have returned 404")
    except Exception as e:
        print_failure(f"Test error: {str(e)}")


def print_summary():
    """Print test summary"""
    print(f"\n{COLORS['BLUE']}{'='*60}{COLORS['END']}")
    print(f"{COLORS['BLUE']}TEST SUMMARY{COLORS['END']}")
    print(f"{COLORS['BLUE']}{'='*60}{COLORS['END']}")
    
    total_tests = tests_passed + tests_failed
    
    print(f"\nTotal Tests: {total_tests}")
    print(f"{COLORS['GREEN']}Passed: {tests_passed}{COLORS['END']}")
    print(f"{COLORS['RED']}Failed: {tests_failed}{COLORS['END']}")
    
    if tests_failed == 0:
        print(f"\n{COLORS['GREEN']}🎉 All tests passed!{COLORS['END']}")
    else:
        success_rate = (tests_passed / total_tests) * 100
        print(f"\n{COLORS['YELLOW']}Success Rate: {success_rate:.1f}%{COLORS['END']}")


def main():
    """Run all tests"""
    print(f"\n{COLORS['BLUE']}{'='*60}{COLORS['END']}")
    print(f"{COLORS['BLUE']}CodeCraftHub API - Automated Test Suite{COLORS['END']}")
    print(f"{COLORS['BLUE']}{'='*60}{COLORS['END']}")
    print(f"\nBase URL: {BASE_URL}")
    print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Check if API is running
    try:
        requests.get(f"{BASE_URL}/", timeout=2)
    except requests.exceptions.ConnectionError:
        print_failure("Cannot connect to API. Make sure the Flask server is running!")
        print_info("Run: python app.py")
        return
    
    # Run all tests
    test_health_check()
    test_get_all_courses()
    
    # Create a test course and use its ID for subsequent tests
    course_id = test_create_course_success()
    
    test_create_course_missing_field()
    test_create_course_invalid_status()
    
    if course_id:
        test_get_course_by_id(course_id)
        test_update_course(course_id)
    
    test_get_course_not_found()
    test_update_course_not_found()
    
    test_search_courses()
    test_search_courses_missing_query()
    test_get_statistics()
    
    if course_id:
        test_delete_course(course_id)
    
    test_delete_course_not_found()
    
    # Print summary
    print_summary()
    
    print(f"\n{COLORS['BLUE']}{'='*60}{COLORS['END']}")
    print(f"Completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{COLORS['BLUE']}{'='*60}{COLORS['END']}\n")


if __name__ == "__main__":
    main()
