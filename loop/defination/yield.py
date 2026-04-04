def even_gererator(limit):
    for i in range(2, limit + 1, 2):
        yield i
         

for num in even_gererator(10):
    print(num)