print("일반 의약품 구매 자판기입니다.")
age = int(input("나이를 입력해주세요.")) 
bill = 0

if age >= 18:
    print("의약품 구매 가능합니다.")
    med = int(input("무슨 약을 구매하시겠습니까? 해열제: 1 소화제: 2 지사제: 3 두통약: 4 \n구매하지 않으신다면 그 외의 버튼을 눌러주세요."))
    if med == 1:
       bill = 2000
       print("해열제를 구입하셨습니다\n")
    if med == 2:
        bill = 1000
        print("소화제를 구입하셨습니다\n")
    if med == 3:
        bill = 1500
        print("지사제를 구입하셨습니다\n")
    if med == 4:
        bill = 3000
        print("두통약을 구입하셨습니다\n")
    else:
        print("의약품 구입을 취소하셨습니다\n")
else:
    print("의약품 구매 불가능합니다.\n")

print(f"발생한 총 금액은 {bill}원 입니다.")