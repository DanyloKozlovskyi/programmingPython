import csv
import interface
import Validator
import workerDBtest
import test1

# '
# 1 file.csv
# 1 file.csv


def show_DB(DB):
    for elem in DB:
        print(str(elem))


def dec_sort(func):
    def wrapper(self, name):
        print('DB before sorting: ')
        show_DB(self)
        func(self, name)
        print('DB after sorting: ')
        show_DB(self)
    return wrapper


def dec_search(func):
    def wrapper(self, name, value):
        print(f'you search element with {value} in field {name}')
        result = func(self, name, value)
        return result
    return wrapper


class Worker:
    max_id = 0
    limit_id = max_id + 1

    name = None
    surname = None
    department = None
    salary = None

    @classmethod
    def setLimit(cls, filename=None):
        if filename is None:
            cls.limit_id = cls.max_id + 1
        else:
            with open(filename, 'r', newline='') as csv_file:
                last_line = csv_file.readlines()[-1]
                # + 1 because we don't include last element
                cls.limit_id = int(last_line.split(',')[0]) + 1

    @classmethod
    def generateID(cls):
        for i in range(cls.max_id, cls.limit_id):
            yield i

    def __init__(self, name, surname, department, salary) -> None:
        # everything except id is str
        # self.__id = Worker.max_id + 1
        # *
        res_id = Worker.generateID()
        self.__id = next(res_id)
        Worker.max_id += 1
        self.name = name
        self.surname = surname
        self.department = department
        self.salary = salary

        self.fieldnames = {
            'id': self.__id,
            'name': self.name,
            'surname': self.surname,
            'department': self.department,
            'salary': self.salary
        }

    @classmethod
    def create_worker(cls, name, surname, department, salary, set_limit=True):
        # validate
        res = Validator.Validator.validateWorker(name, surname, department, salary)
        if len(res) == 0:
            if set_limit:
                cls.setLimit()
            try:
                new_worker = cls(name, surname, department, salary)
            except Exception as exc:
                raise StopIteration
            else:
                return new_worker

        return res

    def __eq__(self, _id):
        return self.__id == _id

    def get_fieldname(self, name):
        # may throw
        return self.fieldnames[name]

    def __str__(self):
        all_properties = [str(value) if attr != "fieldnames" else "" for attr, value in vars(self).items()]
        del all_properties[-1]
        return ', '.join(all_properties)

    def __repr__(self):
        # fixed now should print all fields
        return str(self)

    # ?
    def __lst__(self):
        return [self.__repr__().split(',')]

    def asDict(self):
        return self.fieldnames

    @classmethod
    def string_to_worker(cls, string_data):
        data = string_data.split()
        return cls(*data)

    @classmethod
    def string_to_worker_safe(cls, string_data):
        data = string_data.split()
        new_worker = cls.create_worker(*data)
        return new_worker


class WorkerDB:

    def __init__(self) -> None:
        self.lst = []

    def add(self, new_worker):
        self.lst.append(new_worker)

    def delete(self, _id):
        try:
            self.lst.remove(_id)
        except Exception:
            print(f'Worker with id: {_id} is not in Data Base')

    def change_worker(self, old_worker, mod_worker):
        self.lst[self.lst.index(old_worker)] = mod_worker

    def __iter__(self):
        return iter(self.lst)

    def __eq__(self, other):
        return self.lst == other.lst

    @dec_sort
    def sort(self, name):
        self.lst.sort(key=lambda x: x.get_fieldname(name))

    @dec_search
    def search(self, name, value):
        result = filter(lambda x: x.get_fieldname(name) == value, self.lst)
        result = list(result)
        return result

    def isEmpty(self):
        return not len(self.lst)


def fill_DB(DB, file_path='file.csv'):
    Worker.setLimit(file_path)
    with open(file_path, 'r', newline='') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',')
        for row in reader:
            if row["id"].isnumeric():
                interface.addWorker(DB, row["first_name"], row["last_name"], row["department"], row["salary"], set_limit=False)


def save_DB(DB, file_path='output.csv'):
    with open(file_path, 'w', newline='') as csv_file:
        header = ['id', 'name', 'surname', 'department', 'salary']
        writer = csv.DictWriter(csv_file, delimiter=',', fieldnames=header)
        writer.writeheader()
        for worker in DB:
            writer.writerow(worker.asDict())


# DB = WorkerDB()
# fill_DB(DB)
# for wk in DB:
#     print(wk)
# save_DB(DB)
# print()
# DB.sort('name')
# print()
# devops = DB.search('department', 'DEVOPS')
# for item in devops:
#     print(item)
# print()


def main():
    check = str()
    DB = WorkerDB()
    while check != '+' and check != '-':
        check = input('if you want to enter(continue) the program press +, if you want exit press -: ')
        while check == '+':
            switch = interface.menu()
            match switch:
                case '1':
                    interface.fillDB(DB)
                case '2':
                    interface.searchDB(DB)
                case '3':
                    interface.sortDB(DB)
                case '4':
                    interface.saveDB(DB)
                case '5':
                    interface.showDB(DB)
                case '6':
                    interface.addWorker(DB)
                case '7':
                    interface.deleteWorker(DB)
                case '0':
                    check = ''
                case _:
                    print('try again')


if __name__ == '__main__':
    main()
