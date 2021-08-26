# 기억력 게임 : 클래스 + 변수
# 1. front 배열 카드 10장을 섞는다.
# 2. front 배열에서 같은 카드를 골라 카드의 위치를 입력한다.
# 3. 선택한 2장의 카드가 같은 카드이면, back 배열에 표시한다.
# 4. 모든 카드가 뒤집히면(back배열의 0이 사라지면) 게임은 종료된다.
import random
class Memory:
    front = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
    back = [0 for i in range(10)]

    cnt = 0

    def run(self):
        for i in range(1000):
            r = random.randint(0,9)
            temp = self.front[0]
            self.front[0] = self.front[r]
            self.front[r] = temp
            
        while True:
            print(self.front)
            print(self.back)

            cnt = 0
            for i in range(10):
                if self.back[i] == 0:
                    cnt = 1
                    break
            if cnt == 0:
                print("게임종료")
                break

            c1 = int(input("c1: "))
            c2 = int(input("c2: "))
            print("If you wanna break, type '100'")
            if c2==100:
                break

            if self.front[c1] == self.front[c2]:
                self.back[c1] = self.front[c1]
                self.back[c2] = self.front[c2]
            else:
                print("땡")