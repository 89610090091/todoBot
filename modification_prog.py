HELP = """help - справка 
add - добавление задач 
show - отобразить, что задача добавлена."""

tasks = {
 
}

run = True

while run:
 command = input('Введите команду: ')
 if command == 'help':
  print(HELP)
 elif command == 'show':
  print(tasks)
 elif command == 'add':
   date = input('Введите дату: ')
   task = input('Название задачи: ')
   if date in tasks:
     tasks[date].append(task)
   else:
     tasks[date] = []
     tasks[date].append(task)
   print('Задача', task, 'добавлена на дату', date)
 elif command == 'exit':
   break  
 else:
   print('Неизвестная команда')
   break 
print('Спасибо, до свидание!')


  


 


