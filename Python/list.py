def run():
    my_list = [1,'hello',True,4.3]
    my_dic = {"firstname": "Carlos Andres", "lastname": "Reyes Peña"}


    super_list = [
        {"firstname": "Carlos Andres", "lastname": "Reyes Peña"},
        {"firstname": "Carlos1 Andres", "lastname": "Reyes Peña"},
        {"firstname": "Carlos2 Andres", "lastname": "Reyes Peña"},
        {"firstname": "Carlos3 Andres", "lastname": "Reyes Peña"}

    ]

    super_dic = {
        "natural_nums": [1,2,3,4,5,6],
        "integer_nums": [-1,-2,0,1,2,3],
        "floating_nums": [1.1,2.3,3.3,4.2,5.5,6.4]
    }

    for key, value in super_dic.items():
        print(key," ",value)



if __name__=="__main__":
    run()