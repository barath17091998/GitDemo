import pytest

@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ["rahul","shetty","rahulshettyacademy.com"]

# need to give tag for a fixture
@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")
    yield       # code after yield in this function will be executed at the end of test execution
    print("I will be executed last")

@pytest.fixture(params=[("chrome","Rahul","Shetty"),("Firefox","shetty"),("Internet Explorer","BB")])
# In params, inside [] is list and inside () is tuple
# request instance is used only when fixtures with params is available
def crossBrowser(request):
    return request.param

