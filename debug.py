already_printed = []


def debug_print(var):
    if isinstance(var, str) or isinstance(var, int) or isinstance(var, float):
        not_true = True
        for i in already_printed:
            if i == var:
                not_true = False
        if not_true is True:
            print(var)
            already_printed.append(var)


def debug_test():
    float_ = 1.1
    int_ = 1
    str_ = 'hi'
    while True:
        debug_print(float_)
        debug_print(int_)
        debug_print(str_)
