import random
import os
import platform

from time import sleep
from colorama import init, Fore

def Clean():
    if platform.system() == 'Windows':
        os.system('cls')
    elif platform.system() == 'Linux':
        os.system('clear')

print("Chào mừng tới incoin game thuộc GameZam")

Name = input("Tên bạn là: ")
time = 2

Clean()
Clean()

Bots = {
    'Vẹt':{
        'give':['lấy ra một coin',"không làm gì cả",'gửi vào một coin'],
        'take':["lấy ra một coin","không làm gì cả"],
        "nact":["không làm gì cả",'gửi vào một coin']
    },
    'Chó':{
        'give':["gửi vào một coin"],
        'take':["gửi vào một coin","lấy ra một coin"],
        'nact':["gửi vào một coin","không làm gì cả"]
    },
    "Mèo":{
        'give':['gửi vào một coin','không làm gì cả'],
        'take':['lấy ra một coin','lấy ra một coin','gửi vào một coin'],
        'nact':['không làm gì cả','không làm gì cả','lấy ra một coin']
    },
    "Cá sấu":{
        'give':['không làm gì cả','không làm gì cả','lấy ra một coin','gửi vào một coin'],
        "take":['gửi vào một coin','lấy ra một coin','gửi vào một coin'],
        'nact':['gửi vào một coin','lấy ra một coin','gửi vào một coin']
    },
    'Cua':{
        'give':['không làm gì cả','gửi vào một coin','gửi vào một coin'],
        'take':['lấy ra một coin','không làm gì cả','không làm gì cả'],
        'nact':['gửi vào một coin','gửi vào một coin','lấy ra một con']
    },
    'Bồ câu':{
        'give':['không làm gì cả','lấy ra một coin','gửi vào một coin'],
        'take':['lấy ra một coin','lấy ra một coin','không làm gì cả'],
        'nact':['gửi vào một coin','lấy ra một coin','lấy ra một coin']
    }
}

def Highlight(color,word):
    colors = {
        'red':Fore.RED,
        'blue':Fore.BLUE,
        'yellow':Fore.YELLOW,
        'green':Fore.GREEN,
        'magenta':Fore.MAGENTA,
        'light_blue':Fore.LIGHTBLUE_EX
    }

    return colors[color] + word + Fore.WHITE

def Rule():
    print(f"\nTrò chơi sẽ bắt đầu với một {Highlight('blue','người chơi')} và một {Highlight('magenta','kẻ thù ngẫu nhiên')}")
    print(f"Cả hai sẽ khởi đầu với một {Highlight('yellow','số vốn')} nhất định")
    print(f"Mỗi lượt, người chơi và đối thủ có thể {Highlight('green','gửi')}, {Highlight('red','lấy')} từ {Highlight('light_blue','ngân hàng')} một đồng xu (coin) hoặc không làm gì cả")
    print(f"Với mỗi {Highlight('yellow','coin')}, {Highlight('light_blue','ngân hàng')} sẽ cho ra {Highlight('yellow','lãi')} tương ứng vào các lượt tiếp theo")
    print(f"Vào lượt cuối cùng, số {Highlight('yellow','coin')} trong {Highlight('light_blue','ngân hàng')} sẽ được chia đôi cho cả 2")
    print(f"Ai nhiều {Highlight('yellow','coin')} hơn thì người đó sẽ thắng")

    input("Ok tôi đã hiểu... ")

def PLAY():
    global GAME
    global time
    ListBot = []
    for bot in Bots:
        ListBot.append(bot)

    randBot = random.choice(ListBot)
    bot = {
        'name':randBot,
        'coin':random.randint(5,10),
        'action':Bots[randBot]
    }

    PlayerCoin = random.randint(3,5)

    BankCoin   = 0

    TransKey = {
        'take':'lấy ra một coin',
        'nact':'không làm gì cả',
        'give':"gửi vào một coin"
    }

    Up = 0.1

    Turn = random.randint(5,15)

    LuckyMoney = [0,1]

    while True:

        if Turn == -1 :
            Clean()
            PlayerLuck = random.randint(LuckyMoney[0],LuckyMoney[1])
            BotLuck = random.randint(LuckyMoney[0],LuckyMoney[1])

            print(f"{Name}: {PlayerCoin} (+{int(BankCoin/2)+PlayerLuck})")
            print(f"{randBot}: {bot['coin']} (+{int(BankCoin/2)+BotLuck})")

            PlayerCoin+= int(BankCoin/2)+ PlayerLuck
            bot['coin']+= int(BankCoin/2) + BotLuck

            if PlayerCoin>bot['coin']:
                print(f"{Name} thắng với tỉ số chung cuộc: {PlayerCoin} > {bot['coin']}")
            elif bot['coin']>PlayerCoin:
                print(f"{randBot} thắng với tỉ số chung cuộc : {PlayerCoin} < {bot['coin']}")
            else:
                print(f"Hòa! tỉ số chung cuộc : {PlayerCoin} = {bot['coin']}")
            break
        
        Clean()
        print(Fore.LIGHTBLUE_EX + "[R] xem luật chơi - [S] cài đặt thời gian chờ")
        print(Fore.GREEN+"[Q] thoát - [take] lấy coin - [give] đưa coin - [nact] không làm gì cả")
        print(Fore.RED+ f"Còn {Turn} lượt"+Fore.WHITE)
        print(f"{Name}{(10-len(Name))*' '}{randBot}")
        print(f"{PlayerCoin}{(10-len(f'{PlayerCoin}'))*' '}{bot['coin']}")
        print(f"Ngân hàng hiện có: {int(BankCoin)} và lãi {round(Up*100,3)}% mỗi lượt")

        key = input("nhập lệnh: ")
        
        if key == 'q':
            break 
        if key == 'r':
            Rule()
        if key == 's':
            time = float(input("Độ trễ mỗi lượt (giây): "))
        try:
            act = random.choice(bot['action'][key])

            if TransKey[key] == act and key == 'give' and PlayerCoin>0 and bot['coin']>0:
                print("Cả 2 hợp tác vui vẻ, tăng lãi suất")
                BankCoin+=2
                PlayerCoin-=1
                bot['coin']-=1
                Up+=Up*0.1
                LuckyMoney[1] += 2
                LuckyMoney[0] += 1
            elif TransKey[key] == act and key == 'take':
                print("Cả 2 giành giựt lẫn nhau nên không nhận được gì và bị giảm lãi suất!")
                Up-=Up*0.15
            
            else :
                print(f"Bạn {TransKey[key]}")
                print(f"{randBot} {act}")

                if key == 'take' and BankCoin>0:
                    PlayerCoin+=1
                    BankCoin-=1
                if key == 'give' and PlayerCoin>0:
                    PlayerCoin-=1
                    BankCoin+=1
                
                if act == 'lấy ra một coin' and BankCoin>0:
                    bot['coin']+=1
                    BankCoin-=1
                if act == 'gửi vào một coin' and bot['coin']>0:
                    bot['coin']-=1
                    BankCoin+=1

            sleep(time)

            BankCoin += BankCoin*Up
            Turn-=1

            
        except:
            pass
        

GAME = 1
while GAME:
    start = input("Gõ [OK] để bắt đầu game mới hoặc [Q] để thoát: ").lower()
    if start == 'ok':
        PLAY()
    elif start == 'q':
        break
    else:
        print("Không có lệnh này!")