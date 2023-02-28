"""
    pathlib:python标准库，路径处理库，比os标准库更好用，可以方便获取文件或者目录的名字、文件后缀名等，
        不同系统上路径的表示方式，pathlib可以同时兼容windows和linux风格的路径风格
    PureWindowsPath：这种路径风格是在windows系统下使用的；
    PurePosixPath：这种路径风格是在非windows系统下使用的；
    PurePath：是PureWindowsPath和PurePosixPath的父类
    直接只用PurePath和Path，PurePath只包含路径字符串处理 Path继承自PurePath，除了PurePath的功能，还提供了文件读写
    PurePath可以自动根据系统来确定PureWindowsPath或者PurePosixPath(非windows系统)
    更多示例:https://docs.python.org/zh-cn/3/library/pathlib.html
"""

import pathlib

c0 = r'D:\Projects\KnowledgeFusion\backup\corpus_root_for_fusion_按类别'
c0 = r'D:\Projects\KnowledgeFusion/backup\corpus_root_for_fusion_按类别'
c0 = r'D:/Projects/KnowledgeFusion/backup/corpus_root_for_fusion_按类别'
c0 = r'D:\Projects\KnowledgeFusion/backup\corpus_root_for_fusion_按类别/'
c0 = r'D:\Projects\KnowledgeFusion/backup\corpus_root_for_fusion_按类别'
c = pathlib.PurePath(c0)  # PurePath(c0)可以自动根据系统来确定PureWindowsPath或者PurePosixPath(非windows系统)
c1 = c.parent
c2 = c.name
print()


c0 = r'D:\Projects\KnowledgeFusion\backup\command.txt'
c0 = r'D:\Projects\KnowledgeFusion/backup\command.txt'
c0 = r'D:\Projects\KnowledgeFusion\backup/command.txt'
c0 = r'D:/Projects/KnowledgeFusion/backup/command.txt'
c = pathlib.PurePath(c0)
c1 = c.parent
c2 = c.name
print()


# ######################################################################################################################
"""
Path.exists()
    此路径是否指向一个已存在的文件或目录
    Path('.').exists()
    True
    Path('setup.py').exists()
    True
    Path('/etc').exists()
    True
    Path('nonexistentfile').exists()
    False
Path.is_dir()
    如果路径指向一个目录（或者一个指向目录的符号链接）则返回 True，如果指向其他类型的文件则返回 False。
        当路径不存在或者是一个破损的符号链接时也会返回 False；其他错误（例如权限错误）被传播。
Path.is_file()
    如果路径指向一个正常的文件（或者一个指向正常文件的符号链接）则返回 True，如果指向其他类型的文件则返回 False。
Path.glob(pattern)
    sorted(Path('.').glob('*.py'))
    [PosixPath('pathlib.py'), PosixPath('setup.py'), PosixPath('test_pathlib.py')]
    sorted(Path('.').glob('*/*.py'))
    [PosixPath('docs/conf.py')]
"""

# ######################################################################################################################