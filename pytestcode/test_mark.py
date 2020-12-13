import pytest
class Test_demo():
    @pytest.mark.demo
    def test_demo(self):
        a = 5
        b = -1
        assert a != b
        print("我的第一个用例")
    @pytest.mark.smoke
    def test_two(self):
        print("我的第二个用例")