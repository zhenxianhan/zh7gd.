import pytest
import System
import Staff
import Professor
#check grade for class the professor didn't teach
def test_professor_check_grade(grading_system):

   grading_system.login('calyam', '#yeet')
   grades = grading_system.usr.check_grades('hdjsr7','software_engineering')
   assert 'calyam' in grading_system.courses['software_engineering']['professor']

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
