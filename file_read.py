with open('referat.txt', 'r', encoding='utf-8') as reading_file:
    text = reading_file.read()
#    text = text.upper()            # to convert the text to upper case
    print(text)

words = len(text.split())
print(words)            # 163 words as a result


#with open('referat_w.txt', 'w', encoding='utf-8') as writting_file:
#    writting_file.write('Пропал текст реферата!')

#with open('referat_w.txt', 'a', encoding='utf-8') as writting_file:
#    writting_file.write('Пропал текст реферата!\n')
#    writting_file.write('\t Проверьте файл!')