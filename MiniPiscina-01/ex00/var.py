def my_var():
    number = 42
    string = "42"
    string2 = "quarante-deux"
    num_float = 42.0
    true = True;
    var_list = [42]
    var_dict = {42: 42,}
    var_tuple = (42,)
    var_set = set()
    
    print(f"{number} has a type {type(number)}")
    print(f"{string} has a type {type(string)}")
    print(f"{string2} has a type {type(string2)}")
    print(f"{num_float} has a type {type(num_float)}")
    print(f"{true} has a type {type(true)}")
    print(f"{var_list} has a type {type(var_list)}")
    print(f"{var_dict} has a type {type(var_dict)}")
    print(f"{var_tuple} has a type {type(var_tuple)}")
    print(f"{var_set} has a type {type(var_set)}")

if  __name__ == '__main__':
    my_var()
