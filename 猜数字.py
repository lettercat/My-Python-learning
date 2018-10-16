# 用Python实现猜数字的小游戏 (GUESS THE NUMBER COMPUTER GETS)
# This is the first bug writed by lettercat.
# coding = utf-8
import random
def game():
    print("The computer had a mysterious number. Now we just know it is between 0 to 100. Let us guess! ")
    NUM: int = (random. randint(0, 100))  # 电脑随机生成一个数字（provisionally 1-100）
    x = eval(input('You think the number is:\n '))  # 读取输入的数字
    for i in range(51):
        if x == NUM:
            print('Bingo! ')
            exit()  # 猜对了！游戏结束
        if x != NUM:
            if x > NUM:
                if (x - NUM) > 10:
                    print('too big. ')  # 太大了（tips1）
                if (x - NUM) <= 10:
                    print("It's a bit big. ")  # 很接近了 但还是大（tips2）
            if x < NUM:
                if (NUM - x) > 10:
                    print('too small. ')  # 太小了（tips3）
                if (NUM - x) <= 10:
                    print("it's a bit small. ")  # 很接近了 但还是小 （tips4）
            print('Oh no that is wrong. Let us try again. ')  # 再试一次吧
        x = eval(input('You think the number is:\n '))  # 再次读取输入的数字
game()