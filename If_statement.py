is_male = True
is_tall = False

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not is_tall:
    print("You are a male but not tall")
elif not is_male and is_tall:
    print("You are not a male but you are tall")
else:
    print("You are either male nor tall")

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num3
    else:
        return num3


print(max_num(4,4,4))