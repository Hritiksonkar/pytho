nterms=int(input("Enter number of terms: "))
result = list(map(lambda x: 2 ** x, range(nterms)))
print("The first", nterms, "terms of the power of 2 are:", result)