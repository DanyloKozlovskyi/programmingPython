from main import *
import unittest


class WorkerTest(unittest.TestCase):
    def testUniqueId(self):
        # intentionally chosen two identical workers and one different
        # to show that id is set independently of other fields
        worker1 = Worker.create_worker('Max', 'M', 'BE_DEVELOPER', 12301)
        worker2 = Worker.create_worker('Dima', 'D', 'DEVOPS', 10000)
        corrupted_worker = Worker.create_worker('Dim5a', 'D', 'DEVOPS', '100a00')
        worker3 = Worker.create_worker('Dima', 'D', 'DEVOPS', 10000)
        self.assertNotEqual(worker1, worker2)
        self.assertNotEqual(worker2, worker3)
        self.assertNotEqual(worker1, worker3)

    def testStopIterationId(self):
        # intentionally chosen false to show that if we don't want generator to
        # move values further it will return StopIterationError
        with self.assertRaises(StopIteration):
            Worker.create_worker('Max', 'M', 'BE_DEVELOPER', 12301, False)
            Worker.create_worker('Max', 'M', 'BE_DEVELOPER', 12301, False)