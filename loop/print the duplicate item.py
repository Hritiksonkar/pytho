item=["apple","banana","grapes","apple","orange","banana"]
duplicate_items=set()
for i in item:
    if i in duplicate_items:
        print("duplicate item is:",i)
        continue
    duplicate_items.add(i)

item=["apple","banana","grapes","apple","orange","banana"]
duplicate_items=set()
for i in item:
    if i in duplicate_items:
        print("duplicate item is:",i)
        break
    duplicate_items.add(i)
        