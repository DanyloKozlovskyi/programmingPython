import main
import Validator


def menu():
    print('to enter Data Base with file enter                  1')
    print('to search in Data Base enter                        2')
    print('to sort Data Base enter                             3')
    print('to save Data Base into file enter                   4')
    print('to show Data Base enter                             5')
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

