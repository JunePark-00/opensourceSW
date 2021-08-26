# 식권 자판기 프로그램
# [1] 관리자
# 1) 식권충전
# 2) 잔돈충전
# 3) 뒤로가기
# [2] 사용자
# 1) 구입
# . 입금 금액 입력
# . 구매 매수 입력
# . 잔돈 출력
# 2) 뒤로가기

# 예)
# 잔돈이 7,600원이다.
# 기계에 5,000원 권이 없으면 1,000원짜리로 7장 출력

class Foodticket:

    moneys  = [50000, 10000, 5000, 1000, 500, 100]      # 출력용
    charges = [    1,     1,    1,    1,   5,  10]      # 잔돈 개수
    
    tickets = 5    # 식권 개수
    price = 3200    # 식권 가격

    def run(self):
        while True:
            print("[1]관리자")
            print("[2]사용자")
            print("[3]종료")

            choice = int(input("메뉴 선택 : "))

            if choice == 1:
                while True:
                    print(self.moneys)
                    print(self.charges)
                    print("1)식권충전")
                    print("2)잔돈충전")
                    print("3)뒤로가기")

                    sel1 = int(input("메뉴 선택 : "))
                    if sel1 == 1:
                        tic = int(input("충전할 식권 개수 입력: "))
                        self.tickets += tic
                        print("충전완료. 현재 식권 개수: ",self.tickets)
                    elif sel1 == 2:
                        print(self.moneys)
                        m_idx = int(input("충전할 금액의 인덱스번호 입력: "))
                        self.charges[m_idx] += 1
                    elif sel1 == 3:
                        break
            elif choice == 2:
                while True:
                    print("1)구입")
                    print("2)뒤로가기")

                    sel2 = int(input("메뉴 선택 : "))
                    if sel2 == 1:
                        buy = int(input("구매 매수: "))
                        if buy < 0 :
                            print("잘못된 입력입니다.")
                            continue
                        print("가격: ",buy*self.price)

                        inMoney = 0
                        my_charge = [0 for i in range(len(self.charges))]
                        print("[현금 투입]")
                        for i in range(len(self.moneys)):
                            print(self.moneys[i],end="")
                            m = int(input(": "))
                            self.charges[i] += m
                            inMoney += m*self.moneys[i]
                            my_charge[i] = m
                        print("투입한 금액: ",inMoney)

                        if inMoney < buy*self.price:
                            print("잔액 부족입니다.")
                            print("환불금액: ",inMoney)
                            for i in range(len(self.charges)):
                                self.charges[i] -= my_charge[i]
                            continue
                        if buy > self.tickets:
                            print("기계의 식권 수가 부족합니다. 죄송합니다.")
                            print("현재 식권 개수: ",self.tickets)
                            print("환불금액: ",inMoney)
                            for i in range(len(self.charges)):
                                self.charges[i] -= my_charge[i]
                            continue
                
                        exMoney = inMoney - buy*self.price
                        jandon = exMoney
                        self.tickets -= buy

                        for i in range(len(self.charges)):
                            em = exMoney//self.moneys[i]
                            if self.charges[i] >= em:
                                self.charges[i] -= em
                                exMoney -= (self.moneys[i]*em)
                            else:
                                if em > 0 :
                                    exMoney -= self.charges[i]*self.moneys[i]
                        if exMoney != 0:
                            print("기계의 잔액이 부족합니다. 죄송합니다.")
                            print("환불금액: ",inMoney)
                            for i in range(len(self.charges)):
                                self.charges[i] -= my_charge[i]
                        else:
                            print("잔돈: ",jandon)
                            print("감사합니다.")
                    
     
                    
                    elif sel2 == 2:
                        break

            elif choice==3:
                break

                
