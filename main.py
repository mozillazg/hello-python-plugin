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

    # 找出插件目录下所有的插件
    modules = find_modules('plugins', silent=True)
    for module in modules:
        enabled_plugins = ['plugins.' + x for x in args.plugins]
        # 根据命令行选项 --enable 的值过滤插件
        if module in enabled_plugins:
            # 导入插件
            plugin = import_string(module, silent=True)
            if plugin:
                # 执行约定的每个插件内必须有的函数
                print plugin.output(text)

if __name__ == '__main__':
    main()
