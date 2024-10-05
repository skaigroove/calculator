import math
from typing import Union

# 사용자 정의 예외 클래스 (0으로 나눌 수 없음)
class DivisionByZeroError(Exception):
    def __init__(self, message="0으로 나눌 수 없습니다.") -> None:
        self.message = message
        super().__init__(self.message)
        
# degree 단위를 radian 단위로 환산해주는 메소드 
def convert_to_radians(x : Union[int, float],**kwargs) -> None:
    unit = kwargs.get('angle_unit')    
    if unit == 'degree': # degree 단위일 경우, radian로 변환
        return float(math.radians(x))
    elif unit == 'radian': # radian 단위일 경우, 그대로
        return x
    else: # 잘못 입력받을 경우 에러 메세지 출력
        raise ValueError("유효하지 않은 단위입니다. 'degree' 또는 'radian'을 입력하세요.")
 
# 연산 결과와 precision을 받아 설정만큼의 소수점 자리만큼 f-string으로 포맷해주는 메소드 
def round_result(x,**kwargs) -> None:
    precision = kwargs.get('precision')
    if precision is not None:
        if not isinstance(precision, int) or precision < 0:
            raise ValueError("precision은 0 이상의 정수여야 합니다.")
        # 소수점 자릿수 제한을 위해 float 형으로 변환
        # 첫번째 인수(0)을 소수점 이하 precision 자리만큼 포맷
        format_str = f"{{0:.{precision}f}}" 
        return format_str.format(x)

# from utils import * 사용 시, 리스트에 포함된 클래스와 메소드들만 명시적으로 가져올 수 있도록 만듦
__all__ = ['DivisionByZeroError', 'convert_to_radians', 'round_result'] 