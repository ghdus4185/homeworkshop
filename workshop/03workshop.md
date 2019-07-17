# 03 workshop

## Palindrome은 앞에서부터 읽었을 때와 뒤에서부터 읽었을 때 같은 단어를 뜻한다. 따라서, ‘a’ ‘nan’ ’토마토’ 모두 palindrome에 해당합니다. 단어를 입력받아 Palindrome을 검증하고 True나 False를 리턴하는 함수 palindrome(word)를 만들어보세요.

```python
a = input()
def Palin(a):
    for i in range(len(a)//2):
        if not a[0+i] == a[-1-i]:
            return False
    return True

print(Palin(a))

#a = 'study'
#def palin(a):
#    result = ''
#    for i in range(len(a)):
#        result += a[-1-i]
#    print(result)
#palin(a)
#빈 스트링에 거꾸로 채우기
```


