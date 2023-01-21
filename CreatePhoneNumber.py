tln = list(range(10))
print(tln)
print(type(tln))

def create_phone_number(n):
    temp_list = list()
    for liter in n:
        temp_list.append(f"{liter}")

    temp_list.insert(0, "(")
    temp_list.insert(4, ")")
    temp_list.insert(5, " ")
    temp_list.insert(9, "-")

    print(temp_list)
    print(type(temp_list))
    print(len(temp_list))

    temp_list1 = "".join(temp_list)
    print(temp_list1)
    print(type(temp_list1))
    return  temp_list1


create_phone_number(tln)
