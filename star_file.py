HELP = """help - справка 
add - добавление задач 
show - отобразить, что задача добавлена."""

tasks = []

run = True

while run:
 command = input('Введите команду: ')
 if command == 'help':
  print(HELP)
 elif command == 'show':
  print(tasks)
 elif command == 'add':
  task = input('Введите задачу: ')
  tasks.append(task)
  print('Задача добавлена')
 else: 
  print('Неизвестная команда, досвидание!')
  break

print('До свидания!')

  


 


