calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())

def is_contains(string, list_to_search):
    count_calls()
    print(list_to_search)
    return string in list_to_search

print(string_info(input()))
print(is_contains(input().lower(), input().lower().split())) #значения для второго аргумента для списка вводятся через пробел
print(is_contains(input().lower(), input().lower().split())) #значения для второго аргумента для списка вводятся через пробел
print(string_info(input()))
print(is_contains(input().lower(), input().lower().split())) #значения для второго аргумента для списка вводятся через пробел
print(string_info(input()))
print(calls)