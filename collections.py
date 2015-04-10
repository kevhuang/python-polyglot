lst = []

lst.append(2)
lst.extend([345,45])
lst.insert(1,4)
lst.append([2]*6)
lst.append('cookies')
print(lst)

lst.remove([2]*6)
lst.sort()
print(lst)
lst.reverse()
print(lst)

del  lst[3:]
print(lst)

repeatedChars = ['1','1','1','2','2','2','2','2','2','2','1','1','1','2','2','2','2','2','2','2',]

oneTwo = set(repeatedChars)
oneThree = set('13')
print(oneTwo)
print(oneThree)

print(oneTwo & oneThree)
print(oneTwo | oneThree)
print(oneTwo ^ oneThree)
print(oneTwo - oneThree)
print(oneThree - oneTwo)

dictionary = {'key': 'value'}

print(dictionary['key'])
print(dictionary.keys())
