import main
import Validator
import pandas as pd
import matplotlib.pyplot as plt


def menu():
    print('to enter Data Base with file enter                       1')
    print('to search in Data Base enter                             2')
    print('to sort Data Base enter                                  3')
    print('to save Data Base into file enter                        4')
    print('to show Data Base enter                                  5')
    print('to add new Worker into Data Base enter                   6')
    print('to delete Worker from Data Base enter                    7')
    print('to change Worker in Data Base enter                      8')
    print('to create diagram of departments in Data Base enter      9')
    print('to exit menu enter                                       0')
    switch = input('write your choice: ')
    return switch


def fillDB(DB, filepath='file.csv'):
    filepath = Validator.Validator.get_file_name('')
    main.fill_DB(DB, filepath)


def searchDB(DB):
    name = Validator.Validator.get_parameter('')
    value = Validator.Validator.get_name('')
    result = DB.search(name, value)
    for elem in result:
        print(elem)


def sortDB(DB):
    name = Validator.Validator.get_parameter('')
    DB.sort(name)


def saveDB(DB):
    filename = Validator.Validator.get_file_name('')
    main.save_DB(DB, filename)


def showDB(DB):
    main.show_DB(DB)


def createWorkerKeyboard(name=None, surname=None, department=None, salary=None, set_limit=True):
    if name is None:
        name = input('enter name: ')
    if surname is None:
        surname = input('enter surname: ')
    if department is None:
        department = input('enter department: ')
    if salary is None:
        salary = input('enter salary: ')
    # validate
    res = main.Worker.create_worker(name, surname, department, salary, set_limit)
    return res


def addWorker(DB, name=None, surname=None, department=None, salary=None, set_limit=True):
    res = createWorkerKeyboard(name, surname, department, salary, set_limit)
    if type(res) is main.Worker:
        DB.add(res)
    else:
        print('Errors: ')
        print(res)


def deleteWorker(DB):
    _id = int(Validator.Validator.get_natural_number(''))
    DB.delete(_id)


def changeWorker(DB):
    _id = int(Validator.Validator.get_natural_number(''))
    res = createWorkerKeyboard()
    DB.change_worker(_id, res)


def showDepartmentDiagram(DB):
    main.save_DB(DB)
    df = pd.read_csv('output.csv')
    grouped_by_department = df.groupby(['department'])['id'].count()
    total = df['id'].count()
    # grouped_by_department.plot(kind='pie')
    plt.pie(
        x = grouped_by_department,
        labels=grouped_by_department.index,
        autopct=lambda p: '{:.0f}'.format(p * total / 100),
    )
    plt.show()
