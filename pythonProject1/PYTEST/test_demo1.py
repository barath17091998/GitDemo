# Any pytest file should start with "test_"
# pytest method names should start with "test"
# Any code should be wrapped in method only
# Method names should have sense
import pytest

@pytest.mark.smoke
@pytest.mark.skip
def test_firstProgram():
    print("Hello")

def test_SecondGreetCreditCard():
    print("Good morning")

def test_crossBrowser(crossBrowser):
    print(crossBrowser)

