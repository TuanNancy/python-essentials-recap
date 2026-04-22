evens = []

for i in range(10):
    if i % 2 == 0:
        evens.append(i)

print(evens)

# List Comprehension
evens = [i for i in range(10) if i % 2 == 0]

evens_advanced = [i**2 if i%2==0 else i**3 for i in range(10)]

print(evens_advanced)