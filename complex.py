import math
import cmath
from engineering import EngineeringCalculator
from typing import Union
from utils import *

class ComplexCalculator(EngineeringCalculator):
    # 복소수 입력들의 합을 구하는 메서드
    def add_complex(self,*args,**kwargs):
        for i, arg in enumerate(args):
            # 첫 연산값을 첫 번째 입력으로 초기화
            if i == 0:
                self.output = arg
                continue
            self.output += arg
        # 지정된 옵션을 처리    
        self.option(**kwargs)
        return self.output
    
    # 복소수 입력들의 차를 구하는 메서드
    def sub_complex(self,*args,**kwargs):
        for i, arg in enumerate(args):
            # 첫 연산값을 첫 번째 입력으로 초기화
            if i == 0:
                self.output = arg
                continue
            self.output -= arg
        # 지정된 옵션을 처리    
        self.option(**kwargs)
        return self.output
        
    # 복소수 입력들의 곱을 구하는 메서드
    def mul_complex(self,*args,**kwargs):
        for i, arg in enumerate(args):
            # 첫 연산값을 첫 번째 입력으로 초기화
            if i == 0:
                self.output = arg
                continue
            self.output *= arg
        # 지정된 옵션을 처리    
        self.option(**kwargs)
        return self.output
        
    # 복소수 입력들의 나눗셈 연산을 하는 메서드
    def div_complex(self,*args,**kwargs):
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
    
    # 복소수의 절댓값 연산을 처리    
    def magnitude_complex(self,z:complex,**kwargs):
        # 절댓값 연산을 처리
        self.output = abs(z)
        # 지정된 옵션을 처리    
        self.option(**kwargs)
        return self.output      
    
    # 복소수의 편각 연산을 처리. 입력은 
    def argument_complex(self,z:complex,**kwargs):
        # 복소수의 편각 계산
        self.output = cmath.phase(z)
        # 지정된 옵션을 처리    
        self.option(**kwargs)
        return self.output
    
    # Override -> 옵션에 따라 처리하도록 경우에 따라 실행 로직을 정의해준 메서드      
    def option(self,**kwargs) -> None:
        if 'return_polar' in kwargs:
            self.output = convert_to_polar(self.output,**kwargs)
        if 'precision' in kwargs: # 소수점 자리를 지정해줬을 경우 처리
            self.output = round_result(self.output,**kwargs)
        if 'return_float' in kwargs: # 리턴 자료형을 지정해줬을 경우 처리
            self.return_float(**kwargs)   