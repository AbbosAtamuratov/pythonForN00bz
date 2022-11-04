from awesome_progress_bar import ProgressBar
import time
import emoji
import random

def thought_progress(a)->int:
    total = 100
    bar = ProgressBar(total, bar_length=40, fill='|', use_time=False, spinner_type='db',
                      prefix=emoji.emojize(' таакс... :point_right::tired_face::point_left: ', language='alias'))
    try:
        for x in range(total):
            time.sleep(0.005)
            bar.iter(' мыслительный процесс')
    except:
        bar.stop()
    bar.wait()
    print(emoji.emojize(f'Опа-на! - {a} :point_down::imp::point_down:', language='alias'))
    return a

def RunGame_AI (ps, pm, hl, tc) -> bool:
    coin_toss = True
    while tc>0:
        if coin_toss == False:
            print(emoji.emojize(f'Ходит {ps(coin_toss)}... :alien:', language='alias'))
            if tc<=hl:
                tc=0
            elif 0<tc<2*hl+1:
                if tc%29 == 0:
                    tc-=thought_progress(1)
                else:
                    tc-=thought_progress(tc%29)
            else:
                tc-=thought_progress(random.randint(1,hl+1))
        else:
            turn = pm(coin_toss)
            while turn>hl:
                print(f'А вот жульничать не надо! Максимум {hl} за раз. \nПопробуйте ещё раз.')
                turn=pm(coin_toss)
            tc-=turn
        coin_toss = not coin_toss
        print(f'Осталось {tc} конфет')
    else:
        coin_toss = not coin_toss
        if coin_toss:
            print(f'Игрок{ps(coin_toss)} победил. Поздравляем!')
            return True
        else:
            print('Победил ИИ. Удачи в другой раз.')
            return False

def scoreboard(sc, res) -> list:
    if res:
        sc[0]+=1
    else:
        sc[1]+=1
    return sc