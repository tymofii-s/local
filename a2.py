print('Якщо хочете перекладати з української на азбуку морзе - нажміть 1, якщо навпаки - нажміть 2')
ukr_morze = int(input())
morze_mova = ['.-','-...','.--','....','-..','.','..-..','...-','--..','-.--','..','.---.','.---',
          '-.-','.-..','--','-.','---','.--.','.--.','.-.','...','-','..-','..-.','----','-.-.','---.','--.-','--.--','-..-','..--','.-.-',]
ukr_mova = ['а','б','в','г','д','е','є','ж','з','и','і','ї','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ь','ю','я']

if ukr_morze == 1:
    u = 0
    counter1 = []
    counter2 = []
    print('Введіть текст...')
    text = list(input())
    a = len(text)
    b = 0
    c = 0
    #print(text, a)
    while u < a-1:
        if text[c] == ukr_mova[b]:
            text[c] = morze_mova[b]
            с = c + 1
            b=0
            #print(1, ' с=' + str(c))
            
        else:
            b = b + 1
            #print(2, ' с=' + str(c))
            u+=1
    print(text)
else:
    result = []
    print('Введіть текст...')
    text = list(input())
    for i in range(len(text)):
        index = morze_mova.index(text[i])
        result.append(ukr_mova[index])
    print(result)
