import csv
import interface


def show_DB(DB):
    for elem in DB:
        print(elem)


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

    name = None
    surname = None
    department = None
    salary = None

    def __init__(self, name, surname, department, salary) -> None:
        # everything not except id is str
        self.__id = Worker.max_id + 1
        Worker.max_id += 1
        self.name = name
        self.surname = surname
        self.department = department
        self.salary = salary

        self.fieldnames = {
            'name': self.name,
            'surname': self.surname,
            'department': self.department,
            'salary': self.salary
        }

    def equals(self, _id):
        return self.__id == _id

    def get_fieldname(self, name):
        # may throw
        return self.fieldnames[name]

    def __repr__(self):
        return f'{self.name}, {self.surname}, {self.department}, {self.salary}'

    # ?
    def __lst__(self):
        return [self.__repr__().split(',')]

    def asDict(self):
        return self.fieldnames

    @classmethod
    def string_to_worker(cls, string_data):
        data = string_data.split()
        return cls(data[0], data[1], data[2], data[3])



class WorkerDB:

    def __init__(self) -> None:
        self.lst = []

    def add(self, new_worker):
        self.lst.append(new_worker)

    def delete(self, old_worker):
        self.lst.remove(old_worker)

    def change_worker(self, index, mod_worker):
        self.lst[index] = mod_worker

    def __iter__(self):
        return iter(self.lst)

    @dec_sort
    def sort(self, name):
        self.lst.sort(key=lambda x: x.get_fieldname(name))

    @dec_search
    def search(self, name, value):
        result = filter(lambda x: x.get_fieldname(name) == value, self.lst)
        result = list(result)
        return result


def fill_DB(DB, file_path='file.csv'):
    with open(file_path, 'r', newline='') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',')
        for row in reader:
            if row["id"].isnumeric():
                DB.add(Worker(row["first_name"], row["last_name"], row["department"], row["salary"]))


def save_DB(DB, file_path='output.csv'):
    with open(file_path, 'w', newline='') as csv_file:
        header = ['name', 'surname', 'department', 'salary']
        writer = csv.DictWriter(csv_file, delimiter=',', fieldnames=header)
        writer.writeheader()
        for worker in DB:
            writer.writerow(worker.asDict())


DB = WorkerDB()
fill_DB(DB)
for wk in DB:
    print(wk)
save_DB(DB)
print()
DB.sort('name')
print()
devops = DB.search('department', 'DEVOPS')
for item in devops:
    print(item)
print()


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
                case '0':
                    check = ''
                case _:
                    print('try again')


if __name__ == '__main__':
    main()
