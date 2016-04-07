"""Staxing's module file."""

from .helpers import Helper, Admin, Student, Teacher, User, ContentQA
from .assignment import Assignment
from .page_load import SeleniumWait

if __name__ == '__main__':
    a = Helper
    b = Assignment
    c = Admin
    d = Student
    e = Teacher
    f = User
    g = ContentQA
    h = SeleniumWait
