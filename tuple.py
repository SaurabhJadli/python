tu = (1,2,3,4,5)
print(type(tu))
print(tu)

print("\ntuble without parenteses:")
tu2 = "item1", 1, 5
print("tuble list 2 => ",tu2)

tu3 = 1,2,3
print("tu3 id = ",id(tu3))
tu3 = 1,2
print(tu3)
print("tu3 = ",id(tu3))

print("\ntuples are immutable: ")
tu4 = (1,2,3,4)
tu5 = (1,2,3,4)
print(tu4 == tu5)
print(tu4 is tu5)
print("tu4 id = ", id(tu4))
print("tu5 id = ", id(tu5))
print("means, if value is same then python will assign same id to both.")