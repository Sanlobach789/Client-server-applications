# task_1______________________________________________
import locale
import subprocess

words_1 = ['разработка', 'сокет', 'декоратор']
for word in words_1:
    print(word)
    print(type(word))
    unicode_str = word.encode('utf-8')
    print(unicode_str)
    print(type(unicode_str))
print('__________________________________________________________\n\n')
# task_2________________________________________________
# words_2 = ['class', 'function', 'method']
word_1 = b'class'
print(word_1)
print(type(word_1))
print(len(word_1))

word_2 = b'function'
print(word_2)
print(type(word_2))
print(len(word_2))

word_3 = b'method'
print(word_3)
print(type(word_3))
print(len(word_3))

print('__________________________________________________________\n\n')
# task_3__________________________________________________
# «attribute», «класс», «функция», «type»
words_3 = ['attribute', 'класс', 'функция', 'type']
for word in words_3:
    print(bytes(word, encoding='utf-8'))
print('Нельзя представить в байтовом типе: класс и функция')

print('__________________________________________________________\n\n')

# task_4__________________________________________________
# «разработка», «администрирование», «protocol», «standard»
words_4 = ['разработка', 'администрирование', 'protocol', 'standard']
for word in words_4:
    word_enc = word.encode('utf-8')
    print(word_enc)
    print(word_enc.decode('utf-8'))
    print('\n')
print('__________________________________________________________\n\n')

# task_5__________________________________________________
ping_args = [['ping', 'yandex.ru'], ['ping', 'youtube.com']]

for args in ping_args:
    subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
    for line in subproc_ping.stdout:
        line = line.decode('cp866').encode('utf-8')
        print(line.decode('utf-8'))

# task_6__________________________________________________
test_file = 'test_file.txt'
def_coding = locale.getpreferredencoding()
print(def_coding)

with open(test_file, encoding='utf-8') as f_n:
    for el_str in f_n:
        print(el_str)