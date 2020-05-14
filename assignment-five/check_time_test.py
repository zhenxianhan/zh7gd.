import pytest
import System
import Staff
import Professor
import Student

def test_drop_student(grading_system):

   grading_system.login('hdjsr7', 'pass1234')
   assert grading_system.usr.check_ontime('04/01/20','05/01/20') == True
   assert grading_system.usr.check_ontime('06/01/20','05/01/20') == False





@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
