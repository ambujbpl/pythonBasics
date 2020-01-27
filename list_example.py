arr = ["ambu",12,["new1","new2"],"test"];
print(arr);
arr.append("newTest");
arr.insert(0,"oldTest");
print(len(arr));
for item in arr:
    print(item);


# print(arr[:2])
print(arr[:-1])


print("-----------------------------------------------------")
arr1 = [0,1,2,3,4,5,6,7,8,9,10]
for i in range(len(arr1)):
    print(arr1[0:i]);



print("-----------------------------------------------------")
show_length_size = 7;
arr1 = [0,1,2,3,4,5,6,7,8,9,10]
for i in range(len(arr1)-(show_length_size-1)):
    print(arr1[i:i+show_length_size]);



print("-----------------------------------------------------")
arr2 = "test1,test2,test3,test4,test5";
splited = arr2.split(',');
print(splited);
newStr = ' Start : '.join(splited);
print(newStr);
