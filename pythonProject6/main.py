import random
c = int(input('Введите количество игр:'))
k=0
n=0
b=0

for _ in range(c):
    sp = ['Камень', 'Ножницы', 'Бумага']
    p = input('Введите знак:')
    c = random.choice(sp)
    print(c)
    if p == sp[0]:
        k+=1
        if c == sp[0]:
            print('Ничья')
        elif c == sp[1]:
            print('Победа')
        elif c == sp[2]:
            print('Поражение')
    elif p == sp[1]:
        n+=1
        if c == sp[0]:
            print('Поражение')
        elif c == sp[1]:
            print('Ничья')
        elif c == sp[2]:
            print('Победа')
    elif p == sp[2]:
        b+=1
        if c == sp[0]:
            print('Победа')
        elif c == sp[1]:
            print('Поражение')
        elif c == sp[2]:
            print('Ничья')
print('Вы использовали следующие знаки: Камень(',k,'раз),Ножницы(',n,'раз),Бумага(',b,'раз)')
if k>n and k>b:
    print('Против вас полезнее всего использовать бумагу')
elif n>k and n>b:
    print('Против вас полезнее всего камень ')
else:
    print('Против вас полезнее всего использовать ножницы')
