def list_sum(some_list):
    if not some_list:
        return 0
    elif len(some_list) == 1:
        return some_list[0]
    else:
        return some_list[0] + list_sum(some_list[1:])
