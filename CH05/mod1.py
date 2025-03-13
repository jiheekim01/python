# 함수 선언 : 네임스페이스 등록 => 실행된다

def add_(a,b):
    return a+b

def sum_(a, b):
    return a + b


#  print('aaaaaaa')

def safe sum(a,b):
    if type(a) != type(b):
    print('타입이 동일하지않다')
    return None
else:
    result = sum_(a,b)
    
    return result

# 위 함수들을 테스트하는 코드 
# mod1 을 단독 실행할 때는 main  이 작동한다
# name__ : 어떻게 실행할 것인지를 저장 변수 
# __name__= '__main__' 이 대입된다

# mod1 이 단독실행될 때만, 테스트 코드가 실행되게 하고 싶다
if__name__== '__main__'
print(sum_(1,6))
print(safe_sum(1,'a'))
# cpu 는 stack 영역만 접근 가능

# import 했을떄는 위 테스트 코드가 실행이 안된다다