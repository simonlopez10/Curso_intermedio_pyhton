def run():
    my_list = [1, "hello", True, 4.5]
    my_dict = {"firstname": "Simón", "lastname": "López"}
   
    super_list = [
        {"firstname": "Simón", "lastname": "López"},
        {"firstname": "Miguel", "lastname": "Torres"},
        {"firstname": "Pepe", "lastname": "Rodelo"},
        {"firstname": "Susana", "lastname": "Martinez"},
        {"firstname": "José", "lastname": "García"},
    ]

    super_dict = {
        "natural_nums": [1,2,3,4,5],
        "integer_nums": [-1,-2,0,1,2],
        "floating_nums": [1.1,4.5,6.43],
    }

    for key, value in super_dict.items():
        print(key, "-", value)
    
    for item in super_list:
        print(item)


if __name__== '__main__':
    run()