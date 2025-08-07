import random

def chkh(a):
    d = 0
    for i in range(5):
        if all(x == 0 for x in a[i]):
            d += 1
    return d

def chkv(a):
    d = 0
    for i in range(5):
        if all(a[j][i] == 0 for j in range(5)):
            d += 1
    return d

def chkd1(a):
    if all(a[i][i] == 0 for i in range(5)):
        return 1
    return 0

def chkd2(a):
    if all(a[i][4 - i] == 0 for i in range(5)):
        return 1
    return 0

def display(a):
    for row in a:
        print("\t".join(str(x) for x in row))
    print()

def run_single_game(p):
    min_val = 1000
    for i in range(0, p):
        win_time = run_single_board()
        min_val = min(min_val, win_time)
    return min_val

def run_single_board():
    a = make_board()
    stack = [i + 1 for i in range(0,26)]
    stack.remove(13)
    random.shuffle(stack)
    num_marked = 0
    while check_win(a) == 0:
        a = mark_num(a, stack.pop())
        num_marked += 1
    return num_marked

def run_x_games(x, p = 1):
    wincount = []
    for i in range(0,x):
        wincount.append(run_single_game(p))
    return wincount

def mark_num(a, n):
    for i in range(5):
            for j in range(5):
                if a[i][j] == n:
                    a[i][j] = 0
    return a

def make_board():
    a = [[i * 5 + j + 1 for j in range(5)] for i in range(5)]
    a[2][2] = 0 #free space
    return a

def check_win(a):
    return chkv(a) + chkh(a) + chkd1(a) + chkd2(a)


def main():
    # print(run_single_game(5))
    wins_list = run_x_games(1000, 14)
    print("Average Bingo Win Time", sum(wins_list) / len(wins_list))


if __name__ == "__main__":
    main()
