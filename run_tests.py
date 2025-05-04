import unittest
'''
the file in /tests/homework/b_in_proc_out/tests_in_proc_out
has the test functions
'''

from tests.homework.b_in_proc_out import tests_in_proc_out
suite = unittest.TestLoader().loadTestsFromModule(tests_in_proc_out)
unittest.TextTestRunner(verbosity=2).run(suite)

import unittest
from tests.homework.c_decisions import tests_decisions
suite = unittest.TestLoader().loadTestsFromModule(tests_decisions)
unittest.TextTestRunner().run(suite)

from tests.homework.d_repetition import tests_repetition 
suite = unittest.TestLoader().loadTestsFromModule(tests_repetition)

import unittest
from tests.homework.i_dictionaries_sets import tests_dictionaries_and_sets

suite = unittest.TestLoader().loadTestsFromModule(tests_dictionaries_and_sets)
unittest.TextTestRunner(verbosity=2).run(suite)

import unittest
from tests.homework.j_classes import tests_classes

suite = unittest.TestLoader().loadTestsFromModule(tests_classes)
unittest.TextTestRunner().run(suite)
