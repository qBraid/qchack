def control_input(options, input_ctl):
    if input_ctl is not None:
        if isinstance(input_ctl, int):
            if 0 < input_ctl <= 3:
                return True
            elif options+1 < 3:
                print("Please give a number between 0 and {}.".format(options))
            else:
                print("Please give a number between 0 and {}.".format(3))
        else:
            if input_ctl in options:
                return True
            else:
                print("Please give a valid gate between {}".format(options))
    return False