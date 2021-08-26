'''
1. 현재 주차 가능 자리 수
2. 주차장은 3층짜리
3. 층 별 주차율
'''
class Parking:
    space = []
    car = []

    def __init__(self):
        self.space = [[0]*7 for i in range(3)]

    def parkingRate(self):
        cnt1 = 0
        cnt2 = 0
        cnt3 = 0
        for i in range(3):
            for j in range(7):
                if self.space[i][j]!=0:
                    if i==0:
                        cnt1 += 1
                    elif i==1:
                        cnt2 += 1
                    else:
                        cnt3 += 1
        print("1st Floor Parking Rate : %f"%(cnt1/7*100),"%")
        print("2nd Floor Parking Rate : %f"%(cnt2/7*100),"%")
        print("3rd Floor Parking Rate : %f"%(cnt3/7*100),"%")

    def available(self):
        cnt1 = 0
        cnt2 = 0
        cnt3 = 0
        for i in range(3):
            for j in range(7):
                print("[%d]"%self.space[i][j],end="\t")
                if self.space[i][j]==0:
                    if i==0:
                        cnt1 += 1
                    elif i==1:
                        cnt2 += 1
                    else:
                        cnt3 += 1
            print()
        print("1st Floor Empty : %f"%cnt1)
        print("2nd Floor Empty : %f"%cnt2)
        print("3rd Floor Empty : %f"%cnt3)

    def carSort(self):
        num_sort = sorted(self.car, reverse = False) #item13
        self.car = num_sort

    def menu(self):
        print("[1] 주차하기")
        print("[2] 주차율 확인")
        print("[3] 출차하기")
        print("[4] 차량목록")
        print("[0] 종료하기")

    def run(self):
        while True:
            self.menu()
            sel = int(input(">>> "))
            if sel==1:
                self.available()
                y = int(input("주차할 층수 : "))
                x = int(input("주차할 자리 위치 : "))
                num = int(input("차량 번호 : "))
                if self.space[y-1][x-1] == 0:
                    self.space[y-1][x-1] = num
                    self.car.append(num)
                    print("주차완료.")
                else:
                    print("이미 주차된 자리입니다.")
            elif sel==2:
                self.parkingRate()
            elif sel==3:
                self.available()
                y = int(input("출차할 층수 : "))
                x = int(input("출차할 자리 위치 : "))
                num = int(input("차량 번호 : "))
                if self.space[y-1][x-1]==num:
                    self.space[y-1][x-1] = 0
                    print("출차완료.")
                else:
                    print("잘못된 입력입니다.")
            elif sel==4:
                print("CAR LIST")
                self.carSort()
                print(self.car)
            elif sel==0:      
                break
