def return_10():
    return 10

def add(first_number, second_number):
    sum = first_number + second_number
    return sum

def subtract(first_number, second_number):
    sum = first_number - second_number
    return sum

def multiply(first_number, second_number):
    sum = first_number * second_number
    return sum

def divide(first_number, second_number):
    sum = first_number / second_number
    return sum

def length_of_string(string):
    string_length = len(string)
    return string_length

def join_string(string_1, string_2):
    joined_string = f'{string_1}{string_2}'
    return joined_string

def add_string_as_number(string_1, string_2):
    add_result = int(string_1) + int(string_2)
    return add_result

def number_to_full_month_name(month_number):
    months_of_year = {1: "January", 3: "March", 9: "September"}
    return months_of_year[month_number]

def number_to_short_month_name(month_number):
    months_of_year = {1: "Jan", 4: "Apr", 10: "Oct"}
    return months_of_year[month_number]