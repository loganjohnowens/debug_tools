already_printed = []
old_list = []


def debug_print(var):
    global old_list
    global already_printed
    if isinstance(var, str) or isinstance(var, int) or isinstance(var, float):
        not_true = True
        for i in already_printed:
            if i == var:
                not_true = False
        if not_true is True:
            print(var)
            already_printed.append(var)
    if isinstance(var, list):
        new_list = []
        if old_list != var:
            dif = len(var) - len(old_list)
            dif = dif - dif * 2
            while dif < 0:
                new_list.append(var[dif])
                dif += 1
            print(new_list)
            old_list = var


def debug_test():
    first = True
    float_ = 1.1
    int_ = 1
    str_ = 'hi'
    list_ = [1, 2, 1]
    while True:
        debug_print(float_)
        debug_print(int_)
        debug_print(str_)
        debug_print(list_)
        if first is True:
            first = False
            float_ = 1.2
            int_ = 3
            str_ = 'hello'
            list_ = [1, 2, 1, 2]


debug_test()
