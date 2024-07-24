# Assignment 1

def main(a, b):
    if (a == 20 or b == 20 or a+b == 20):
        return print("True")
    else:
        return print("False")
main(10,10)

def sum(a, b):
    if a>b:
        print("True")
    elif a<b:
        print("False")
    else:
        print("None")
sum(0,0)

def sequence(num_list):
    for i in range(len(num_list)-2):
        if num_list[i] == 1 and num_list[i+1] == 2 and num_list[i+2] == 3:
            return print('sequence is True')
        else:
            return print('sequence is False')

sequence([1,2,3,4,2])

# Assignments 2

def string(str_list):
    str_l= ""
    for i in range(len(str_list)):
        result = str_l+str_list[:i+9]
        return print(result)
string("codcocode")

def string2(str_list2):
    num = len(str_list2)
    if num > 4:
        num = 4
        for i in range(num):
            if str_list2[i] == 6:
                return True

        return False

print(string2([1,2,6,4,5,3]))

def last(str):
    if len(str) <=2:
        return 0
    last2 = str[len(str)-2:]
    count = 0

    for i in range(len(str)-2):
        sub = str[i : i+2]
        if sub == last2:
            count = count + 1
    return count

print(last('hixxhi'))