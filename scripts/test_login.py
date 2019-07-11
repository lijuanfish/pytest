import pytest


class TestLogin:

    def test_log1(self):
        print("1")
    def test_log2(self):
        print("2")
    def test_log3(self):
        print("3")
    # @pytest.mark.run(order=1)
    def test_log4(self):
        print("4")
    def test_log5(self):
        print("5")
	def test_log6(self):
        print("5")

if __name__ == '__main__':
    pytest.main(["-s","test_login.py"])
