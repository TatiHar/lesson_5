# задание 1
my_file = open('list_1.txt', 'w')
line = input('Введите текст \n')
while line:
    my_file.writelines(line)
    line = input('Введите текст \n')
    if not line:
        break
my_file.close()
my_file = open('list_1.txt', 'r')
file = my_file.readlines()
print(file)
my_file.close()

# задание 2
for line in open("list_2.txt").readlines():
    print(line.split())
    print(len(line))

# задание 3
with open('list_3.txt', 'r') as my_file:
    sal = []
    poor = []
    my_list = my_file.read().split('\n')
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
           poor.append(i[0])
        sal.append(i[1])
print(f'Оклад меньше 20.000 {poor}, средний оклад {sum(map(int, sal)) / len(sal)}')

# задание 4
ru = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
file = []
with open('text_1.txt', 'r') as new_file:
    for i in new_file:
        i = i.split(' ', 1)
        file.append(ru[i[0]] + '  ' + i[1])
    print(file)
with open('text_2.txt', 'w') as new_file_one:
    new_file_one.writelines(file)
new_file.close()

# задание 5
my_file = open('my_list_2.txt', 'w')
line = input('Введите текст \n')
print(len(line))

# задание 6
with open('list.txt', 'r+') as f:
    for line in f.readlines():
        sub = ['Информатика', 'Физика', 'Физкультура']
        line = input('Введите название предмета:')
        if line == sub[0]:
            print(f'{sum(map(float, filter(lambda x: x.isdigit(),(line[0]))))}')
        elif line == sub[1]:
            print(f'{sum(map(float, filter(lambda x: x.isdigit(), (line[1]))))}')
        else:
            print(f'{sum(map(float, filter(lambda x: x.isdigit(),(line[2]))))}')
# не получилось реализовать задание. Это мои мысли по поводу этого задания.

# задание 7
import json
profit = {}
pr = {}
prof = 0
prof_aver = 0
i = 0
with open('file_7.txt', 'r') as file:
    for line in file:
        name, firm, earning, damage = line.split()
        profit[name] = int(earning) - int(damage)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
        print(f'Прибыль средняя - {prof_aver:.2f}')
    else:
        print(f'Прибыль средняя - отсутсвует. Все работают в убыток')
    pr = {'средняя прибыль': round(prof_aver)}
    profit.update(pr)
    print(f'Прибыль каждой компании - {profit}')

with open('file_7.json', 'w') as write_js:
    json.dump(profit, write_js)

    js_str = json.dumps(profit)
    print(f'Создан файл с расширением json со следующим содержимым: \n '
          f' {js_str}')
