from random import randint
from colored import fg, bg, attr


class Brain_game:

    def __init__(self, score=0, life=3):
        self.score = score
        self.life = life

    # Level 1 function
    def level1(self):
        global level2, level3
        score1, life1 = self.score, self.life
        color = fg(0) + bg(randint(1, 100))
        res = attr('reset')
        name = input(color + f'Hi there i`m simple brain game {res}\n{color}What is your name : ' + res)
        if not name.isalpha():
            print(fg('red'), '\nPlease create only letters not numbers \n', res)
            return Brain_game.level1(self)
        print(color, f'Good {name.capitalize()} you have 3 life' + res)
        for answer in range(1000):
            a, b = randint(1, 100), randint(1, 100)
            try:
                answer = int(input(f'{a} + {b} = '))
                if answer == a + b:
                    score1 += 1
                    print(bg('blue'), fg('white') + 'Correct', score1, res)
                    if score1 == 4:
                        print(f'\n{color}Vere nice ! you are clever{res}')
                        return level2()
                elif answer != a + b:
                    life1 -= 1
                    print(bg('red'), fg('white'), 'Wrong! True answer is ', a + b, 'your chance', life1, res)
                    if life1 == 0:
                        print(color, 'You lose', res)
                        break
            except ValueError:
                print(f'\n{bg("red")}{fg("white")}Ops only numbers not letters{res}\n')

            # Level 2 function

            def level2():
                global level3
                score2, life2 = score1, life1
                for answer2 in range(1000):
                    a, b, c = randint(10, 100), randint(1, 60), randint(10, 500)

                    try:
                        answer2 = int(input(f'{a} * {b} - {c} = '))
                        if answer2 == a * b - c:
                            score2 += 2
                            print(bg('blue'), fg('white') + 'Correct', score2, res)
                            if score2 == 20:
                                print(f'\n{color} Bramissimo {res}')
                                return level3()

                        elif answer2 != a * b - c:
                            life2 -= 1
                            print(bg('red'), fg('white'), 'Wrong! True answer is ', a * b - c, 'your chance', life2,
                                  res)
                            if life2 == 0:
                                print(color, 'You lose', res)
                                break
                    except ValueError:
                        print(f'\n{bg("red")}{fg("white")}Ops only numbers not letters{res}\n')

                    # Level 3 functions
                    def level3():
                        score3, life3 = score2, life2
                        for answer3 in range(1000):
                            a, b, c, d = randint(10, 100), randint(10, 300), randint(1, 500), randint(1, 100)

                            try:
                                answer3 = float(input(f'{a} * {b} + {c} / {d}= '))
                                if answer3 == a*b+c/d:
                                    score3 += 3
                                    print(bg('blue'), fg('white') + 'Correct', score3, res)


                                elif answer3 != a*b+c/d:
                                    life3 -= 1
                                    print(bg('red'), fg('white'), 'Wrong! True answer is ', a+b+c+d, 'your chance', life3, res)
                                    if life3 == 0:
                                        print(color, 'You lose', res)
                                        break
                            except ValueError:
                                print(f'\n{bg("red")}{fg("white")}Ops only numbers not letters{res}\n')


game = Brain_game()
print(game.level1())