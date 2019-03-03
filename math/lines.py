#!/usr/bin/env python3
# -*- coding:utf-8 -*-


from copy import copy
intersection_point_count = 31


def mutiply(lista):
    """
    [a, b, c, d]*[a, b, c, d] => ab + ac + ad + bc + bd + cd
    """
    listb = copy(lista)
    sum_of_mutiple = 0
    for i, a in enumerate(lista):
        for j, b in enumerate(listb):
            if i < j:
                sum_of_mutiple += a * b
    return sum_of_mutiple


def add_to_result(result, group):
    """
    result is a list to save group
    group   is a list [1, 2, 3]
    """
    group.sort()
    if mutiply(group) == intersection_point_count:
        if group not in result:
            result.append(group)


def lines_sep2(line_count = 10):
    """ 
    Split the line group into two sets of parallel lines
    """
    result = []
    for a in range(1, line_count):
        b = line_count - a
        add_to_result(result, [a, b])
    return result


def lines_sep3(line_count = 10):
    """ 
    Split the line group into three sets of parallel lines
    """
    result = []
    for a in range(1, line_count):
        for b in range(1, line_count - a):
            c = line_count - a - b
            add_to_result(result, [a, b, c])
    return result


def lines_sep4(line_count = 10):
    """ 
    Split the line group into four sets of parallel lines
    """
    result = []
    for a in range(1, line_count):
        for b in range(1, line_count - a):
            for c in range(1, line_count - a - b):
                d = line_count - a - b - c
                add_to_result(result, [a, b, c, d])
    return result


def lines_sep5(line_count = 10):
    """ 
    Split the line group into five fsets of parallel lines
    """
    result = []
    for a in range(1, line_count):
        for b in range(1, line_count - a):
            for c in range(1, line_count - a - b):
                for d in range(1, line_count - a - b - c):
                    e = line_count - a - b - c - d
                    add_to_result(result, [a, b, c, d, e])
    return result


def lines_sep6(line_count = 10):
    """ 
    Split the line group into six sets of parallel lines
    """
    result = []
    for a in range(1, line_count):
        for b in range(1, line_count - a):
            for c in range(1, line_count - a - b):
                for d in range(1, line_count - a - b - c):
                    for e in range(1, line_count - a - b - c - d):
                        f = line_count - a - b - c - d - e
                        add_to_result(result, [a, b, c, d, e, f])
    return result


def lines_sep7(line_count = 10):
    """ 
    Split the line group into seven sets of parallel lines
    """
    result = []
    for a in range(1, line_count):
        for b in range(1, line_count - a):
            for c in range(1, line_count - a - b):
                for d in range(1, line_count - a - b - c):
                    for e in range(1, line_count - a - b - c - d):
                        for f in range(1, line_count - a - b - c - d - e):
                            g = line_count - a - b - c - d - e - f
                            add_to_result(result, [a, b, c, d, e, f, g])
    return result


def lines_sep8(line_count = 10):
    """ 
    Split the line group into eight sets of parallel lines
    """
    result = []
    for a in range(1, line_count):
        for b in range(1, line_count - a):
            for c in range(1, line_count - a - b):
                for d in range(1, line_count - a - b - c):
                    for e in range(1, line_count - a - b - c - d):
                        for f in range(1, line_count - a - b - c - d - e):
                            for g in range(1, line_count - a - b - c - d - e - f):
                                h = line_count - a - b - c - d - e - f - g
                                add_to_result(result, [a, b, c, d, e, f, g, h])
    return result


def lines_sep9(line_count = 10):
    """ 
    Split the line group into nine sets of parallel lines
    """
    result = []
    for a in range(1, line_count):
        for b in range(1, line_count - a):
            for c in range(1, line_count - a - b):
                for d in range(1, line_count - a - b - c):
                    for e in range(1, line_count - a - b - c - d):
                        for f in range(1, line_count - a - b - c - d - e):
                            for g in range(1, line_count - a - b - c - d - e - f):
                                for h in range(1, line_count - a - b - c - d - e - f - g):
                                    i = line_count - a - b - c - d - e - f - g - h
                                    add_to_result(result, [a, b, c, d, e, f, g, h, i])
    return result


def lines_sep10(line_count = 10):
    """ 
    Split the line group into ten sets of parallel lines
    """
    result = []
    for a in range(1, line_count):
        for b in range(1, line_count - a):
            for c in range(1, line_count - a - b):
                for d in range(1, line_count - a - b - c):
                    for e in range(1, line_count - a - b - c - d):
                        for f in range(1, line_count - a - b - c - d - e):
                            for g in range(1, line_count - a - b - c - d - e - f):
                                for h in range(1, line_count - a - b - c - d - e - f - g):
                                    for i in range(1, line_count - a - b - c - d - e - f - g - h):
                                        j = line_count - a - b - c - d - e - f - g - h - i
                                        add_to_result(result, [a, b, c, d, e, f, g, h, i, j])
    return result


if __name__ == '__main__':

    print("--------------同一平面, 10 根直线, 无任何三线共点 ")
    for i in range(9, 46):
        intersection_point_count = i
        seplist = []
        seplist.append(lines_sep2())
        seplist.append(lines_sep3())
        seplist.append(lines_sep4())
        seplist.append(lines_sep5())
        seplist.append(lines_sep6())
        seplist.append(lines_sep7())
        seplist.append(lines_sep8())
        seplist.append(lines_sep9())
        seplist.append(lines_sep10())

        exist_sep = False
        for single_sep in seplist:
            if single_sep:
                exist_sep = True

        if exist_sep:
            print("----------------------------------------  恰好 %d 个交点:"  % i)
            for j, single_sep in enumerate(seplist):
                if single_sep:
                    print("sep%d:  %r" % (j+2, single_sep))
