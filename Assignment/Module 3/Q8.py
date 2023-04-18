# WAP to remove duplicates from a list

v=input("Enter list : ") #[10,20,30,20,10,50,60,40,80,50,40]

dup_items = set()
uniq_items = []
for x in v:
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.add(x)

print(dup_items)
