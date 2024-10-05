import math
from typing import Union
from utils import *

# 일반 계산기 클래스 정의
class Calculator:
    
    # 생성자 메서드
    def __init__(self) -> None:
        # 고유 output을 가질 수 있도록 정의
        self.output = 0 
      
    # 옵션에 따라 처리하도록 경우에 따라 실행 로직을 정의해준 메서드      
    def option(self,**kwargs) -> None:
        if 'precision' in kwargs: # 소수점 자리를 지정해줬을 경우 처리
            self.output = round_result(self.output,**kwargs)
        if 'return_float' in kwargs: # 리턴 자료형을 지정해줬을 경우 처리
            self.return_float(**kwargs)
    
    # 옵션에 따라 리턴 자료형을 지정할 수 있는 메서드
    def return_float(self,**kwargs) -> None:
        return_float = kwargs.get('return_float')
        if(return_float == True):
            self.output = float(self.output)
        else: # 항상 정수형
            self.output = int(self.output)
    
    # 입력들의 합을 구하는 메서드     
    def add(self,*args, **kwargs) -> Union[int, float]:
        for i, arg in enumerate(args):
            # 첫 연산값을 첫 번째 입력으로 초기화
            if i == 0:
                self.output = arg
                continue
            self.output += arg
        # 지정된 옵션을 처리    
        self.option(**kwargs)
        return self.output
    
    # 입력들의 차를 구하는 메서드        
    def subtract(self,*args, **kwargs) -> Union[int, float]:
        for i, arg in enumerate(args):
            # 첫 연산값을 첫 번째 입력으로 초기화
            if i == 0: 
                self.output = arg
                continue
            self.output -= arg
        # 지정된 옵션을 처리    
        self.option(**kwargs)
        return self.output
    
    # 입력들의 곱을 구하는 메서드        
    def multiply(self,*args, **kwargs) -> Union[int, float]:
        for i, arg in enumerate(args):
            # 첫 연산값을 첫 번째 입력으로 초기화
            if i == 0:
                self.output = arg
                continue
            self.output *= arg
        # 지정된 옵션을 처리    
        self.option(**kwargs)
        return self.output
    
    # 입력들의 나눗셈 연산을 통해 몫을 구하는 메서드    
    def divide(self,*args, **kwargs) -> Union[int, float]:
        for i, arg in enumerate(args):
            # 첫 연산값을 첫 번째 입력으로 초기화
            if i == 0:
                self.output = arg
                continue
            # 0으로 나누기 에러 처리
            if arg == 0 :
                raise ValueError("0으로 나눌 수 없습니다.")
            self.output /= arg
        # 지정된 옵션을 처리    
        self.option(**kwargs)
        return self.output
    
class EngineeringCalculator(Calculator):
    
    # 루트 연산을 처리하는 메서드                
    def square_root(self, x : Union[int, float], **kwargs) -> Union[int, float]:
        self.output = math.sqrt(x)
        # 지정된 옵션을 처리    
        self.option(**kwargs)
        return self.output
    
    # 제곱 연산을 처리하는 메서드   
    def power(self, x : Union[int, float], y : Union[int, float], **kwargs) -> Union[int, float]:
        self.output = math.pow(x,y)
        # 지정된 옵션을 처리    
        self.option(**kwargs)
        return self.output
    
    # 로그 연산을 처리하는 메서드    
    def log(self, x : Union[int, float], base : Union[int, float] = 10 , **kwargs) -> Union[int, float]:
        self.output = math.log(x,base)
        # 지정된 옵션을 처리    
        self.option(**kwargs)
        return self.output
    
    # 자연로그 연산을 처리하는 메서드    
    def ln(self, x : Union[int, float], **kwargs) -> Union[int, float]:
        self.output = math.log(x) # 자연로그는 log()로 계산함
        # 지정된 옵션을 처리    
        self.option(**kwargs)
        return self.output        
    
    ''' 삼각함수 계산
    각 math 라이브러리의 삼각함수 메소드는
    입력을 'radian' 단위로 받음 '''
    
    # 사인 연산을 처리하는 메서드
    def sin(self, x : Union[int, float], **kwargs) -> Union[int, float]:
        self.output = convert_to_radians(x, **kwargs)
        self.output = math.sin(self.output)
        # 지정된 옵션을 처리    
        self.option(**kwargs)
        return self.output    
    
    # 코사인 연산을 처리하는 메서드
    def cos(self, x : Union[int, float], **kwargs) -> Union[int, float]:
        self.output = convert_to_radians(x,**kwargs)
        self.output = math.cos(self.output)
        # 지정된 옵션을 처리    
        self.option(**kwargs)
        return self.output    
    
    # 탄젠트 연산을 처리하는 메서드
    def tan(self, x : Union[int, float], **kwargs) -> Union[int, float]:
        self.output = convert_to_radians(x,**kwargs)
        self.output = math.tan(self.output)
        # 지정된 옵션을 처리    
        self.option(**kwargs)
        return self.output    
        
    # 오버라이드, DivisionByZeroError를 발생
    def divide(self,*args, **kwargs) -> Union[int, float]:
        for i, arg in enumerate(args):
            # 첫 연산값을 첫 번째 입력으로 초기화
            if i == 0:
                self.output = arg
                continue
            # 나누는 값이 0이라면 사용자 정의 에러를 발생
            if arg == 0:
                raise DivisionByZeroError()
            self.output /= arg
        # 지정된 옵션을 처리    
        self.option(**kwargs)
        return self.output

# 외부에서 from calculator import * 를 사용할 때 리스트에 포함된 클래스와 메소드들만 명시적으로 가져올 수 있도록 만듦
__all__ = ['Calculator', 'EngineeringCalculator'] 

if __name__ == '__main__':
    # 간단한 데모 코드
    calc = Calculator()
    eng_calc = EngineeringCalculator()

    print("Basic Calculator Demo:")
    print(calc.add(1, 2, 3))
    print(calc.multiply(2, 4, 6))

    print("\nEngineering Calculator Demo:")
    print(eng_calc.square_root(16))
    print(eng_calc.sin(30, angle_unit='degree'))

