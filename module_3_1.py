calls = 0
def count_cal():
    global calls
    calls += 1


def string_info(string):
    string_ = []
    string_.append(len(string))
    string_.append(string.upper())
    string_.append(string.lower())
    tuple(string_)
    count_cal()
    print(string_)


def is_contains(string, list_to_search):
    a = list_to_search
    b = [x.upper() for x in a]
    if (string.upper()) in (b):
        print(True)
    else:
        print(False)
    count_cal()


string_info('Capybara')
string_info('Armageddon')
is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])
is_contains('cycle', ['recycling', 'cyclic'])
print(calls)

