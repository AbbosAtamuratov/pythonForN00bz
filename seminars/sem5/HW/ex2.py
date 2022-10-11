# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

player = lambda x: 2 if not x else 1 
total_candies = 2021
max_capacity_move = 28
first_move = True
turn = lambda x: x-int(input(f'Игрок{player(move)} Ваш ход: ')) 
move=player(first_move)

def RunGame(p, tc, t, m, mc):
    while tc != 0:
        tc += t(m)
        print (f'Осталось {tc} конфет.')
        if tc > 0:
            m = not m
    else:
        print(f'Игрок{p(m)} победил')

RunGame(player, total_candies, turn, move, max_capacity_move)