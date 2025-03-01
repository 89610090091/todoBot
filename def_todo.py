
HELP = """
help - справка 
add - добавление задач 
show - отобразить, что задача добавлена
random - добавлять случайную задачу на дату сегодня"""

RANDOM_TASK = 'Выполнить задачи из плана работ' 

tasks = {
 
}

run = True


def add_todo(date, task): 
  if date in tasks:
    tasks[date].append(task)
  else: 
    task[date] = []
    tasks[date].append(task)  
  print('Задача', task, 'добавлена на дату', date)

while run:
 command = input('Введите команду: ')
 if command == 'help':
  print(HELP)
 elif command == 'show':
  date = input('Введите дату задачи ')
  if date in tasks:
   for task in tasks[date]:
    print('-> ', task)
  else:
     print('Такой даты нет')
 elif command == 'add':
   date = input('Введите дату: ')
   task = input('Название задачи: ')
   add_todo(date, task)
 elif command == 'random':
   add_todo(date, RANDOM_TASK)
 elif command == 'exit':
   break  
 else:
   print('Неизвестная команда')
   break 
print('До свидание!')