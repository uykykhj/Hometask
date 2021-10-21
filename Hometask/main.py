nap=int(input())
pov=int(input())
pol=''


if nap==11:
    pol='Север'
    if pov == -1:
        pol = 'Восток'
    elif pov == 0:
        pol = 'Север'
    elif pov == 1:
        pol = 'Запад'


elif nap==12:
    pol = 'Запад'
    if pov == -1:
        pol = 'Север'
    elif pov == 0:
        pol = 'Восток'
    elif pov == 1:
        pol = 'Юг'


elif nap==13:
    pol = 'Юг'
    if pov == -1:
        pol = 'Запад'
    elif pov == 0:
        pol = 'Юг'
    elif pov == 1:
        pol = 'Восток'


elif nap==14:
    pol = 'Восток'
    if pov == -1:
        pol = 'Юг'
    elif pov == 0:
        pol = 'Восток'
    elif pov == 1:
        pol = 'Север'
print(pol)

