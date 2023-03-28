a = 5
b = 7
print(c := 5 == 7)
MY_CONSTANT = "Hello"
print(MY_CONSTANT + str(b - a))
list1 = [a, b, c, MY_CONSTANT]
print(set(list1))
tup1 = (3, 4)
tup2 = (5, 6)
tup3 = tup1 + tup2
print(list(tup3))
dict1 = {"Hi": 6, "HI": "HI", 6: "HI", True: None, False: [1, 2, 3, 4], 3.14: {"HI": "HI", 5: 5}, (3,): (3, 4)}
