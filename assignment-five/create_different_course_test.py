import pytest
import System
import Staff
#test professor cannot create assignment for class they didn't teach.
def test_create_assignment_differernt(grading_system):

   grading_system.login('goggins', 'augurrox')
   grading_system.usr.create_assignment('assignment9', '09/01/20', 'cloud_computing')
   assert   grading_system.courses['cloud_computing']['assignments']['assignment9']['due_date'] == '09/01/20'
   assert 'goggins' in grading_system.courses['cloud_computing']['professor']
   

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
