import tkinter as tk

import interface
from main import *


class Application:
    def __init__(self, root, DB, input_file, output_file):
        self.root = root
        self.DB = DB
        self.input_file = input_file
        self.output_file = output_file

        self.root.title('Worker Graphic Interface')
        self.root.geometry("650x500")

        # fillDB
        fillDB_button = tk.Button(root, text="Fill",
                                  command=self.fillDB)
        fillDB_button.grid(column=0, row=0, sticky=tk.W, pady=2)
        # fillDB_button.pack()
        # saveDB
        saveDB_button = tk.Button(root, text="Save",
                                  command=self.saveDB)
        saveDB_button.grid(column=1, row=0, sticky=tk.W, pady=2)
        # saveDB_button.pack()
        # showDB
        showDB_button = tk.Button(root, text="Show",
                                  command=self.showDB)
        showDB_button.grid(column=2, row=0)
        # showDB_button.pack()
        # showDiagram
        showDiagram_button = tk.Button(root, text="ShowDiagram",
                                  command=self.ShowDiagramDB)
        showDiagram_button.grid(column=3, row=0)
        # showDiagram_button.pack()
        # searchDB
        search_button = tk.Button(root, text="Search",
                                       command=self.searchDB)
        search_button.grid(column=4, row=0)
        # search_button.pack()

        # sortDB
        sort_button = tk.Button(root, text="Sort",
                                  command=self.sortDB)
        sort_button.grid(column=5, row=0)
        # sort_button.pack()

        # add new worker
        add_worker_button = tk.Button(root, text="Add",
                                command=self.addWorker)
        add_worker_button.grid(column=6, row=0)
        # add_worker_button.pack()

        # delete worker
        delete_worker_button = tk.Button(root, text="Delete",
                                      command=self.deleteWorker)
        delete_worker_button.grid(column=7, row=0)
        # delete_worker_button.pack()

        # change worker
        change_worker_button = tk.Button(root, text="Change",
                                         command=self.changeWorker)
        change_worker_button.grid(column=8, row=0)
        # change_worker_button.pack()

        change_input_file_button = tk.Button(root, text="Change Input file",
                                         command=self.changeInputFile)
        change_input_file_button.grid(column=9, row=0)

        change_output_file_button = tk.Button(root, text="Change Output file",
                                             command=self.changeOutputFile)
        change_output_file_button.grid(column=10, row=0)

        self.output_text = tk.Text(self.root)
        self.output_text.grid(column=0, columnspan=11, row=3)
        # self.output_text.pack()

    def flush(self):
        self.output_text.delete('1.0', tk.END)

    def searchDB(self):
        self.flush()
        newWindow = tk.Toplevel(self.root)

        # sets the title of the
        # Toplevel widget
        newWindow.title("Search Window")

        # sets the geometry of toplevel
        newWindow.geometry("200x200")

        self.newEntry = tk.Entry(newWindow)
        self.newEntry.pack()

        # Dropdown menu options
        self.options = [
            'name',
            'surname',
            'department',
            'salary'
        ]

        # datatype of menu text
        self.clicked = tk.StringVar()

        # initial menu text
        self.clicked.set("name")

        # Create Dropdown menu
        self.drop = tk.OptionMenu(newWindow, self.clicked, *self.options)
        self.drop.pack()


        # searchDB
        input_search_button = tk.Button(newWindow, text="Search",
                                  command=self.inputSearchDB)
        input_search_button.pack()

    def inputSearchDB(self):
        self.flush()

        self.output_text.insert(tk.END, interface.searchDBApplication(
            self.DB, self.clicked.get(), self.newEntry.get()))

    def sortDB(self):
        newWindow = tk.Toplevel(self.root)

        # sets the title of the
        # Toplevel widget
        newWindow.title("Sort Window")

        # sets the geometry of toplevel
        newWindow.geometry("200x200")

        # Dropdown menu options
        self.options = [
            'name',
            'surname',
            'department',
            'salary'
        ]

        # datatype of menu text
        self.clicked = tk.StringVar()

        # initial menu text
        self.clicked.set("name")

        # Create Dropdown menu
        self.drop = tk.OptionMenu(newWindow, self.clicked, *self.options)
        self.drop.pack()

        input_sort_button = tk.Button(newWindow, text="Sort",
                                        command=self.inputSortDB)
        input_sort_button.pack()

    def inputSortDB(self):
        self.flush()
        self.output_text.insert(tk.END,interface.sortDBApplication(self.DB, self.clicked.get()))

    def addWorker(self):
        newWindow = tk.Toplevel(self.root)

        # sets the title of the
        # Toplevel widget
        newWindow.title("Add Worker Window")

        # sets the geometry of toplevel
        newWindow.geometry("500x500")

        self.newEntry = tk.Entry(newWindow, width=40)
        self.newEntry.insert(0, "Name, Surname, Department, Salary")
        self.newEntry.pack()

        input_add_worker_button = tk.Button(newWindow, text="Add Worker",
                                      command=self.inputAddWorker)
        input_add_worker_button.pack()

    def inputAddWorker(self):
        self.flush()
        self.output_text.insert(tk.END, interface.addWorkerApplication(
            self.DB, self.newEntry.get()))

    def deleteWorker(self):
        newWindow = tk.Toplevel(self.root)
        # sets the title of the
        # Toplevel widget
        newWindow.title("Delete Worker Window")

        # sets the geometry of toplevel
        newWindow.geometry("500x500")

        self.newEntry = tk.Entry(newWindow, width=40)
        self.newEntry.insert(0, "Id of worker you want to delete")
        self.newEntry.pack()

        input_add_worker_button = tk.Button(newWindow, text="Delete Worker",
                                      command=self.inputDeleteWorker)
        input_add_worker_button.pack()

    def inputDeleteWorker(self):
        self.flush()
        self.output_text.insert(tk.END, interface.deleteWorkerApplication(
            self.DB, self.newEntry.get()))

    def changeWorker(self):
        newWindow = tk.Toplevel(self.root)
        # sets the title of the
        # Toplevel widget
        newWindow.title("Change Worker Window")

        # sets the geometry of toplevel
        newWindow.geometry("500x500")

        self.newEntryId = tk.Entry(newWindow, width=40)
        self.newEntryId.insert(0, "Id of worker you want to change")
        self.newEntryId.pack()

        self.newEntryWorker = tk.Entry(newWindow, width=40)
        self.newEntryWorker.insert(0, "Name, Surname, Department, Salary")
        self.newEntryWorker.pack()

        input_change_worker_button = tk.Button(newWindow, text="Change Worker",
                                      command=self.inputChangeWorker)
        input_change_worker_button.pack()

    def inputChangeWorker(self):
        self.flush()
        self.output_text.insert(tk.END, interface.changeWorkerApplication(
            self.DB, self.newEntryId.get(), self.newEntryWorker.get()))

    def showDB(self):
        self.flush()
        self.output_text.insert(tk.END, DB_to_string(self.DB))

    def ShowDiagramDB(self):
        interface.showDepartmentDiagram(self.DB)

    def fillDB(self):
        self.flush()
        self.output_text.insert(tk.END,interface.fillDBApplication(self.DB, self.input_file))

    def insert_value_in_entry(self):
        self.entry.get()
        self.root.title(self.entry.get())

    def saveDB(self):
        interface.saveDB(self.DB, self.output_file)

    def changeInputFile(self):
        newWindow = tk.Toplevel(self.root)
        newWindow.title("Change Input File Window")
        newWindow.geometry("500x500")

        self.newEntry = tk.Entry(newWindow, width=40)
        self.newEntry.insert(0, "enter new input file")
        self.newEntry.pack()

        input_change_file_button = tk.Button(newWindow, text="Change",
                                               command=self.inputChangeFile)
        input_change_file_button.pack()

    def inputChangeFile(self):
        self.flush()
        new_input_file = self.newEntry.get()
        if Validator.Validator.validate_file_name(new_input_file):
            self.input_file = new_input_file
            self.output_text.insert(tk.END,f'input file was successfully changed to {new_input_file}')
        else:
            self.output_text.insert(tk.END,f'no file with name {new_input_file} was found')

    def changeOutputFile(self):
        newWindow = tk.Toplevel(self.root)
        newWindow.title("Change Output File Window")
        newWindow.geometry("500x500")

        self.newEntry = tk.Entry(newWindow, width=40)
        self.newEntry.insert(0, "enter new output file")
        self.newEntry.pack()

        output_change_file_button = tk.Button(newWindow, text="Change",
                                               command=self.outputChangeFile)
        output_change_file_button.pack()

    def outputChangeFile(self):
        self.flush()
        new_output_file = self.newEntry.get()
        if Validator.Validator.validate_file_name(new_output_file):
            self.output_file = new_output_file
            self.output_text.insert(tk.END,f'output file was successfully changed to {new_output_file}')
        else:
            self.output_text.insert(tk.END,f'no file with name {new_output_file} was found')


DB = WorkerDB()

root = tk.Tk()
app = Application(root, DB, 'file.csv', 'output.csv')
root.mainloop()
