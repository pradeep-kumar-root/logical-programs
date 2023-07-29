def divide(first, second):
    print ("The result is:", first/second)

def swipe_decorator(func):
    def swipe(first, second):
        if first < second:
            first, second = second, first
        return func(first, second)

    return swipe


divide = swipe_decorator(divide)
divide(4, 16)
