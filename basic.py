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