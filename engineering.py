import math
from typing import Union
from basic import Calculator
from utils import *

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