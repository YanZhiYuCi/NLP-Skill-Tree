# -*- coding: UTF-8 -*
import os
import sys

import pathlib

c0 = r'D:\Projects\KnowledgeFusion\backup\corpus_root_for_fusion_按类别'
c0 = r'D:\Projects\KnowledgeFusion/backup\corpus_root_for_fusion_按类别'
c0 = r'D:/Projects/KnowledgeFusion/backup/corpus_root_for_fusion_按类别'
c0 = r'D:\Projects\KnowledgeFusion/backup\corpus_root_for_fusion_按类别/'
c0 = r'D:\Projects\KnowledgeFusion/backup\corpus_root_for_fusion_按类别'
c = pathlib.PurePath(c0)
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