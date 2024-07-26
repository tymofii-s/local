#Задано 2 кути. Знайти і визначити третій кут.

print('Введіть перший кут')
first_corner = int(input())
print('Введіть другий кут')
second_corner = int(input())
third_corner = 180 - first_corner - second_corner
a = 1
u = ['прямий','гострий','тупий','неозначений']


while first_corner<180 and second_corner<180 and third_corner<180 and a==1 or first_corner<0 or second_corner<0:
    if first_corner<0 or second_corner<0:
        print('Введіть додатні кути!!!')
        forma = u[3]
        break
    elif third_corner == 90:
        forma = u[0]
        a=2
    elif 0<third_corner<90 :
        forma = u[1]
        a=2
    elif 90<third_corner<180:
        forma = u[2]
        a=2
    else:
        print("Третій кут трикутника від'ємний. Його не існує. Ви ввели градусну міру першого або другого кута (або обох кутів) більшу за 90 градусів")
        forma = u[3]
        break

print('Третій кут дорівнює ' +str(third_corner) +'. Кути трикутника: перший кут - (' +str(first_corner) +') другий кут - (' +str(second_corner) +'). Тип ' + forma +'.')
