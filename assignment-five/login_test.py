import pytest
import System

def test_login(grading_system):

   grading_system.login('saab', 'boomr345' )
   assert grading_system.usr.name=='saab'
   assert grading_system.usr.password=='boomr345'


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
