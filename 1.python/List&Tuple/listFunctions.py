values = [5, 4, 6, 1, 7, 3, 8, 9]

print(values[0]) # 5 
print(values[1]) #4

#slicing the list same as string
print(values[2:4]) #[6,1]
print(values[0:5]) #[5,4,5,1,7]

#list Functions
print(values.append(2)) #[5,4,6,1,7,3,8,9,2]
print(values)
print(values.pop(3)) #[5,4,6,7,3,8,9,2] remove element of index position 3
print(values)
print(values.insert(4, 1)) #[5,4,6,7,1,3,8,9,2] inserted 1 at index position 4 
print(values)
print(values.sort()) #[1,2,3,4,5,6,7,8,9]
print(values)
print(values.reverse()) #[9,8,7,6,5,4,3,2,1]
print(values)
print(values.remove(9)) #[8,7,6,5,4,3,2,1]
print(values)


