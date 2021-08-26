'''
노래방 곡명을 가나다순으로 정렬
'''
class Singing:
    songNum = 0
    songList = []
    songName = ""
    def __init__(self,songNum,songName=None,songList=None):
        self.songNum = songNum
    
    def makeList(self):
        for i in range(self.songNum):
            self.songName = input("곡명을 입력해주세요 : ")
            self.songList.append(self.songName)

    def sorting(self):
        self.makeList()
        self.songList.sort()

    def run(self):
        self.sorting()
        print("[SONG LIST]")
        for i in range(self.songNum):
            print("[%d] %s"%(i+1,self.songList[i]))
        while True:
            sel = int(input("곡 넘버를 입력해주세요(0을 누르면 종료) : "))  
            if sel==0:
                break
            print("현재 곡 : %s"%(self.songList[sel-1]))   
