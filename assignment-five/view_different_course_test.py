import pytest
import System
import Staff
import Professor
import Student
#student should watch assignment for class they are not in.
def test_view_assignments(grading_system):

   grading_system.login('hdjsr7', 'pass1234')
   grading_system.usr.view_assignments('comp_sci')
   assert 'comp_sci' in grading_system.users['hdjsr7']['courses']

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
