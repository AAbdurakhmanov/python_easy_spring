# Converter simple program
from colored import fg, bg, attr
from random import randint


def hello():

    color = fg(0) + bg(randint(2, 255))
    close = attr('reset')

    hi = print(color, 'Hi i`m simple converter program', close)

    def dollar():
        choose = input(f'{color}Choose valuta so`m(1) or euro(2) > ')
        if choose == 'so`m' or choose == '1':
            print('Conversion result:', money * 10450, f'so`m{close}')
        elif choose == 'euro' or choose == '2':
            print('Conversion result:', money / 0.83, f'euro{close}')
        else:
            print(fg('red'), 'Heyy choose one of them so`m yoki euro', close)
            return dollar()

    def som():
        choose = input(f'{color}Choose valuta dollar(1) or euro(2) > ')
        if choose == 'dollar' or choose == '1' or choose == '$':
            print('Conversion result:', money / 10450, f'${close}')
        elif choose == 'euro' or choose == '2':
            print('Conversion result:', money / 12500, f'euro{close}')
        else:
            print(fg('red'), 'Heyy choose one of them dollar yoki euro')
            return som()

    def euro():
        choose = input(f'{color}Choose valuta so`m(1) or dollar(2) > ')
        if choose == 'so`m' or choose == '1':
            print('Conversion result:', money * 12500, f'so`m{close}')
        elif choose == '$' or choose == '2' or choose == 'dollar':
            print('Conversion result:', money * 0.83, f'${close}')
        else:
            print(fg('red'), 'Heyy choose one of them so`m yoki dollar')
            return dollar()

    try:
        money = float(input(f'{color}Create value :'))
        birligi = str(input('Create valuta (So`m)(1), (Dollar)(2) or (Euro)(3) '))

        if birligi == 'So`m' or birligi == 'so`m' or birligi == '1':
            print('So`m', close)
            return som()
        elif birligi == 'Dollar' or birligi == 'dollar' or birligi == '2':
            print('$', close)
            return dollar()
        elif birligi == 'Euro' or birligi == 'euro' or birligi == '3':
            print('Euro', close)
            return euro()
        else:
            print(bg('black')+fg('white')+f'Bittasini tanla 1,2,3{close}\n')
            return print(hello().birligi)
    except ValueError:
        print(bg('red')+fg('white')+f'Enter only numbers not lettors!{close}\n')
        return hello()


def again():
    want = input(fg('blue') + '\nagain yes/no : ')
    if want == 'yes' or want == 'y':
        print(fg('red') + 'good job !\n')
        return hello()
    elif want == 'no' or want == 'n':
        print('thanks for using! good luck')
        exit()


hello()
again()
