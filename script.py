
def set_number_for_conversion(value):
    non_numerical_values = ["a","b","c","d","e","f"]
    if value.isdigit():
        return int(value)
    index = non_numerical_values.index(value)
    return int(index + 10)

def to_the_power(value, power_notation):
    # print("value", str(value))
    # print("power notation", power_notation)
    new_value = value
    if power_notation == 0:
        return 1
    if power_notation == 1:
        return new_value
    for i in range(1,power_notation):
        # print("val of ",i,value)
        new_value = new_value * value
    # print("end value", new_value)
    return new_value

def convert_to_decimal(value, position_type):
    end_of_the_loop = len(value)-1
    decimal_number = 0
    
    for i in range(0,end_of_the_loop+1):
        number = set_number_for_conversion(value[end_of_the_loop-i])
        # print("end of the loop", end_of_the_loop)

        decimal_number = decimal_number + to_the_power(position_type, i) * number
        print("dec",decimal_number)
    return decimal_number



def change_position_systems(initial_position_type, value, ending_position_type):
    if int(initial_position_type) < 2:
        print("initial position type cannot be smaller than 2")
        return 0
    if ending_position_type < 2:
        print("ending position type cannot be smaller than 2")
        return 0
    value_as_array = str(value).split(".")
    decimal_value = convert_to_decimal(value_as_array[0], initial_position_type)
    end_value_to_reverse = []
    if len(value_as_array) == 2:
        dot_value = value_as_array[1]
    while decimal_value >= 1:
        print("d",decimal_value)
        end_value_to_reverse.append(decimal_value % ending_position_type)
        decimal_value = int(decimal_value / ending_position_type)
        print("e",decimal_value)
    print(end_value_to_reverse)
    return decimal_value

print(change_position_systems(16,"a2", 3))