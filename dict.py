import random

print("Dictionaries in py:")
dic = {
    "fruit":"f1",
    "comp": "smartphone"
}
print(dic)

print("\n Printing with index: ")
print(dic["comp"])

fruit = {"apple": 10,
         "orange": 20,
         "pears": 35
         }
fruit["mango"] = 50
print(fruit)

fruit.pop("orange")

for key in fruit.keys():
    print("fruit keys: ", key)
    
print("values of dict fruit: ", list(fruit.values()))
print("items: ",list(fruit.items()))
    