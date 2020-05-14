import pytest
import System
import Staff
import Professor

def test_drop_student(grading_system):

   grading_system.login('goggins', 'augurrox')
   grading_system.usr.drop_student('hdjsr7', 'databases')
   assert 'databases' not in grading_system.users['hdjsr7']['courses']

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
