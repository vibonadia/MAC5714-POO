#from student import Student
from people import People
import numpy as np

class Student(People):

    def __init__(self, name, age):
        People.__init__(self, name, age)

    def print_name(self):
        print 'Student', name

    @staticmethod
    def arithmetic_mean(results):
        print np.mean(results)

    @staticmethod
    def bad_results(results):
        print filter(lambda x: x < 5, results)

    @classmethod
    def show_max_result(cls):
        print '10'

    def __private_method(self):
        print 'This is a private method.'
