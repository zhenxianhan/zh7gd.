import pytest
import System
import Staff
import Professor
import Student

def test_drop_student(grading_system):

   grading_system.login('hdjsr7', 'pass1234')
   grading_system.usr.submit_assignment('cloud_computing', 'assignment5','Blahh000hhh', '04/01/20')
   assert grading_system.users['hdjsr7']['courses']['cloud_computing']['assignment5']['submission']=='Blahh000hhh'
   assert grading_system.users['hdjsr7']['courses']['cloud_computing']['assignment5']['ontime']==true



@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
