from calculator import *

def test_add():
    # Calculator 인스턴스를 생성하고, 여러 숫자를 더한 결과가 15.00인지 확인합니다.
    calc = Calculator()
    assert calc.add(1,2,3,4,5,precision=2,return_float=True) == 15.00

def test_sin():
    # EngineeringCalculator 인스턴스를 생성하고, 각도 단위에 따라 sin 값을 확인합니다.
    eng_calc = EngineeringCalculator()
    assert eng_calc.sin(30, angle_unit='degree')  # 30도에 대한 sin 값
    assert eng_calc.sin(60, angle_unit='radian')  # 60라디안에 대한 sin 값
    
def test_add_complex():
    # ComplexCalculator 인스턴스를 생성하고, 두 복소수를 더한 결과를 극좌표로 반환하는지 확인합니다.
    complex_calc = ComplexCalculator()
    assert complex_calc.add_complex(1+2j, 3+4j, return_polar=True, precision=2)
