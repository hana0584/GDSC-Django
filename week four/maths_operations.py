def basic_operations(a, b):
    try:
        add = a + b
        sub = a - b
        mul = a * b
        div = a / b
        return {'addition': add, 'subtraction': sub, 'multiplication': mul, 'division': div}
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except TypeError:
        print("Error: Invalid input")
        return None

def power_operation(base, exponent, **kwargs):
    try:
        if 'modulo' in kwargs:
            mod = kwargs['modulo']
            return pow(base, exponent, mod)
        else:
            return pow(base, exponent)
    except TypeError:
        print("Error: Invalid input")
        return None

def apply_operations(operation_list):
    results = []
    for operation in operation_list:
        function = operation[0]
        arguments = operation[1]
        try:
            result = function(*arguments)
            results.append(result)
        except:
            results.append(None)
    return results
