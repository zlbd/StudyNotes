#!/usr/bin/python
# coding:utf-8
# author:zlbd

import os, io, chardet

def fencode(filename):
    ret = 'utf-8'
    if os.path.exists(filename):
        with open(filename, 'rb') as f:
            c = chardet.detect(f.read())
            ret = c['encoding']
            if ret == 'ascii':
                ret = 'utf-8'
    return ret


def fread(filename):
    txt = ''
    fcode = fencode(filename)
    f = io.open(filename, mode = 'rt', encoding=fcode)
    txt = f.read()
    f.close()
    return txt


def fwrite(filename, txt):
    fcode = fencode(filename)
    #print("wirte file encode:" + fcode)
    f = io.open(filename, mode = 'wt', encoding=fcode)
    f.write(txt)
    f.close()


def freplace(oldfile, s1, s2, newfile = ''):
    if newfile == '':
        newfile = oldfile

    fcode = 'utf-8'
    if os.path.exists(newfile):
        fcode = fencode(newfile)
    else:
        fcode = fencode(oldfile)

    txt = fread(oldfile)
    txtNew = txt.replace(s1, s2)
    fwrite(newfile, txtNew)
    #print(fread(newfile))


def main():
    freplace('ucs2.txt', 'ucs2', 'ucs2-ucs2')
    freplace('utf8.txt', 'utf8', 'utf8-utf8')


if __name__ == '__main__':
    main()
