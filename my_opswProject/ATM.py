# 1. 회원가입
# . id와 pw를 입력받아 가입
# . 가입 시 돈 1000원 부여
# . id 중복체크
# 2. 회원탈퇴
# . 로그인시에만 이용가능
# 3. 로그인
# . id와 pw를 입력받아 로그인
# . 로그아웃 상태에서만 이용가능
# 4. 로그아웃
# . 로그인시에만 이용가능
# 5. 입금
# . 로그인시에만 이용가능
# 6. 이체
# . 로그인시에만 이용가능
# 7. 잔액조회
# . 로그인시에만 이용가능

class Bank:
    size = 5
    ids = [0 for i in range(size)]
    pws = [0 for i in range(size)]
    moneys = [0 for i in range(size)]
    log = -1

    def run(self):
        while True:
            print("[1]회원가입")
            print("[2]회원탈퇴")
            print("[3]로그인")
            print("[4]로그아웃")
            print("[5]입금")
            print("[6]이체")
            print("[7]잔액조회")
            print("[0]종료")

            choice = int(input("메뉴 선택 : "))

            if choice == 1:
                idx = 0
                while True:
                    if self.ids[idx] == 0:
                        break
                    idx += 1
                my_id = int(input("사용할 id: "))
                check = 0
                for i in range(self.size):
                    if my_id == self.ids[i]:
                        print("중복입니다.")
                        check = 1
                        break
                if check == 0:
                    self.ids[idx] = my_id
                    my_pw = int(input("사용할 pw: "))
                    self.pws[idx] = my_pw
                    print("회원가입 완료. 가입 기념으로 1000원 충전")
                    self.moneys[idx] = 1000
                else:
                    continue
                
            elif choice == 2:
                if self.log == -1:
                    print("로그인 후 이용해주십시오")
                    continue
                self.ids[self.log] = 0
                self.pws[self.log] = 0
                self.log = -1
                print("탈퇴되었습니다.")
                
            elif choice == 3:
                if self.log == -1:
                    my_id = int(input("id: "))
                    my_pw = int(input("pw: "))
                    for i in range(self.size):
                        if my_id == self.ids[i] and my_pw == self.pws[i]:
                            self.log = i
                            print("%d님, 로그인 되었습니다."%(self.ids[i]))
                            break
                    if self.log == -1:
                        print("아이디 혹은 패스워드 오류입니다.")
                else:
                    print("이미 로그인 되어있습니다.")               
                
            elif choice == 4:
                if self.log == -1:
                    print("이미 로그아웃 되어있습니다.")
                else:
                    self.log = -1
                    print("로그아웃 되었습니다.")
                    
            elif choice == 5:
                if self.log == -1:
                    print("로그인 후 이용해주십시오")
                    continue

                m = int(input("입금할 금액을 입력하세요: "))
                self.moneys[self.log] += m
                print("입금 완료")
            elif choice == 6:
                if self.log == -1:
                    print("로그인 후 이용해주십시오")
                    continue
                m = int(input("이체할 금액을 입력하세요: "))
                if self.moneys[self.log] >= m:
                    self.moneys[self.log] -= m
                    print("이체 완료")
                else:
                    print("잔액이 부족합니다.")
                
            elif choice == 7:
                if self.log == -1:
                    print("로그인 후 이용해주십시오")
                    continue
                print("잔액은 %d원 입니다."%(self.moneys[self.log]))
            elif choice == 0:
                print("프로그램 종료")
                break