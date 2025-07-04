def debug_init():
    global already_printed
    global old_list
    global run_amount
    global repeats
    run_amount = 0
    already_printed = []
    old_list = []
    repeats = 0


def debug_update():
    global repeats
    repeats += 1


def debug_print(var, how_many_repeats):
    global old_list
    global already_printed
    global repeats
    if isinstance(var, str) or isinstance(var, int) or isinstance(var, float):
        not_true = True
        for i in already_printed:
            if i == var:
                not_true = False
        if not_true is True:
            print(var)
            already_printed.append(var)
        if repeats < how_many_repeats:
            print(var)
            already_printed.append(var)
            how_many_repeats += 1
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
    first = 1
    float_ = 1.1
    int_ = 1
    str_ = 'hi'
    list_ = [1, 2, 1]
    while True:
        debug_print(float_, 1)
        debug_print(int_, 0)
        debug_print(str_, 0)
        debug_print(list_, 0)
        if first == 1:
            first += 1
            float_ = 1.2
            int_ = 3
            str_ = 'hello'
            list_ = [1, 2, 1, 2]
        debug_update()


debug_init()
debug_test()
