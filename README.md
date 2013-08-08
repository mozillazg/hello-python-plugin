#尝试实现简单的插件功能

    $ python main.py -h
    usage: main.py [-h] [--enable PLUGINS]

    optional arguments:
    -h, --help        show this help message and exit
    --enable PLUGINS  enable some plugins (default: [])

默认输出：

    $ python main.py
    Default: test plugin.

启用插件 foo:

    $ python main.py --enable foo
    Default: test plugin.
    Plugin foo: test plugin.

启用插件 foo, bar:

    $ python main.py --enable foo --enable bar
    Default: test plugin.
    Plugin bar: test plugin.
    Plugin foo: test plugin.
