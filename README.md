# Calculator Doc ver 2

- Recent Update : 2024.10.08.

[GitHub - skaigroove/calculator: custom calculator for study Python](https://github.com/skaigroove/calculator.git)

# Using Intruction

- 설치

```bash
cd calculator # 패키지 폴더에 들어간 뒤
pip install . # pyproject.toml 파일을 이용해 패키지를 설치합니다
```

- 사용

```bash
export PYTHONPATH=$PYTHONPATH:~/calculator # 파이썬 PATH를 설정해줍니다
python test_using_calc.py # 파이썬 파일을 실행합니다
```

![image.png](Calculator%20Doc%20ver%202%20726b30bd6f754db5978ca351b3a0b9a9/image.png)

# Structure

```nasm
calculator/
├── tests/
│   └── test_calculator.py
├── __init__.py
├── .gitignore
├── LICENSE
├── pyproject.toml
├── README.md
├── requirements.txt
├── basic.py
├── calculator.py
├── complex.py
├── engineering.py
└── utils.py
```

---

# **1. `__init**__.py`

<aside>
💡

필요한 클래스와 함수를 import 하여 패키지 레벨에서 사용할 수 있도록 구현

</aside>

```python
# 상대경로 임포트. 현재 패키지 내의 모듈들을 임포트하여 외부에서 사용할 수 있게 함
from .calculator import * 
from .engineering import EngineeringCalculator
from .basic import Calculator
from .utils import *
```

- `from` 상대경로 `import` 현재 패키지 내의 함수 or 클래스

---

# **2. `calculator**.py`

<aside>
💡

계산기 클래스 정의

</aside>

| class | function | explain |
| --- | --- | --- |
| `Calculator` | `__init__(self)` | 생성자 메서드로 `output` 변수를 초기화. |
| `Calculator` | `option(self,**kwargs)`  | `precision`과 `return_float`가 `kwargs` 안에 있는지 검사하여 관련된 class function 실행. |
| `Calculator` | `return_float(self,**kwargs)` | `return_float`의 value가 **int**인지 **float**인지에 따라, self.output을 알맞게 형변환. |
| `Calculator` | `add(self,*args, **kwargs)` | `args`의 index가 0이라면, `self.output`을 `arg`로 초기화. 나머지 경우는 더해줌. `self.option` 메소드를 실행시켜 `kwargs`가 있을 경우를 처리. |
| `Calculator` | `subtract(self,*args, **kwargs)` | `args`의 index가 0이라면, `self.output`을 `arg`로 초기화. 나머지 경우는 빼줌. `self.option` 메소드를 실행시켜 `kwargs`가 있을 경우를 처리. |
| `Calculator` | `multiply(self,*args, **kwargs)` | `args`의 index가 0이라면, `self.output`을 `arg`로 초기화. 나머지 경우는 곱해줌. `self.option` 메소드를 실행시켜 `kwargs`가 있을 경우를 처리. |
| `Calculator` | `divide(self,*args, **kwargs)` | `args`의 index가 0이라면, `self.output`을 `arg`로 초기화. 나머지 경우는 나눠줌. 단, arg의 값이 0이라면 ValueError를 발생. `self.option` 메소드를 실행시켜 `kwargs`가 있을 경우를 처리. |
| `EngineeringCalculator` | `square_root(self, x : Union[int, float], **kwargs)` | `math.sqrt()` 를 사용하여 root를 계산. `self.option` 메소드를 실행시켜 `kwargs`가 있을 경우를 처리. |
| `EngineeringCalculator` | `power(self, x : Union[int, float], y : Union[int, float], **kwargs)` | `math.pow()` 를 사용하여 power를 계산. (제곱) `self.option` 메소드를 실행시켜 `kwargs`가 있을 경우를 처리. |
| `EngineeringCalculator` | `log(self, x : Union[int, float], base : Union[int, float] = 10 , **kwargs)` | `math.log()` 를 사용하여 log를 계산. `self.option` 메소드를 실행시켜 `kwargs`가 있을 경우를 처리. |
| `EngineeringCalculator` | `ln(self, x : Union[int, float], **kwargs)` | `math.log()` 를 사용하여 log를 계산.`self.option` 메소드를 실행시켜 `kwargs`가 있을 경우를 처리. |
| `EngineeringCalculator` | `sin(self, x : Union[int, float], **kwargs)` | `math.sqrt()` 를 사용하여 ln을 계산. base를 채워주지 않을 시, 자동으로 자연 로그로 계산됨. `self.option` 메소드를 실행시켜 `kwargs`가 있을 경우를 처리. |
| `EngineeringCalculator` | `cos(self, x : Union[int, float], **kwargs)` | `math` 라이브러리의 삼각함수 메소드는 입력을 `radian` 단위로 받으므로, 먼저 `trans_input_unit()`으로 입력 단위를 변환. `math.sin()` 를 사용하여 sin을 계산. `self.option` 메소드를 실행시켜 `kwargs`가 있을 경우를 처리. |
| `EngineeringCalculator` | `tan(self, x : Union[int, float], **kwargs)` | `math` 라이브러리의 삼각함수 메소드는 입력을 `radian` 단위로 받으므로, 먼저 `trans_input_unit()`으로 입력 단위를 변환. `math.cos()` 를 사용하여 cos을 계산. `self.option` 메소드를 실행시켜 `kwargs`가 있을 경우를 처리. |
| `EngineeringCalculator` | `divide(self,*args, **kwargs)` | `math` 라이브러리의 삼각함수 메소드는 입력을 `radian` 단위로 받으므로, 먼저 `trans_input_unit()`으로 입력 단위를 변환. `math.tan()` 를 사용하여 tan을 계산. `self.option` 메소드를 실행시켜 `kwargs`가 있을 경우를 처리. |
| `ComplexCalculator` | `add_complex(self,*args,**kwargs)-> Union[int, float]` | `complex` 자료형 튜플을 입력으로 받아, 합을 계산. `self.option` 메소드를 실행시켜 `kwargs`가 있을 경우를 처리. |
| `ComplexCalculator` | `sub_complex(self,*args,**kwargs)-> Union[int, float]` | `complex` 자료형 튜플을 입력으로 받아, 차을 계산. `self.option` 메소드를 실행시켜 `kwargs`가 있을 경우를 처리. |
| `ComplexCalculator` | `mul_complex(self,*args,**kwargs)-> Union[int, float]` | `complex` 자료형 튜플을 입력으로 받아, 곱을 계산. `self.option` 메소드를 실행시켜 `kwargs`가 있을 경우를 처리. |
|  | `div_complex(self,*args,**kwargs)-> Union[int, float]` | `complex` 자료형 튜플을 입력으로 받아, 나눗셈을 계산. `self.option` 메소드를 실행시켜 `kwargs`가 있을 경우를 처리. |
|  | `magnitude_complex(self,z:complex,**kwargs)-> Union[int, float]` | `complex` 자료형을 입력으로 받아, 절댓값을 계산. `self.option` 메소드를 실행시켜 `kwargs`가 있을 경우를 처리. |
|  | `argument_complex(self,z:complex,**kwargs)-> Union[int, float]` | `complex` 자료형을 입력으로 받아, 편각을 계산. `self.option` 메소드를 실행시켜 `kwargs`가 있을 경우를 처리. |
|  | `option(self,**kwargs) -> None`  | `Override` 된 메소드. `return_polar` 가 `kwargs` 리스트 인자로 들어온다면, 출력을 극 좌표계로 표현해야 할 경우를 처리하는 기능 추가. |

---

# **3. `basic**.py` , `engineering.py` , `complex.py`

<aside>
💡

일반 계산기와 공학용 계산기 기능을 나누어 구현

</aside>

- 각 파일 안의 클래스의 기능은 [`calculator.py`](http://calculator.py) 의 설명과 같음

---

# 4.  `utils.py`

| class | function | explain |
| --- | --- | --- |
| `DivisionByZeroError` | `__init__(self, message="~")` | 0으로 나눌 수 없을 때, 처리할 사용자 정의 예외 클래스를 정의.  |
|  | `convert_to_radians(x : Union[int, float],**kwargs)` | `angle_unit` 의 value를 `kwargs`로부터 받아와, `degree` 단위일 경우 `radian`으로 변환, `radian` 단위일 경우 그대로 설정, 잘못 입력 받을 경우, `ValueError`를 발생. |
|  | `round_result(x,**kwargs)` | 연산 결과와 `precision`을 받아 설정만큼의 소수점 자리만큼 `f-string`으로 포맷해주는 메소드. `precision` 이 0이상의 정수가 아니라면, `ValueError`를 발생시킴. 입력이 극 좌표계 일때의 경우도 따로 처리. |
|  | `convert_to_polar(z,**kwargs) -> tuple` | 연산 결과와 `return_polar` 를 받아 만약 `return_polar`가 **True**라면 극좌표계 인스턴스로 바꾸어 return 한다.  |
| `PolarPoint` | `__init__(self, r, theta)` | 극 좌표계 클래스 생성자 함수. 반지름과 각도(라디안) 클래스 변수를 초기화. |
| `PolarPoint` | `__repr__(self)` | 객체의 문자열 표현을 반환 |

---

# 5. `test_calculator.py`

| test_function | explain |
| --- | --- |
| `test_add` | `Calculator` 인스턴스를 생성하고, 여러 숫자를 더한 결과가 맞는지 확인. |
| `test_sin` | `EngineeringCalculator` 인스턴스를 생성하고, 각도 단위에 따라 sin 값을 확인. |
| `test_add_complex` | `ComplexCalculator` 인스턴스를 생성하고, 두 복소수를 더한 결과를 극 좌표로 반환하는지 확인. |
- 테스트 방법
    
    `루트 디렉토리`에서 `pytest` 명령어로 테스트 파일 실행
    
    ![image.png](Calculator%20Doc%20ver%202%20726b30bd6f754db5978ca351b3a0b9a9/image%201.png)
    
- 결과
    
    ![image.png](Calculator%20Doc%20ver%202%20726b30bd6f754db5978ca351b3a0b9a9/image%202.png)
    

---

# 6. `requirements.txt` , `environments.yml`

- `requirements.txt`
    
    ```python
    pytest # for running test code
    ```
    
    - `requirements.txt` 파일을 사용하여 Python 프로젝트의 의존성을 설치
        
        ```bash
        pip install -r requirements.txt
        ```
        
- `environments.yml` (For Conda Virtual Environment)
    
    ```nasm
    name: calculator
    channels:
      - conda-forge
      - defaults
    dependencies:
      - pytest=7.4.4
      - python=3.9.19
      - wheel=0.44.0
    prefix: /opt/anaconda3/envs/calculator
    ```
    
    - `environments.yml` 파일을 사용해 새로운 conda 환경을 생성하기 위한 커맨드
        
        ```bash
        conda env create -f environment.yml
        ```
        

---