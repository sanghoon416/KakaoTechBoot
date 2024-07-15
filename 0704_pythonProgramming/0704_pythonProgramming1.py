## 사용자로부터 이름, 나이, 이메일을 입력받아 딕셔너리에 저장하는 프로그램을 작성하세요.
## 나이와 이메일의 형식을 검증하고, 잘못된 입력이 있으면 예외 처리를 하세요.

def validate_age(age):
    if age.isdigit():
       age = int(age)
       if 0 < age and age <= 100:
         return age       
    return -1

def validate_email(email):
    for i in email:
       if i == '@':
          return 0
    return -1

name = input()
age = input(int)
email = input()

if validate_age(age) == -1:
  raise ValueError("나이의 형식이 잘 못 되었습니다")

if validate_email(email) == -1:
  raise ValueError("email의 형식이 잘 못 되었습니다")

print(f"이름 :" + name)
print(f"나이 :" + age)
print(f"메일 :" + email)