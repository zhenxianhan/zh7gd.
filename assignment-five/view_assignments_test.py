import pytest
import System
import Staff
import Professor
import Student

def test_view_assignments(grading_system):

   grading_system.login('hdjsr7', 'pass1234')
   assert grading_system.usr.view_assignments('software_engineering')[0]==['assignment1','1/1/20']

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
