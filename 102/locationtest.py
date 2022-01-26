from location import Location
l1 = Location()
l2 = Location(10, 10)
l3 = Location(-100, 100)
l4 = Location(50, -50)
print(l1)
print(l2)
print(l3)
print(l4)
l1.row = 25
l1.col = 25
l2.row = -10
l2.col = -100
print(l1)
print(l2)