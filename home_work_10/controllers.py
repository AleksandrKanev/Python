from models import (get_steps_lst, get_steps_count, process_step)
from loggers import logger


def process_func(values, user):
    
    lst_steps = get_steps_lst(values)

    count_steps = get_steps_count(lst_steps)
    res_lst = lst_steps[:]

    for _ in range(count_steps):
        res_lst = process_step(res_lst)

    logger(res_lst[0], values, user,)
    return res_lst[0]

