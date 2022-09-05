#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""--- test_console.py ---

@author   Hank Adler
@version  0.1.0
@license  MIT

--- Copyright (C) 2017 Hank Adler ---
"""


import datetime
import os
import sys
import unittest

import console
import header
import logger


class Test(unittest.TestCase):
    """Tests Console ask() and select() with various arguments."""

    name = 'console'
    version = header.getVersion(
        ''.join(console.__path__) + '/' + name + '.py'
    )
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    logger = logger.get(__name__, '%s-%s-unittest-%s' % (name, version, date))
    stdin = sys.stdin
    console = console.Console()
    result = unittest.TestResult()

    # Override
    def setUp(self):
        with open('input.txt', 'w') as fh:
            pass
        sys.stdin = open('input.txt', 'r')
        print()
        self.logger.info('%s' % '-' * 70)

    # Override
    def tearDown(self):
        sys.stdin.close()
        sys.stdin = self.stdin
        os.remove('input.txt')
        print()
        if self.result.wasSuccessful():
            self.logger.info('RESULT: PASS')
        else:
            self.logger.info('RESULT: FAIL')

    def test_ask_without_keywords(self):
        self.logger.info("  TEST: console.ask('Enter name: ')")
        with open('input.txt', 'w') as fh:
            fh.write('Henry')
        print()
        name = self.console.ask('Enter name: ')
        print('Henry')
        print()
        self.logger.info('        INPUT  = Henry')
        self.logger.info('        OUTPUT = %s' % name)
        self.assertEqual(name, 'Henry')

    def test_ask_with_keyword_default_and_value(self):
        self.logger.info(
            "  TEST: console.ask('Enter name: ', default='Aguila')",
        )
        with open('input.txt', 'w') as fh:
            fh.write('Henry')
        print()
        name = self.console.ask('Enter name: ', default='Aguila')
        print('Henry')
        print()
        self.logger.info('        INPUT  = Henry')
        self.logger.info('        OUTPUT = %s' % name)
        self.assertEqual(name, 'Henry')

    def test_ask_with_keyword_default_and_no_value(self):
        self.logger.info(
            "  TEST: console.ask('Enter name: ', default='Aguila')",
        )
        with open('input.txt', 'w') as fh:
            fh.write('\n')
        print()
        name = self.console.ask('Enter name: ', default='Aguila')
        print('')
        print()
        self.logger.info('        INPUT  = ')
        self.logger.info('        OUTPUT = %s' % name)
        self.assertEqual(name, 'Aguila')

    def test_ask_with_keyword_type_int(self):
        self.logger.info("  TEST: console.ask('Enter integer: ', type=int)")
        with open('input.txt', 'w') as fh:
            fh.write('1')
        print()
        integer = self.console.ask('Enter integer: ', type=int)
        print('1')
        print()
        self.logger.info('        INPUT  = 1')
        self.logger.info('        OUTPUT = %s' % integer)
        self.assertEqual(integer, 1)

    def test_ask_with_keyword_type_float(self):
        self.logger.info("  TEST: console.ask('Enter number: ', type=float)",)
        with open('input.txt', 'w') as fh:
            fh.write('2.0')
        print()
        number = self.console.ask('Enter number: ', type=float)
        print('2')
        print()
        self.logger.info('        INPUT  = 2')
        self.logger.info('        OUTPUT = %s' % number)
        self.assertEqual(number, 2.0)

    def test_ask_with_keyword_type_bool(self):
        self.logger.info("  TEST: console.ask('Enter boolean: ', type=bool)")
        with open('input.txt', 'w') as fh:
            fh.write('True')
        print()
        boolean = self.console.ask('Enter boolean: ', type=bool)
        print('True')
        print()
        self.logger.info('        INPUT  = True')
        self.logger.info('        OUTPUT = %s' % boolean)
        self.assertEqual(boolean, True)

    def test_ask_with_keyword_type_bool_num(self):
        self.logger.info("  TEST: console.ask('Enter boolean: ', type=bool)")
        with open('input.txt', 'w') as fh:
            fh.write('1')
        print()
        boolean = self.console.ask('Enter boolean: ', type=bool)
        print('1')
        print()
        self.logger.info('        INPUT  = 1')
        self.logger.info('        OUTPUT = %s' % boolean)
        self.assertEqual(boolean, True)

    def test_select_single_item(self):
        self.logger.info(
            "  TEST: console.select('Select color', ['red', 'green', 'blue'])",
        )
        with open('input.txt', 'w') as fh:
            fh.write('3')
        print()
        color = self.console.select(
            'Select color', ['red', 'green', 'blue'],
        )
        print('3')
        print()
        self.logger.info('        INPUT  = 3')
        self.logger.info('        OUTPUT = %s' % color)
        self.assertEqual(color, 'blue')

    def test_select_multiple_items(self):
        self.logger.info(
            "  TEST: console.select('Select colors', ['red', 'green', 'blue'])",
        )
        with open('input.txt', 'w') as fh:
            fh.write('3 2')
        print()
        colors = self.console.select(
            'Select colors', ['red', 'green', 'blue'],
        )
        print('3 2')
        print()
        self.logger.info('        INPUT  = 3 2')
        self.logger.info('        OUTPUT = %s' % colors)
        self.assertEqual(colors, ['blue', 'green'])


if __name__ == '__main__':
    print(__doc__, end='')
    unittest.main()
