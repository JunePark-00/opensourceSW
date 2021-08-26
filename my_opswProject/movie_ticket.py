'''
# 모듈로 구현 (파일포함)

. 사용자로부터 좌석번호(index)를 입력받아 예매하는 시스템이다.
. 예매가 완료되면 해당 좌석 값을 1로 변경한다.
. 이미 예매가 완료된 좌석은 재구매할 수 없다.
. 한 좌석당 예매 가격은 12000원이다.
. 프로그램 종료 후, 해당 영화관의 총 매출액을 출력한다.
'''
class Movie:
    seat = []
    money = 0
    index = -1

    def __init__(self,index,money=0,seat=None):
        self.index = index
        self.seat = [0 for i in range(10)]

    def printSeat(self):
        print(self.seat)
        return self.seat

    def ticket(self,index):
        if self.seat[index] != 0:
            print("이미 예매된 좌석입니다.")
            return;
        self.seat[index] = 1
        self.money += 12000

    def menu(self):
        print("[1] 예매하기")
        print("[2] 종료")

    def run(self):
        while True:
            self.printSeat()
            self.menu()
            sel = int(input(": "))
            if sel == 1:
                self.ticket(self.index)
            elif sel == 2:
                print("매출액: ",self.money)
                break
