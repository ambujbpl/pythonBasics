list1 = [1,2,3,4,5,6]
list2 = ["amb","harshi","ami","sid","ma","pa"]
zipped = list(zip(list1,list2))
print(zipped)
unzipped = list(zip(*zipped))
print(unzipped)
print(unzipped[0])
print(unzipped[1])

for (l1,l2) in zip(list1,list2):
    print(l1)
    print(l2)
    print('\n')


products = ['Apple','Mango','Banana']
quantity = [1,5,12]
price = [50,12,30]
sentances = []
for (p,q,pri) in zip(products,quantity,price):
    # p, r, pri = str(p), str(q), str(pri)   // group typcasting
    sentance = 'I bought ' + str(q) + ' ' + p + ' in ' + str(pri) + ' rupees only.';
    sentances.append(sentance)
    # print(p)
    # print(q)
    # print(pri)
    # print('\n')

print(sentances)