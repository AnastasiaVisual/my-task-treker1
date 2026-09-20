FILE_NAME = 'task.txt'
#загрузка задач
def load_tasks():
    try:
        with open(FILE_NAME, 'r', encoding='utf-8') as file:
            tasks = file.readlines()
        return [task.strip() for task in tasks]
    except:
        return[]
#сохранение
def save_tasks(tasks):
    with open(FILE_NAME, 'w', encoding='utf-8') as file:
        for task in tasks:
            file.write(task + '\n')
#отображение списка задач
def view_tasks():
    tasks= load_tasks()
    if not tasks:
        print('Список задач пуст')
    else:
        print('\nВаши задачи')
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

#добавление новой задачи 
def add_task():    
    tasks= load_tasks()
    new_task= input('Введите новую задачу: ')
    if new_task.strip():
        tasks.append(new_task.strip())
        save_tasks(tasks)
        print(f'Задача "{new_task}" добавлена')
    else:
        print('Пустая задача не добавлена')

def delete_task():
    tasks=load_tasks()
    if not tasks:
        print('Список задач пуст')
        return

    view_tasks()
    try:
        task_num = int(input('Введите номер задачи для удаления: '))
        if 1<= task_num <=len(tasks):
            removed_task = tasks.pop(task_num -1)
            save_tasks(tasks)
        else:
            print('Неверный номер задачи')
    except ValueError:
        print('Пожалуйста введите число: ') 


#
def main_menu():
    print('\nтрекер задач:')
    print('1. Просмотреть задачи')
    print('2. Добавить задачу')
    print('3. Удалить задачу')
    print('4. Выйти')


def run():
    while True:
        main_menu()
        choise = input('Выберите действие: ')
        if choise =='1':
            view_tasks()
        elif choise =='2':
            add_task()
        elif choise =='3':
            delete_task()
        elif choise =='4':
            print('До встречи!')
            break

if __name__ == '__main__':
    run()