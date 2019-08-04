#!/usr/bin/python

import unittest

loader = unittest.TestLoader()
suite = loader.discover('tests/unit')
print('found ' + str(suite.countTestCases()) + ' test cases')
unittest.TextTestRunner().run(suite)