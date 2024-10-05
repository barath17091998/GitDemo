import pytest

@pytest.mark.smoke
@pytest.mark.xfail
def test_firstProgram():
    msg = "Hello"
    assert msg == "Hi", "Test failed because strings do not match"

def test_secondCreditCard():
    a = 4
    b = 6
    assert a+2 == 6, "Addition does not match"

# need to give tag for a fixture
@pytest.fixture()
def setup():
    print("I will be executing first")

# need to give the fixture function "setup" as an argument
def test_fixtureDemo(setup):
    print("i will execute steps in fixture Demo method")



