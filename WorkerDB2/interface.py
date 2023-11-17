import main
import Validator


def menu():
    print('to enter Data Base with file enter                  1')
    print('to search in Data Base enter                        2')
    print('to sort Data Base enter                             3')
    print('to save Data Base into file enter                   4')
    print('to show Data Base enter                             5')
    print('to add new Worker into Data Base enter              6')
    print('to delete Worker from Data Base enter               7')
    print('to exit menu enter                                  0')
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


def addWorker(DB, name=None, surname=None, department=None, salary=None, set_limit=True):
    if name is None:
        name = input('enter name: ')
    if surname is None:
        surname = input('enter surname: ')
    if department is None:
        department = input('enter department: ')
    if salary is None:
        salary = input('enter salary: ')
    # validate
    res = Validator.Validator.validateWorker(name, surname, department, salary)
    if len(res) == 0:
        if set_limit:
            main.Worker.setLimit()
        try:
            new_worker = main.Worker(name, surname, department, salary)
            DB.add(new_worker)
        except Exception as exc:
            print(f'StopIteration exception was caught')


    else:
        print('Errors: ')
        print(res)


def deleteWorker(DB):
    _id = int(Validator.Validator.get_natural_number(''))
    DB.delete(_id)




