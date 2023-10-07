# testunitpython
Apprendre les  tests unitaires python



'''python 


import unittest
from unittest.mock import patch

from employee import Employee 


class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print('setupClass')


    @classmethod
    def tearDownClass(cls) -> None:
        print('tearDownClass')



    def setUp(self) -> None:
        print('set up')
        self.emp_1 = Employee('donald', 'tedom', 50000)

        self.emp_2 = Employee('franc', 'smith', 60000)


    def tearDown(self) -> None:
        print('\n tear down')    


    def test_email(self):


        self.emp_1.first = 'nou'
        self.emp_2.first = 'jan'


        self.assertEqual(self.emp_1.email, 'nou.tedom@email.com')
        self.assertEqual(self.emp_2.email, 'jan.smith@email.com')



     
    def test_fullname(self):

        self.assertEqual(self.emp_1.fullname, 'donald tedom')
        self.assertEqual(self.emp_2.fullname, 'franc smith')


        self.emp_1.first = 'nou'
        self.emp_2.last = 'jan'

        self.assertEqual(self.emp_1.fullname, 'nou tedom')
        self.assertEqual(self.emp_2.fullname, 'franc jan')
     




    def test_apply_raise(self):
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)


    def test_monthly_schedule(self):

        with patch('employee.requests.get') as mocked_get:

            mocked_get.return_value.ok = True 
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/tedom/May')

            self.assertEqual(schedule, 'Success')


            mocked_get.return_value.ok = False 
            mocked_get.return_value.status_code = 400

            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/smith/June')

            self.assertEqual(schedule, 400)
        


if __name__ == '__main__':
    unittest.main()



'''
