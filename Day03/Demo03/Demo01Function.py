def com_number(a,b):
    """
    比较两个数字大小
    :param a:
    :param b:
    :return:
    """
    if a>b:
        print("{0}是较大值".format(a))
    else:
        print("{0}是较大值".format(b))

com_number(4,5)
com_number(8,5)
help(com_number.__doc__)