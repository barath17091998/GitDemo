import pytest

@pytest.mark.usefixtures('setup')
class TestExample:

# need to give the fixture function "setup" as an argument
    def test_fixtureDemo(self):
        print("i will execute steps in fixture Demo method")

    def test_fixtureDemo1(self):
        print("i will execute steps in fixture Demo1 method")

    def test_fixtureDemo2(self):
        print("i will execute steps in fixture Demo2 method")

    def test_fixtureDemo3(self):
        print("i will execute steps in fixture Demo3 method")
