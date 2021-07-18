import os

"""
    Rumus : https://github.com/johsteven/penghitung-wr
"""

def clear():
    os.system("clear")
    pass
def pause():
    input()
    pass

def banner():
    clear()
    print(""" _       ______     ______                  __
| |     / / __ \   / ____/___  __  ______  / /____  _____
| | /| / / /_/ /  / /   / __ \/ / / / __ \/ __/ _ \/ ___/
| |/ |/ / _, _/  / /___/ /_/ / /_/ / / / / /_/  __/ /
|__/|__/_/ |_|   \____/\____/\__,_/_/ /_/\__/\___/_/ Mobile Legends

  [1] Penghitung WR
  [2] Total Win dan Lose
  [3] Hitung WR dengan LoseStreak
  [0] Exit
    """)
    pass

def penghitungWr(tMatch, tWr, wrReq):
    tWin = tMatch * (tWr / 100)
    tLose = tMatch - tWin
    sisaWr = 100 - wrReq
    wrResult = 100 / sisaWr
    seratusPersen = tLose * wrResult
    final = seratusPersen - tMatch
    final = int(final)
    print(f"\nKamu memerlukan sekitar {final} win tanpa lose untuk mendapatkan win rate {wrReq}%")
    pass
def winLose(tMatch, tWr):
    win  = tMatch * (tWr / 100)
    lose = tMatch - (tMatch * (tWr / 100))
    print(f"\nTotal Win  : {int(win)}\nTotal Lose : {int(lose)}")
    pass
def loseStreak(tMatch, tWr, lsReq):
    wr = (tMatch * (tWr / 100) - lsReq) / tMatch * 100
    wr = format(wr, '.2f')
    print(f"\nJika anda losestreak sebanyak {int(lsReq)} kali, maka winrate anda menjadi {wr}%")
    pass
while True:
    banner()
    choose = input(">> ")
    if choose == "1":
        tMatch = float(input('Total match anda   : '))
        tWr    = float(input('Total WR anda      : '))
        wrReq  = float(input('WR yang diinginkan : '))
        penghitungWr(tMatch, tWr, wrReq)
        pause()
        pass
    if choose == "2":
        tMatch = float(input('Total match anda   : '))
        tWr    = float(input('Total WR anda      : '))
        winLose(tMatch, tWr)
        pause()
        pass
    if choose == "3":
        tMatch = float(input('Total match anda   : '))
        tWr    = float(input('Total WR anda      : '))
        wrReq  = float(input('LS yang diinginkan : '))
        loseStreak(tMatch, tWr, wrReq)
        pause()
        pass
    if choose == "0":
        exit()
        pass
    pass
