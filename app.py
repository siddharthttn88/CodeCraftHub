"""
CodeCraftHub - Flask REST API for Course Management
A simple CRUD API for managing learning courses using JSON file storage
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

# Constants
COURSES_FILE = 'courses.json'
ALLOWED_STATUSES = ['Not Started', 'In Progress', 'Completed']


# ==================== Helper Functions ====================

def load_courses():
    """
    Load courses from the JSON file.
    Creates the file automatically if it doesn't exist.
    Returns an empty list if no data exists.
    """
    try:
        # Check if file exists
        if not os.path.exists(COURSES_FILE):
            # Create an empty courses file
            with open(COURSES_FILE, 'w') as f:
                json.dump([], f)
            return []
        
        # Read and return courses from file
        with open(COURSES_FILE, 'r') as f:
            courses = json.load(f)
            return courses if courses else []
    
    except json.JSONDecodeError:
        # Handle corrupted JSON file
        return []
    except Exception as e:
        # Handle any other errors
        print(f"Error loading courses: {str(e)}")
        return []


def save_courses(courses):
    """
    Save all courses to the JSON file.
    Uses pretty JSON formatting for readability.
    """
    try:
        with open(COURSES_FILE, 'w') as f:
            json.dump(courses, f, indent=4)
        return True
    except Exception as e:
        print(f"Error saving courses: {str(e)}")
        return False


def get_next_id(courses):
    """
    Generate the next available numeric ID.
    Returns 1 if no courses exist, otherwise returns max_id + 1.
    """
    if not courses:
        return 1
    
    # Find the maximum ID and add 1
    max_id = max(course['id'] for course in courses)
    return max_id + 1


def validate_course_data(data, is_update=False):
    """
    Validate course data.
    Returns (is_valid, error_message).
    """
    required_fields = ['name', 'description', 'target_date', 'status']
    
    # Check if all required fields are present (for POST requests)
    if not is_update:
        for field in required_fields:
            if field not in data or not data[field]:
                return False, f"Missing required field: {field}"
    
    # Validate status if provided
    if 'status' in data and data['status'] not in ALLOWED_STATUSES:
        return False, f"Invalid status. Allowed values: {', '.join(ALLOWED_STATUSES)}"
    
    return True, None


# ==================== API Endpoints ====================

@app.route('/api/courses', methods=['POST'])
def create_course():
    """
    Create a new course.
    Expects JSON body with: name, description, target_date, status
    Returns HTTP 201 on success.
    """
    try:
        # Get JSON data from request
        data = request.get_json()
        
        if not data:
            return jsonify({
                'success': False,
                'message': 'No data provided'
            }), 400
        
        # Validate input data
        is_valid, error_message = validate_course_data(data)
        if not is_valid:
            return jsonify({
                'success': False,
                'message': error_message
            }), 400
        
        # Load existing courses
        courses = load_courses()
        
        # Create new course object
        new_course = {
            'id': get_next_id(courses),
            'name': data['name'],
            'description': data['description'],
            'target_date': data['target_date'],
            'status': data['status'],
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        # Add to courses list
        courses.append(new_course)
        
        # Save to file
        if not save_courses(courses):
            return jsonify({
                'success': False,
                'message': 'Failed to save course'
            }), 500
        
        return jsonify({
            'success': True,
            'message': 'Course created successfully',
            'data': new_course
        }), 201
    
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Internal server error: {str(e)}'
        }), 500


@app.route('/api/courses', methods=['GET'])
def get_all_courses():
    """
    Get all courses.
    Returns HTTP 200 with list of all courses.
    """
    try:
        courses = load_courses()
        
        return jsonify({
            'success': True,
            'message': 'Courses retrieved successfully',
            'data': courses
        }), 200
    
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Internal server error: {str(e)}'
        }), 500


@app.route('/api/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    """
    Get a specific course by ID.
    Returns HTTP 200 on success, HTTP 404 if not found.
    """
    try:
        courses = load_courses()
        
        # Find course with matching ID
        course = next((c for c in courses if c['id'] == course_id), None)
        
        if not course:
            return jsonify({
                'success': False,
                'message': 'Course not found'
            }), 404
        
        return jsonify({
            'success': True,
            'message': 'Course retrieved successfully',
            'data': course
        }), 200
    
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Internal server error: {str(e)}'
        }), 500


@app.route('/api/courses/<int:course_id>', methods=['PUT'])
def update_course(course_id):
    """
    Update an existing course.
    Returns HTTP 200 on success, HTTP 404 if not found.
    """
    try:
        # Get JSON data from request
        data = request.get_json()
        
        if not data:
            return jsonify({
                'success': False,
                'message': 'No data provided'
            }), 400
        
        # Validate input data (for updates, fields are optional)
        is_valid, error_message = validate_course_data(data, is_update=True)
        if not is_valid:
            return jsonify({
                'success': False,
                'message': error_message
            }), 400
        
        # Load existing courses
        courses = load_courses()
        
        # Find course with matching ID
        course_index = next((i for i, c in enumerate(courses) if c['id'] == course_id), None)
        
        if course_index is None:
            return jsonify({
                'success': False,
                'message': 'Course not found'
            }), 404
        
        # Update course fields
        course = courses[course_index]
        if 'name' in data:
            course['name'] = data['name']
        if 'description' in data:
            course['description'] = data['description']
        if 'target_date' in data:
            course['target_date'] = data['target_date']
        if 'status' in data:
            course['status'] = data['status']
        
        # Save updated courses
        if not save_courses(courses):
            return jsonify({
                'success': False,
                'message': 'Failed to save course'
            }), 500
        
        return jsonify({
            'success': True,
            'message': 'Course updated successfully',
            'data': course
        }), 200
    
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Internal server error: {str(e)}'
        }), 500


@app.route('/api/courses/<int:course_id>', methods=['DELETE'])
def delete_course(course_id):
    """
    Delete a course by ID.
    Returns HTTP 200 on success, HTTP 404 if not found.
    """
    try:
        # Load existing courses
        courses = load_courses()
        
        # Find course with matching ID
        course_index = next((i for i, c in enumerate(courses) if c['id'] == course_id), None)
        
        if course_index is None:
            return jsonify({
                'success': False,
                'message': 'Course not found'
            }), 404
        
        # Remove the course
        deleted_course = courses.pop(course_index)
        
        # Save updated courses
        if not save_courses(courses):
            return jsonify({
                'success': False,
                'message': 'Failed to delete course'
            }), 500
        
        return jsonify({
            'success': True,
            'message': 'Course deleted successfully',
            'data': deleted_course
        }), 200
    
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Internal server error: {str(e)}'
        }), 500


# ==================== Bonus Endpoints ====================

@app.route('/api/courses/stats', methods=['GET'])
def get_stats():
    """
    Get statistics about courses.
    Returns total count and breakdown by status.
    """
    try:
        courses = load_courses()
        
        stats = {
            'total_courses': len(courses),
            'not_started': sum(1 for c in courses if c['status'] == 'Not Started'),
            'in_progress': sum(1 for c in courses if c['status'] == 'In Progress'),
            'completed': sum(1 for c in courses if c['status'] == 'Completed')
        }
        
        return jsonify({
            'success': True,
            'message': 'Statistics retrieved successfully',
            'data': stats
        }), 200
    
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Internal server error: {str(e)}'
        }), 500


@app.route('/api/courses/search', methods=['GET'])
def search_courses():
    """
    Search courses by name or description.
    Query parameter: q (search keyword)
    Case-insensitive matching.
    """
    try:
        # Get search query parameter
        query = request.args.get('q', '').lower()
        
        if not query:
            return jsonify({
                'success': False,
                'message': 'Search query parameter "q" is required'
            }), 400
        
        # Load courses
        courses = load_courses()
        
        # Filter courses that match the query
        results = [
            course for course in courses
            if query in course['name'].lower() or query in course['description'].lower()
        ]
        
        return jsonify({
            'success': True,
            'message': f'Found {len(results)} course(s)',
            'data': results
        }), 200
    
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Internal server error: {str(e)}'
        }), 500


# ==================== Health Check Endpoint ====================

@app.route('/', methods=['GET'])
def health_check():
    """
    Simple health check endpoint.
    """
    return jsonify({
        'success': True,
        'message': 'CodeCraftHub API is running!',
        'version': '1.0.0'
    }), 200


# ==================== Run Application ====================

if __name__ == '__main__':
    # Run the Flask app on port 5000
    # Debug mode is enabled for development (disable in production)
    app.run(debug=True, host='0.0.0.0', port=5000)
