import emoji

def startup ():
    print(emoji.emojize(':candy: Добро пожаловать в игру "Конфетки"! :candy:'))
    print(emoji.emojize(':star2:  Всего на столе 201 конфета.', language='alias'))
    print(emoji.emojize(':bangbang:Каждый игрок может взять максимум 28 конфет за раз.', language='alias'))
    print(emoji.emojize(':bangbang:Игрок, взявший последние конфеты со стола, побеждает.:sparkles::sparkles::sparkles:', language='alias'))
    print(emoji.emojize(':candy::candy:Победитель забирает все конфеты.:candy::candy:'))
    print(emoji.emojize(':question:Получится ли у вас обыграть ИИ Алёшу:question:\n', language='alias'))

def help():
    print('run game - Начать игру')
    print('score - Показать счёт')
    print('quit - Закончить работу')

def show (nick, sc):
    print(f'{nick}  {sc[0]} - {sc[1]}  Алёша')