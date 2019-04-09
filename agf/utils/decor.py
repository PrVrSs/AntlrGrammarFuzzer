"""Decorators"""
import functools
import errno
import os
import signal

from agf.my_error import TimeoutError


def memoization(func):
    rule_dictionary = {}

    @functools.wraps(func)
    def wrapper(self, new_rule):
        if new_rule not in rule_dictionary:
            rule_dictionary[new_rule] = func(self, new_rule)
        return rule_dictionary[new_rule]
    return wrapper


def logging(trace_enable):
    """
    Декоратор, логирующий работу кода.
    Номер/количество вызова/вов, Время работы, полученные данные и данные, которые возвращает
    """
    def decorator(func):
        import time

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            wrapper.count += 1
            t = time.clock()
            res = func(*args, **kwargs)
            with open("log.txt", 'a') as logging_file:
                logging_file.write("********************************\n")
                logging_file.write(func.__name__ + "\n")
                logging_file.write("Время работы: {}\n".format(time.clock() - t))
                logging_file.write("Была вызвана: {}\n".format(wrapper.count))
                logging_file.write("Параметр вызова: {}\n".format(*args))
                logging_file.write("Возвращаемое значение: {}\n".format(res))
            return res
        wrapper.count = 0
        with open("log.txt", 'w') as _:
            pass
        return wrapper if trace_enable else func
    return decorator


def timeout(seconds=20, error_message=os.strerror(errno.ETIME)):
    def decorator(func):
        def _handle_timeout(signum, frame):
            raise TimeoutError(error_message)

        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.setitimer(signal.ITIMER_REAL, seconds)
            try:
                result = func(*args, **kwargs)
            except TimeoutError:
                return False
            finally:
                signal.setitimer(signal.ITIMER_REAL, 0)
            return result
        return wrapper
    return decorator
