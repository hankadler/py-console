#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""--- console.py ---

A command-line interface.

@author   Hank Adler
@version  0.1.0
@license  MIT

--- Copyright (C) 2017 Hank Adler ---
"""


import inspect
import os
import platform
import sys
import time


class Console:
    """A command-line interface."""

    def __init__(self):
        self._clear_flag = False
        self._silent_flag = False
        self._value_type = None
        self._value_default = None
        self._value = ''

    """clear_flag (bool): Controls clearing screen before prompt."""
    @property
    def clear_flag(self):
        return self._clear_flag
    @clear_flag.setter
    def clear_flag(self, value):
        if not isinstance(value, bool):
            raise TypeError("Wrong type for 'clear', must be %s!" % bool)
        self._clear_flag = value

    """silent_flag (bool): Controls display of error messages."""
    @property
    def silent_flag(self):
        return self._silent_flag
    @silent_flag.setter
    def silent_flag(self, value):
        if not isinstance(value, bool):
            raise TypeError("Wrong type for 'silent', must be %s!" % bool)
        self._silent_flag = value

    """value_type (object): Type imposed on requested value."""
    @property
    def value_type(self):
        return self._value_type
    @value_type.setter
    def value_type(self, value):
        if not inspect.isclass(value):
            raise ValueError("'type' value must be a class!")
        self._value_type = value

    """value_default (object): Default value if None is entered."""
    @property
    def value_default(self):
        return self._value_default
    @value_default.setter
    def value_default(self, value):
        if self.value_type is not None:
            if not isinstance(value, self.value_type):
                raise TypeError("Wrong type for 'default', must be %s!"
                                % self.value_type)
        self._value_default = value

    """value (object): Value entered after prompt."""
    @property
    def value(self):
        return self._value
    @value.setter
    def value(self, value):
        if not value:
            if self.value_default is None:
                raise ValueError
            else:
                value = self.value_default
        if self.value_type is int:
            value = int(value)
        elif self.value_type is float:
            value = float(value)
        elif self.value_type == bool:
            if isinstance(value, str):
                if value.strip() not in ['False', 'True', '0', '1']:
                    raise ValueError
                else:
                    if value == '0' or value == 'False':
                        value = False
                    else:
                        value = True
        self._value = value

    def ask(self, prompt, **kwargs):
        """Asks user for input.

        Parameters:
            prompt (str): Message to display before reading input.

        Returns:
            object: Value entered.
        """
        self.__init__()
        self._parse_args(kwargs)

        while True:
            if self.clear_flag:
                self.clear()
            try:
                self.value = input(prompt)
            except EOFError:
                # Resets sys.stdin.
                sys.stdin = open('/dev/tty')
                print('\r', end='')
            except ValueError:
                if not self.silent_flag:
                    if self.value_type is None:
                        print('ERROR: Value must be entered!')
                    else:
                        print('ERROR: Value must be %s convertible!'
                              % self.value_type)
                    time.sleep(1)
                continue
            break
        return self.value

    def _parse_args(self, kwargs):
        for k,v in kwargs.items():
            if k == 'clear':
                self.clear_flag = True
            elif k == 'silent':
                self.silent_flag = True
            elif k == 'type':
                self.value_type = v
            elif k == 'default':
                self.value_default = v

    def clear(self):
        """Clears console screen."""
        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')

    def select(self, prompt, items, **kwargs):
        """Asks user to select one or more items from a list.

        Parameters:
            prompt (str): Message to display before reading input.
            items (list): List of items to choose from.

        Returns:
            object: Selected item.
        """
        if not items:
            return

        self.__init__()
        self._parse_args(kwargs)

        i = 1
        for item in items:
            prompt += '\n%4s%d. %s' % ('', i, item)
            i += 1
        prompt += '\nChoice(s): '

        values = []
        keep_asking = True
        while keep_asking:
            try:
                if self.clear_flag:
                    self.clear()

                chosen_indexes = input(prompt).split()

                if not chosen_indexes:
                    if self.value_default is None:
                        raise ValueError
                    else:
                        return self.value_default

                chosen_indexes = [int(i)-1 for i in chosen_indexes]

                for index in chosen_indexes:
                    if (0 <= index < len(items)):
                        values.append(items[index])
                        keep_asking = False
                    else:
                        raise ValueError
            except EOFError:
                # Resets sys.stdin.
                sys.stdin = open('/dev/tty')
                print('\r', end='')
            except ValueError:
                if not self.silent_flag:
                    if chosen_indexes:
                        print('ERROR: Choice(s) outside 1 to %d range!'
                              % len(items))
                    else:
                        print('ERROR: Value must be entered!')
                    time.sleep(1)
        if len(values) == 1:
            return values[0]
        else:
            return values


if __name__ == '__main__':
    pass
