duration=int(input('Введите продолжительность промежутка времени в секундах '))

days=duration//86400
hours=(duration%86400)//3600
minutes=((duration%86400)%3600)//60
seconds=((duration%86400)%3600)%60

if duration>=86400:
    print(days,' дн ',hours,' час ',minutes,' мин ',seconds,' сек')
elif duration>=3600:
    print(hours,' час ',minutes,' мин ',seconds,' сек')
elif duration>=60:
    print(minutes, ' мин ', seconds, ' сек')
else: print(seconds, ' сек')
