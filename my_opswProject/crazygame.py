# 크레이지 아케이드 (모듈 사용)
'''
1. 맵의 크기는 7 x 7 이다. 
2. 상(1)하(2)좌(3)우(4)로 이동이 가능하며,
	 폭탄설치(5), 폭파(6)로 설정한다. 
3. 벽(3), 플레이어(2), 폭탄(9), 아이템(4)로 설정한다.
4. 단, 폭탄이 설치된 순서대로 터져야 하며,
	 폭파 시 십자가 형태로 터진다.
5. 벽 파괴시 아이템이 랜덤하게 생성되어,
	 아이템을 먹으면 설치할 수 있는 폭탄의 개수가 증가된다.
'''
import random

class Crazy:
    g_map = []
    wall = 3
    player = 2
    bomb = 9
    item = 4
    p_x = 0
    p_y = 0
    bombList = []
    end = 0

    def __init__(self):
        self.g_map = [[0]*7 for i in range(7)]
        self.bombList = [[9]*2 for i in range(3)]

    def showMap(self):
        cnt = 0
        for i in range(7):
            for j in range(7):
                if self.g_map[i][j] == 0:
                    print("□",end="")
                elif self.g_map[i][j] == self.wall:
                    cnt += 1
                    print("■",end="")
                elif self.g_map[i][j] == self.player:
                    print("§",end="")
                elif self.g_map[i][j] == self.bomb:
                    print("●",end="")
                else:
                    print("♣",end="")
            print()
        if cnt == 0:
            print("Game Clear")
            self.end = 1
            return
        print("설치할 수 있는 폭탄 개수: ",len(self.bombList))

    def menu(self):
        print("[1]상 [2]하 [3]좌 [4]우")
        print("[5]폭탄설치 [6]폭파 [7] 종료")
        
    def setWall(self,num):
        for i in range(num):
            r1 = random.randint(0,6)
            r2 = random.randint(0,6)
            self.g_map[r1][r2] = self.wall

    def setPlayer(self):
        i = 0
        while i < 1:
            r1 = random.randint(0,6)
            r2 = random.randint(0,6)
            if self.g_map[r1][r2] == 0:
                self.g_map[r1][r2] = self.player
                self.p_x = r2
                self.p_y = r1
                i += 1
            else:
                continue      
        
    def installBomb(self):
        b_y = self.p_y
        b_x = self.p_x
        print(b_y,b_x)
        size = len(self.bombList)
        idx = -1
        for i in range(size):
            if self.bombList[i][0] == 9:
                idx = i
                break
        if idx == -1:
            print("폭탄을 모두 사용하였습니다.")
            return
        
        print("[1]상 [2]하 [3]좌 [4]우")
        b = int(input("폭탄설치 위치: "))
        if b == 1:
            if b_y == 0:
                print("설치할 수 없는 위치입니다.")
            else:
                if self.g_map[b_y-1][b_x] == self.wall:
                    print("설치할 수 없는 위치입니다.")
                    return
                b_y -= 1
                
        elif b == 2:
            if b_y == 6:
                print("설치할 수 없는 위치입니다.")
            else:
                if self.g_map[b_y+1][b_x] == self.wall:
                    print("설치할 수 없는 위치입니다.")
                    return
                b_y += 1

        elif b == 3:
            if b_x == 0:
                print("설치할 수 없는 위치입니다.")
            else:
                if self.g_map[b_y][b_x-1] == self.wall:
                    print("설치할 수 없는 위치입니다.")
                    return
                b_x -= 1

        elif b == 4:
            if b_x == 6:
                print("설치할 수 없는 위치입니다.")
            else:
                if self.g_map[b_y][b_x+1] == self.wall:
                    print("설치할 수 없는 위치입니다.")
                    return
                b_x += 1

        print(idx)
        self.g_map[b_y][b_x] = self.bomb
        self.bombList[idx][0] = b_y
        self.bombList[idx][1] = b_x

    ######
    def explode(self):
        r = random.randint(1,3)
        y = self.bombList[0][0]
        x = self.bombList[0][1]
        del(self.bombList[0])
        i = 0
        while i < 5:
            try:
                if i == 0:
                    if self.g_map[y][x-1] == self.player or self.g_map[y][x+1] == self.player or self.g_map[y-1][x] == self.player or self.g_map[y+1][x] == self.player:
                        print("Game Over")
                        self.end = 1
                        return
                if i == 1:
                    if self.g_map[y][x-1] == self.wall:
                        self.makeItem(r)
                        self.g_map[y][x-1] = 0
                if i == 2:
                    if self.g_map[y][x+1] == self.wall:
                        self.makeItem(r)
                        self.g_map[y][x+1] = 0
                if i == 3:
                    if self.g_map[y-1][x] == self.wall:
                        self.makeItem(r)
                        self.g_map[y-1][x] = 0
                if i == 4:
                    if self.g_map[y+1][x] == self.wall:
                        self.makeItem(r)
                        self.g_map[y+1][x] = 0
                self.g_map[y][x] = 0
            except IndexError:
                pass
            finally:
                i += 1
            
                        
    def makeItem(self,r):
        i = 0
        while i < r:
            r1 = random.randint(0,6)
            r2 = random.randint(0,6)
            if self.g_map[r1][r2] == 0:
                self.g_map[r1][r2] = self.item
                i += 1
            else:
                continue

    def move(self,sel):
        if sel == 1:
            if self.p_y == 0:
                print("더이상 이동할 수 없습니다.")
            else:
                if self.g_map[self.p_y-1][self.p_x] == self.wall:
                    print("벽을 만나 이동할 수 없습니다.")
                    return
                self.g_map[self.p_y][self.p_x] = 0
                self.p_y -= 1
                
        elif sel == 2:
            if self.p_y == 6:
                print("더이상 이동할 수 없습니다.")
            else:
                if self.g_map[self.p_y+1][self.p_x] == self.wall:
                    print("벽을 만나 이동할 수 없습니다.")
                    return
                self.g_map[self.p_y][self.p_x] = 0
                self.p_y += 1

        elif sel == 3:
            if self.p_x == 0:
                print("더이상 이동할 수 없습니다.")
            else:
                if self.g_map[self.p_y][self.p_x-1] == self.wall:
                    print("벽을 만나 이동할 수 없습니다.")
                    return
                self.g_map[self.p_y][self.p_x] = 0
                self.p_x -= 1
                
        elif sel == 4:
            if self.p_x == 6:
                print("더이상 이동할 수 없습니다.")
            else:
                if self.g_map[self.p_y][self.p_x+1] == self.wall:
                    print("벽을 만나 이동할 수 없습니다.")
                    return
                self.g_map[self.p_y][self.p_x] = 0
                self.p_x += 1
        if self.g_map[self.p_y][self.p_x] == self.item:
            print("아이템 획득! 설치할 수 있는 폭탄 개수 + 1")
            self.bombList.append([9]*2)
        self.g_map[self.p_y][self.p_x] = self.player