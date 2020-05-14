import pytest
import System

def test_check_password(grading_system):

   assert grading_system.check_password('saab', 'boomr345' )==True
   assert grading_system.check_password('saab', 'hkjk')==False
   assert grading_system.check_password('saab', '0987433')==False
   assert grading_system.check_password('saab', 'BOOMR')==False




@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

