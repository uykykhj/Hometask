d=''
sl=input('Введите слово')
sl=sl.lower()
if sl[0] in 'aeiouy':
    sl=sl+'ay'
else:
    d=sl[0]
    sl=sl.replace(sl[0],'')
    sl=sl+d+'ay'
print(sl)