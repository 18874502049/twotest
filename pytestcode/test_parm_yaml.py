import pytest
import yaml
from pythoncode.calculator import Calculator

def get_datas():
    with open("./data.yaml") as f:
        datas = yaml.safe_load(f)
        print(datas)
        add_datas = datas["datas"]
        add_ids = datas["myid"]
        return [add_datas,add_ids]
class TestCalc:
    def setup_class(self):
        self.cal = Calculator()
        print("开始计算")
    def teardown_class(self):
        print("结束计算")

    @pytest.mark.parametrize("a,b,expect",
                            get_datas()[0],
                             ids=get_datas()[1])
    def test_add(self,a,b,expect):
        assert expect == self.cal.add(a,b)