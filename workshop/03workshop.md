# 03 workshop

## Palindrome은 앞에서부터 읽었을 때와 뒤에서부터 읽었을 때 같은 단어를 뜻한다. 따라서, ‘a’ ‘nan’ ’토마토’ 모두 palindrome에 해당합니다. 단어를 입력받아 Palindrome을 검증하고 True나 False를 리턴하는 함수 palindrome(word)를 만들어보세요.

```python
# 앞이랑 뒤랑 비교하면서 가운데까지 for문이 도는 것
a = input()
def Palin(a):
    for i in range(len(a)//2):
        if not a[0+i] == a[-1-i]:
            return False
    return True

print(Palin(a))


#단어를 뒤집어서 비교하기
def palindrome(word):
    result = ''
    for i in word:
        result = i + result
    if word == result:
        return True
    else:
        return False
palindrome('토마토')


#빈 스트링에 거꾸로 채우기
a = 'study'
def palin(a):
    result = ''
    for i in range(len(a)):
        result += a[-1-i]
    print(result)
palin(a)

#선생님
def palindrome(word):
    for i in range(len(word)//2):
        if not word[i] == word[-i-1]:
            return False
    return True

print(palindrome('토마토라'))

#슬라이싱을 이용한 뒤집어서 비교한 코드
def palindrome(word):
    return word == word[::-1]
palindrome('토마토가')

```


