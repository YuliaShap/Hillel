def cache_decorator(func, *args):  
    cache = {}

    def decorated_function(*args):
        print('-' * 50)
        print('args =', args)
        print('cache =', cache)
        if cache.get(args):
            print('Operation: get the result from the cache')
            return cache[args]
        else:
            print('Operation: calculating and caching the result')
            cache[args] = func(*args)
            return cache[args]

    return decorated_function


@cache_decorator
def custom_sum(*args):
    return sum(args)


print('result =', custom_sum(1, 2))
print('result =', custom_sum(1, 2))
print('result =', custom_sum(1, 2, 3))
print('result =', custom_sum(1, 2, 3))
