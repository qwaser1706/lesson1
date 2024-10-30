from module_4_2_1 import *

def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()
    return inner_function
inner = test_function()

inner

inner_function()

test_function()