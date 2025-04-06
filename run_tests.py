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
from tests.homework.g_lists_and_tuples import tests_lists_and_tuples

suite = unittest.TestLoader().loadTestsFromModule(tests_lists_and_tuples)
unittest.TextTestRunner(verbosity=2).run(suite)
