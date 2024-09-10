def function_3(value_1, value_2):
    if value_1 == 0:
        value_1 = value_1 + 1
        print(value_1)
    if value_1 == 1:
        print(value_2)
    else:
        print("booyah")
        return value_1
    return value_2

result = function_3(7, 565)

print(result)