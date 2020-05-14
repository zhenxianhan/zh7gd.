import pytest
import System
import Staff
import Professor
import Student

def test_check_grade(grading_system):

   grading_system.login('hdjsr7', 'pass1234')
   grades = grading_system.usr.check_grades('software_engineering')
   assert grades[0][1] == 100




@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
