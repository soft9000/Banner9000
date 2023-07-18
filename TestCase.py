#! /usr/bin/env python3
import BigChars as banner


if banner.is_char(''):
    raise Exception("Empty string error.")
if not banner.get_char(''):
    raise Exception("Non-empty string error.")
banner.big_print("Python", 1, '#')
banner.big_print(" got", 4, '@')
banner.big_print("Bigger", 2, 'B')
