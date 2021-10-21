n=input('Введите имя')
if len(n)<5:
    s=input('Введите фамилию')
    print(n+s.upper())
else:
    print(n.lower())