import pytest
import System
import Staff

def test_create_assignment(grading_system):

   grading_system.login('cmhbf5', 'bestTA')
   grading_system.usr.create_assignment('assignment8', '08/01/20', 'cloud_computing')
   assert grading_system.courses['cloud_computing']['assignments']['assignment8']['due_date'] == '08/01/20'

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
