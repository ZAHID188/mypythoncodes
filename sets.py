#create an empty set
s = set()

#Add elements to set
s.add(1)
s.add(2)
s.add(3)
s.add(4)
print(s)

s.remove(3)
s.add(7)
print(s)
print(f"The set has {len(s)} elements")
