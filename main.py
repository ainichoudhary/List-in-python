##### emoji converting
message = input(">")
word = message.split(' ')
emoji = {
    ":)": "😆",
    ":(": "😔"
}
output = " "
for i in word:
    output += emoji.get(i, "!") + " "
print(output)

# print number in alphabates
phone = input("Enter your phone number: ")
digit_mapping = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four"
}
output = " "
for i in phone:
    output += digit_mapping.get(i, " ! ") + " "
print(output)

# Dictionaries#######################
# in this we use curly bracket in bracket write key value pair
customer = {
    "name": "Qurat ul ain",
    "age": 26,
    "is_verify": True
}
# print(customer["age"])
# for print non default value in dictionary
print(customer.get("birth day", "12 june 1997"))

################## unpacking ########################
# if we use small bracket that are pack if use square bracket that are unpacking
coordinate = [1, 2, 3]
x, y, z = coordinate
print(y)

################# tuple #######################################
# tuple are immuteable and in this we use small bracket
number = (1, 2, 3)
# its not working is i use square bracket then work but tuple is convet into aray
# number[0] = 10
print(number[1])

# ########remove duplicate from array list
number = [2, 4, 5, 3, 2, 7, 6, 7, 2, 3, 4, 3, 0, 1, 0, 1, 9, 8]
uniques = []
(number.sort())
for i in number:
    if i not in uniques:
        uniques.append(i)
print(uniques)

number = [1, 4, 2, 7, 9, 5, 3]
# insert number in array
# number.append(13)
# insert number at index
number.insert(2, 10)
print(number)

matrix = [
    [1, 2, 3],
    [3, 6, 7],
    [2, 5, 3]
]
# matrix[2][2] = 5
# print (matrix[1][2])
for row in matrix:
    for i in row:
        print(i)

number = [15, 4, 5, 7, 1, 3]
max = number[0]
for i in number:
    if i > max:
        max = number
print(max)

# basic of list
names = ['ali', 'ahmad', 'quratulain', 'aisha']
names[2] = 'qurat'
# print(names[1:3])
print(names)
