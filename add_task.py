
HELP = """help - справка 
add - добавление задач 
show - отобразить, что задача добавлена."""

today = [] 
tomorrow = [] 
other = []

run = True

while run:
 command = input('Введите команду: ')
 if command == 'help':
  print(HELP)
 elif command == 'show':
  print('today', today)
  print('tomorrow', tomorrow)
  print('other', other)
  break
  print(tasks)
 elif command == 'add':
  task = input('Введите задачу: ')
  date = input('введите дату выполнения: ')
  if date == 'today':
   today.append(task) 
  elif date == 'tomorrow':
   tomorrow.append(task)
  elif date == 'other':
   other.append(task)    
 elif command == 'exit':
   print("Спасибо за использование! До свидания!")
   break
 else: 
  print('Неизвестная команда, досвидание!')
  break
  


 


