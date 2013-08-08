#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse

from utils import import_string, find_modules


def parse_args():
    """解析命令行参数."""
    parser = argparse.ArgumentParser()
    parser.add_argument('--enable', action='append', dest='plugins',
                        default=[], help='enable some plugins (default: [])')
    return parser.parse_args()


def main():
    args = parse_args()
    text = 'test plugin.'
    print 'Default: %s' % text

    modules = find_modules('plugins')
    for module in modules:
        enabled_plugins = ['plugins.' + x for x in args.plugins]
        if module in enabled_plugins:
            plugin = import_string(module)
            print plugin.output(text)

if __name__ == '__main__':
    main()
