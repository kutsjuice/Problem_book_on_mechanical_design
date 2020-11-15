# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 20:42:44 2020

@author: Mikhail Kuts
Скрипт для автоматизированной генерации директорий git
"""
import os

import os.path as pt


def opendir(folder):
    print(folder)
    l_dir = os.listdir(folder)
    if 'README.md' in l_dir:
        print('README.md exist')
    else:
        f = open('README.md','w')
        f.close()
    for name in l_dir:
        c_folder = folder + '\\' + name
        if pt.isdir(c_folder) and (name[0]!='.'):
            opendir(c_folder)
            
    

def main():
    c_folder = os.getcwd()
    print(c_folder)
    opendir(c_folder)    
    
if __name__=="__main__":
    main()
    

    

