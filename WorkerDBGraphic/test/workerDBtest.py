from main import *
import unittest


class WorkerTest(unittest.TestCase):
    def testAdd(self):
        # intentionally chosen two identical workers and one different
        # to show that id is set independently of other fields
        worker1 = Worker.create_worker('Max', 'M', 'BE_DEVELOPER', 12301)
        DB = WorkerDB()
        self.assertFalse([worker1] == DB.search('name', 'Max'))
        DB.add(worker1)
        self.assertTrue([worker1] == DB.search('name', 'Max'))

    def testDelete(self):
        worker1 = Worker.create_worker('Ivan', 'I', 'FE_DEVELOPER', 12512)
        DB = WorkerDB()
        self.assertFalse([worker1] == DB.search('surname', 'I'))
        DB.add(worker1)
        self.assertTrue([worker1] == DB.search('surname', 'I'))
        DB.delete(worker1)
        self.assertFalse([worker1] == DB.search('surname', 'I'))

    def testDeleteLen(self):
        worker1 = Worker.create_worker('Alina', 'A', 'BE_DEVELOPER', 12512)
        DB = WorkerDB()
        self.assertTrue(DB.isEmpty())
        DB.add(worker1)
        self.assertFalse(DB.isEmpty())
        DB.delete(worker1)
        self.assertTrue(DB.isEmpty())

    def testChange(self):
        worker1 = Worker.create_worker('Igor', 'I', 'FE_DEVELOPER', 21345)
        worker2 = Worker.create_worker('Mykhailo', 'M', 'DEVOPS', 54231)
        DB = WorkerDB()
        DB.add(worker1)
        self.assertTrue([worker1] == DB.search('name', 'Igor'))
        self.assertFalse([worker2] == DB.search('name', 'Mykhailo'))
        DB.change_worker(worker1, worker2)
        self.assertFalse([worker1] == DB.search('name', 'Igor'))
        self.assertTrue([worker2] == DB.search('name', 'Mykhailo'))

    def testSort(self):
        worker1 = Worker.create_worker('Anton', 'A', 'FE_DEVELOPER', 32140)
        worker2 = Worker.create_worker('Evgeniy', 'E', 'DEVOPS', 20000)
        worker3 = Worker.create_worker('Mykyta', 'M', 'BE_DEVELOPER', 10501)
        DB1 = WorkerDB()
        DB2 = WorkerDB()
        DB1.add(worker1)
        DB1.add(worker2)
        DB1.add(worker3)
        DB2.add(worker2)
        DB2.add(worker3)
        DB2.add(worker1)
        self.assertFalse(DB1 == DB2)
        DB1.sort('salary')
        DB2.sort('salary')
        self.assertTrue(DB1 == DB2)







