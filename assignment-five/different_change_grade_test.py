import pytest
import System
import Staff
#teacher canot change grade of class they don't teach
def test_different_change_grade(grading_system):

   grading_system.login('saab', 'boomr345')
   grading_system.usr.change_grade('yted91', 'software_engineering', 'assignment1', 17)
   assert grading_system.users['yted91']['courses']['software_engineering']['assignment1']['grade'] == 17


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
