# CodeCraftHub API - PowerShell Test Script
# Run this script to quickly test all API endpoints

$BaseUrl = "http://localhost:5000"

Write-Host "========================================" -ForegroundColor Blue
Write-Host "CodeCraftHub API - Quick Test Script" -ForegroundColor Blue
Write-Host "========================================" -ForegroundColor Blue

# Check if API is running
Write-Host "`nChecking if API is running..." -ForegroundColor Yellow
try {
    $null = Invoke-RestMethod -Uri "$BaseUrl/" -Method Get -TimeoutSec 2
    Write-Host "✓ API is running" -ForegroundColor Green
} catch {
    Write-Host "✗ API is not running. Please start it with: python app.py" -ForegroundColor Red
    exit 1
}

# Test 1: Health Check
Write-Host "`nTest 1: Health Check" -ForegroundColor Blue
$response = Invoke-RestMethod -Uri "$BaseUrl/" -Method Get
$response | ConvertTo-Json -Depth 10

# Test 2: Get All Courses
Write-Host "`nTest 2: Get All Courses" -ForegroundColor Blue
$courses = Invoke-RestMethod -Uri "$BaseUrl/api/courses" -Method Get
$courses | ConvertTo-Json -Depth 10

# Test 3: Get Statistics
Write-Host "`nTest 3: Get Course Statistics" -ForegroundColor Blue
$stats = Invoke-RestMethod -Uri "$BaseUrl/api/courses/stats" -Method Get
$stats | ConvertTo-Json -Depth 10

# Test 4: Create New Course
Write-Host "`nTest 4: Create New Course" -ForegroundColor Blue
$newCourse = @{
    name = "PowerShell Test Course"
    description = "Created by PowerShell test script"
    target_date = "2026-12-31"
    status = "Not Started"
} | ConvertTo-Json

$response = Invoke-RestMethod -Uri "$BaseUrl/api/courses" -Method Post -Body $newCourse -ContentType "application/json"
$response | ConvertTo-Json -Depth 10

$courseId = $response.data.id
Write-Host "Created course with ID: $courseId" -ForegroundColor Green

# Test 5: Get Specific Course
Write-Host "`nTest 5: Get Course by ID ($courseId)" -ForegroundColor Blue
$course = Invoke-RestMethod -Uri "$BaseUrl/api/courses/$courseId" -Method Get
$course | ConvertTo-Json -Depth 10

# Test 6: Update Course
Write-Host "`nTest 6: Update Course Status" -ForegroundColor Blue
$updateData = @{
    status = "In Progress"
} | ConvertTo-Json

$response = Invoke-RestMethod -Uri "$BaseUrl/api/courses/$courseId" -Method Put -Body $updateData -ContentType "application/json"
$response | ConvertTo-Json -Depth 10

# Test 7: Search Courses
Write-Host "`nTest 7: Search Courses" -ForegroundColor Blue
$searchResults = Invoke-RestMethod -Uri "$BaseUrl/api/courses/search?q=powershell" -Method Get
$searchResults | ConvertTo-Json -Depth 10

# Test 8: Delete Course
Write-Host "`nTest 8: Delete Course" -ForegroundColor Blue
$response = Invoke-RestMethod -Uri "$BaseUrl/api/courses/$courseId" -Method Delete
$response | ConvertTo-Json -Depth 10

# Test 9: Verify Deletion (should return 404)
Write-Host "`nTest 9: Verify Deletion (should return 404)" -ForegroundColor Blue
try {
    $response = Invoke-RestMethod -Uri "$BaseUrl/api/courses/$courseId" -Method Get
    $response | ConvertTo-Json -Depth 10
} catch {
    Write-Host "✓ Correctly returned 404 - Course not found" -ForegroundColor Green
}

# Test 10: Error Scenario - Missing Fields
Write-Host "`nTest 10: Error Scenario - Missing Required Field" -ForegroundColor Blue
$incompleteCourse = @{
    name = "Incomplete Course"
} | ConvertTo-Json

try {
    $response = Invoke-RestMethod -Uri "$BaseUrl/api/courses" -Method Post -Body $incompleteCourse -ContentType "application/json"
    $response | ConvertTo-Json -Depth 10
} catch {
    $errorResponse = $_.ErrorDetails.Message | ConvertFrom-Json
    $errorResponse | ConvertTo-Json -Depth 10
}

# Test 11: Error Scenario - Invalid Status
Write-Host "`nTest 11: Error Scenario - Invalid Status" -ForegroundColor Blue
$invalidCourse = @{
    name = "Invalid Course"
    description = "Test"
    target_date = "2026-12-31"
    status = "Pending"
} | ConvertTo-Json

try {
    $response = Invoke-RestMethod -Uri "$BaseUrl/api/courses" -Method Post -Body $invalidCourse -ContentType "application/json"
    $response | ConvertTo-Json -Depth 10
} catch {
    $errorResponse = $_.ErrorDetails.Message | ConvertFrom-Json
    $errorResponse | ConvertTo-Json -Depth 10
}

# Test 12: Error Scenario - Course Not Found
Write-Host "`nTest 12: Error Scenario - Course Not Found" -ForegroundColor Blue
try {
    $response = Invoke-RestMethod -Uri "$BaseUrl/api/courses/99999" -Method Get
    $response | ConvertTo-Json -Depth 10
} catch {
    $errorResponse = $_.ErrorDetails.Message | ConvertFrom-Json
    $errorResponse | ConvertTo-Json -Depth 10
}

# Final Statistics
Write-Host "`nFinal Statistics" -ForegroundColor Blue
$finalStats = Invoke-RestMethod -Uri "$BaseUrl/api/courses/stats" -Method Get
$finalStats | ConvertTo-Json -Depth 10

Write-Host "`n========================================" -ForegroundColor Green
Write-Host "All tests completed!" -ForegroundColor Green
Write-Host "========================================`n" -ForegroundColor Green
