# 04 workshop

## 양의 정수 x를 입력 받아 제곱근의 근사값을 반환하는 함수를 작성하세요. 단, sqrt() 사용 금지

```python
def bi_section(x):
    left = 1
    right = x
    result = 1
    
    import math
    while not math.isclose(result**2,x):  # isclose는 어느정도 근사치에 들어오면 같다라고 반환, 아니면 차가 어느정도 이하냐로 조건 설정
        result = (left+right)/2    
        if result **2 < x:
            left = result
        else:
            right = result
    return result
bi_section(2)
```


