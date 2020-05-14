import pytest
import System
import Staff
import Professor

def test_add_student(grading_system):

   grading_system.login('goggins', 'augurrox')
   grading_system.usr.add_student('yted91', 'databases')
   assert 'databases' in grading_system.users['yted91']['courses']

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
