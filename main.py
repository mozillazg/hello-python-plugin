#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils import import_string, find_modules


def main():
    text = 'test plugin.'
    print 'Default: %s' % text

    modules = find_modules('plugins')
    for module in modules:
        plugin = import_string(module)
        print plugin.output(text)

if __name__ == '__main__':
    main()
