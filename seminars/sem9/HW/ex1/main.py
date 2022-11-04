import engine as e
import view as v

nickname = input('Как вас звать? ')
player_switch = lambda x: nickname if x else 'Алёша'
player_move = lambda b: int(input('{}, ваш ход: '.format(player_switch(b))))
is_running= True
who_won = False
score = [0, 0]

v.startup()
while is_running:
    command=input('Введите команду или help: ')
    if command == 'run game':
        who_won = e.RunGame_AI(player_switch, player_move, hl=28,tc=201)
        score = e.scoreboard(score, who_won)
    elif command == 'quit':
        is_running=False
    elif command == 'help':
        v.help()
    elif command == 'score':
        v.show(nickname, score)
    else:
        print('Некорректный ввод. Попробуйте ещё раз...')

