# Assignment 1
def main(a, b):
    shorter = min(len(a), len(b))
    count = 0
    for i in range(shorter-1):
        a_sub = a[i:i+2]
        b_sub = b[i:i+2]
        if a_sub == b_sub:
            count = count+1
    return print(count)
main('abcder', 'abcd')

# expect
('abcder', 'abcd')-2



# Assignment2
def main2(num):
    sum = 0
    in_range = False
    for i in range(len(num)):
        if num[i] == 7:
            in_range = True
        if num[i] == 8:
            in_range = False
        if in_range == False:
            sum = sum + num[i]
    return print(sum)
main2([1,2,2,5,7,55,42,67,8,25])

# expect
[1,2,2,5,7,55,42,67,8,25]-43


# Assignment3

fr = ['7@camp1.com|4|55|GDPSV',
      '7@camp1.com|8|22|GDPSV',
      '13@camp1.com|9|13|GDPSV',
      ]
d = {'7@camp1.com': '555',
     '8@camp1.com': '222',
     '13@camp1.com': '1333'
     }

line_list = []
for line in fr:
    columns = line.split('|')
    lookup_val = columns[0]
    if(d.get(lookup_val) is None):
        next_number = int(max(d.values())) + 1
        d[lookup_val] = str(next_number)
        columns[0] = str(next_number)
        line_list.append("|".join(columns))
    else:
        columns[0] = d.get(lookup_val)
        line_list.append("|".join(columns))

fr = line_list
print("Value of fr:")
print(fr)
print("Value of d:")
print(d)


# # Assignment 6
# class Animal:
#     def __init__(self):
#         print("Animal Constructed")
#     def eat(self):
#         print("Animal Eating")
# class Bird(Animal):
#     def __init__(self, name):
#         self.Bird_name = name
#     def move(self):
#         print("Bird Flying")
#
# mybird = Bird("wolfy")
# print(mybird.Bird_name)
