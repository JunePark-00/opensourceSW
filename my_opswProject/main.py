#main
import movie_ticket
import LadderGame
import food_ticket
import ATM
import Lotte
import MemoryGame
import crazygame
import ShoppingCenter
import Karaoke
import ParkingLot

def menu():
    print("[1] Restaurant")
    print("[2] Cinema")
    print("[3] Game Center")
    print("[4] Shopping Center")
    print("[5] Bank")
    print("[6] Karaoke")
    print("[7] Parking Lot")
    print("[0] Exit")

while True:
    print("Welcome to DKU-MAll")
    menu()
    sel = int(input(">>> "))
    if sel==1:
        print("DKU RESTAURANT")
        print("[1] Food Court")
        print("[2] Lotteria")
        cho = int(input(">>> "))
        if cho==1:
            foodtic = food_ticket.Foodticket()
            foodtic.run()
        elif cho==2:
            burger = Lotte.Lotteria()
            burger.run()
    elif sel==2:
        print("DKU CINEMA")
        movie = movie_ticket.Movie(0)
        movie.run()
    elif sel==3:
        print("DKU GAME CENTER")
        print("[1] Ladder Game")
        print("[2] Memory Game")
        print("[3] Crazy Acade")
        cho = int(input(">>> "))
        if cho==1:
            game1 = LadderGame.Ladder(2)
            game1.run()
        elif cho==2:
            game2 = MemoryGame.Memory()
            game2.run()
        elif cho==3:
            g = crazygame.Crazy()
            g.setWall(8)
            g.setPlayer()
            while True:
                if g.end == 1:
                    break
                g.showMap()
                g.menu()
                sel = int(input(": "))
                if 1 <= sel <= 4:
                    g.move(sel)
                elif sel == 5:
                    g.installBomb()
                elif sel == 6:
                    g.explode()
                elif sel == 7:
                    print("게임을 종료합니다.")
                    break 
    elif sel==4:
        print("DKU SHOPPING CENTER")
        shop = ShpppingCenter.Shopping()
        shop.run()
    elif sel==5:
        print("DKU BANK")
        dkuatm = ATM.Bank()
        dkuatm.run()
    elif sel==6:
        print("DKU KARAOKE")
        songNum = int(input("등록할 곡 수를 입력하세요 : "))
        sing = Karaoke.Singing(songNum)
        sing.run()
    elif sel==7:
        print("DKU-MALL PARKING LOT")
        park = ParkingLot.Parking()
        park.run()
    elif sel==0:
        print("Thank you for coming")
        break
        
        

