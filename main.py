print(" bye ")
print("I want to go home")
print("why is not working")
print("I want to go home")

import tlqkf

Alice = tlqkf.Person("Alice", 30)
Alice.add_point(5)
print(Alice)

Alex = tlqkf.Person("Alex", 25, 10)
print(Alex)

print(f"Alice's points: {Alice.point}")
print(f"Alex's points: {Alex.point}")

TaxCalculator = tlqkf.TaxCalc()
label = tlqkf.Pricelabel(TaxCalculator)

print(label.text(10000))