import csv

get_answer = [
    {'Привет!': 'Привет!',
    'Как ты?': 'Лучше всех!',
    'Пока!': 'Увидимся!'}
]

with open('get_answer_scv.csv', 'w', encoding='utf-8') as new_file:
    fields = ['Привет!', 'Как ты?', 'Пока!']
    writer = csv.DictWriter(new_file, fields, delimiter='\n')
#    writer.writeheader()
    for answer in get_answer:
        writer.writerow(answer)

# При простом открытии файла (не через "Получение внешних данных") 
# киллица не читается (латиница открывается  спервого раза). 
# Через "Получение внешних данных" открываются оба варианта.

#import csv

#get_answer = [
#    {'Hello!': 'Hello!',
#    'How are you doing?': 'Fine!',
#    'See you soon!': 'Bye!'}
#]

#with open('get_answer.csv', 'w') as new_file:
#    fields = ['Hello!', 'How are you doing?', 'See you soon!']
#    writer = csv.DictWriter(new_file, fields, delimiter=';')
#    for answer in get_answer:
#        writer.writerow(answer)