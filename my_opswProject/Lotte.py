# 1. 메뉴판을 출력한다.
# 2. 사용자는 주문하고자 하는 메뉴의 번호를 입력한다.
# 3. 현금을 입력받는다.
# 4. 입력받은 현금과 메뉴가격을 확인해, 영수증을 출력한다.
# 5. 단, 현금이 부족한 경우 "현금이 부족합니다."라는 메세지를 출력한다.

class Lotteria:
    price1 = 8700
    price2 = 6200
    price3 = 1500

    def menu(self):
        print("=== 롯데리아 ===")
        print("1. 불고기 버거 :", self.price1, "원")
        print("2. 새우   버거 :", self.price2, "원")
        print("3. 콜      라 :", self.price3, "원")


    def run(self):
        while True:
            self.menu()
            choice = int(input("메뉴를 선택하세요 : "))
            print("(종료는 0번을 눌러주세요)")
            if choice == 0:
                break
            money = int(input("현금을 입력하세요 : "))

            if choice == 1:
                charge = money - self.price1
            if choice == 2:
                charge = money - self.price2
            if choice == 3:
                charge = money - self.price3
            if choice == 1 or choice == 2 or choice == 3:
                if charge >= 0:
                    print("잔돈 =", charge)
                if charge < 0:
                    print("현금이 부족합니다.")