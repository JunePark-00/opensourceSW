import os

class Shopping:
    ids = ["qwer", "python", "abcd"]
    pws = ["1111",   "2222", "3333"]
    size = len(ids)
    items = ["사과", "바나나", "딸기"]
    max_size = 100
    jang = [[0] * 2 for i in range(max_size)]
    count = 0
    log = -1

    file_name = "jang.txt"

    def run(self):
        while True:
            data = ""
            print("[1]로그인")
            print("[2]로그아웃")
            print("[3]쇼핑")
            print("[4]장바구니")
            print("[5]저장")
            print("[6]로드")
            print("[0]종료")

            sel = int(input("메뉴 선택 : "))
            if sel == 1:
                if self.log != -1:
                    print("이미 로그인 되어있습니다.")
                    continue
                my_id = input("아이디를 입력하세요: ")
                my_pw = input("비밀번호를 입력하세요: ")
                cnt = 0
                for i in range(self.size):
                    if my_id == self.ids[i] and my_pw == self.pws[i]:
                        print("%s님, 로그인되었습니다."%(self.ids[i]))
                        self.log = i
                        cnt = 1
                        break
                if cnt == 0:
                    print("아이디 혹은 비밀번호 오류입니다.")
            elif sel == 2:
                if self.log == -1:
                    print("이미 로그아웃 되어있습니다.")
                    continue
                self.log = -1
                print("로그아웃 되었습니다.")
            elif sel == 3:
                if self.log == -1:
                    print("로그인 후 이용해주세요.")
                    continue
                while True:
                    for i in range(len(self.items)):
                        print("[%d]"%(i+1),self.items[i])
                    item_idx = int(input("구매하실 아이템의 번호를 입력하세요(종료는 0): "))

                    if item_idx == 0:
                        break

                    else:
                        self.jang[self.count][0] = self.log
                        self.jang[self.count][1] = item_idx
                        self.count +=1
                
            elif sel == 4:
                if self.log == -1:
                    print("로그인 후 이용해주세요.")
                    continue
                apple = 0
                banana = 0
                straw = 0
                print(self.count)
                for i in range(self.count):
                    if self.jang[i][0] == self.log:
                        if self.jang[i][1] == 1:
                            apple += 1
                        elif self.jang[i][1] == 2:
                            banana += 1
                        elif self.jang[i][1] == 3:
                            straw += 1
                print("사과: ",apple)
                print("바나나: ",banana)
                print("딸기: ",straw)
                            
            elif sel == 5:
                if self.log == -1:
                    print("로그인 후 이용해주세요.")
                    continue
                f = open(file_name,"wt")
                for i in range(self.count):
                    data += (str(self.jang[i][0]) + "/" + str(self.jang[i][1]) + "\n")
                f.write(data)
                f.close()
                print("파일 생성 완료")
            elif sel == 6:
                if self.log == -1:
                    print("로그인 후 이용해주세요.")
                    continue
                if os.path.exists(file_name):
                    f = open(file_name,"rt")
                    data = f.read()
                    f.close()

                    temp = data.split("\n")

                    for i in range(self.count):
                        temp2 = temp[i].split("/")

                        self.jang[i][0] = int(temp2[0])
                        self.jang[i][1] = int(temp2[1])
                        print(self.jang[i])
                else:
                    print("파일을 불러올 수 없습니다.")
                        
            elif sel == 0:
                print("프로그램 종료")
                break