import pytest
from pythoncode.calculator import Calculator

class TestCalc:
    def setup_class(self):
        self.cal = Calculator()
        print("开始计算")
    def teardown_class(self):
        print("结束计算")

    @pytest.mark.parametrize("a,b,expect",[
        (3,5,8),(-1,-2,-3),(100,300,400)
    ],ids=["int","minus","bigint"])
    def test_add(self,a,b,expect):
        assert expect == self.cal.add(a,b)

    @pytest.mark.parametrize("a,b,expect", [
        (3, 5, -2), (-1, -2, 1), (100, 300, -200)
    ], ids=["int", "minus", "bigint"])
    def test_sub(self,a,b,expect):
        assert expect == self.cal.sub(a,b)

    @pytest.mark.parametrize("a,b,expect", [
        (3, 5, 15), (-1, -2, 2), (100, 300, 30000)
    ], ids=["int", "minus", "bigint"])
    def test_mul(self, a, b, expect):
        assert expect == self.cal.mul(a, b)

    @pytest.mark.parametrize("a,b,expect", [
        (3, 5, 0.6), (-1, -2, 0.5), (100, 50, 2.0)
    ], ids=["int", "minus", "bigint"])
    def test_mod(self, a, b, expect):
        assert expect == self.cal.mod(a, b)