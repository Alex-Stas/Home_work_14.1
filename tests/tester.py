def printing(function):
    def inner(*args, **kwargs):
        result = function(*args, **kwargs)
        print('result =', result)
        return result
    return inner

def add_one(x):
    return x + 1



if __name__ == "__main__":
    add_one = printing(add_one)

    y = add_one(10)
    # => result = 11
    print(y)
    # 11