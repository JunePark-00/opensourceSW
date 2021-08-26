# 모듈로 구현
'''
. 인원 및 캐릭터/결과값 설정 (입력받음)
. 사다리 출력
. 랜덤 인덱스에서 출발
. 0을 만나면 아래로 내려감
. 1을 만나면 좌우검사 후, 1 값이 있는 방향으로 이동
. 결과 출력
'''
import random
    
class Ladder:
    player_cnt = 0
    ladder = []
    def __init__(self,player_cnt):
        self.player_cnt = player_cnt
        self.ladder = [[0, 0, 0, 0, 0],
                       [1, 1, 0, 1, 1],
                       [0, 1, 1, 0, 0],
                       [0, 0, 1, 1, 0],
                       [1, 1, 0, 0, 0],
                       [0, 1, 1, 0, 0],
                       [1, 1, 0, 0, 0],
                       [0, 0, 0, 1, 1],
                       [0, 0, 0, 0, 0]
                       ]
        
        
    
    def printLadder(self):
        for i in range(9):
            for j in range(5):
                if self.ladder[i][j] == 0:
                    print("│", end="")
                elif self.ladder[i][j] == 1:
                    if j != 0 and self.ladder[i][j-1] == 1:
                        print("┤", end="")
                    elif j != 4 and self.ladder[i][j+1] == 1:
                        print("├", end="")
            print()
    def run(self):
        temp = []
        for i in range(5):
            item = input("결과값%d: "%(i))
            temp.append(item)
        self.printLadder()
        cnt = [0,0,0,0,0]
        k = 0
        while k < self.player_cnt:
            x = random.randint(0,4)
            if cnt[x] != 0:
                continue
            cnt[x] = 1
            print("idx: ",x)
        
            y = 0
            for i in range(9):
                if self.ladder[y][x] == 1:
                    if x != 0 and self.ladder[y][x-1] == 1:
                        x -= 1
                    elif x != 4 and self.ladder[y][x+1] == 1:
                        x += 1
                y += 1

            print("결과%d: %s"%(k+1,temp[x]))

            k += 1
