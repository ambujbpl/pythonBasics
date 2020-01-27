from collections import OrderedDict
obj = {"name":"ambuj","surname":"dubey","org":"AVR"};
print(obj["name"]);
print(obj.get("mobile"));
print(obj.get("test"));

print( sorted(list(obj.values())))

obj1 = {"ambuj_age":30,"skd_age":56,"kal_age":51,"ami_age":31,"har_age":25,"sid_age":8}
arr =[];
for key in obj1:
    if obj1[key] >= 30:
        arr.append(key)

print(arr)


print([arr2 for arr2 in obj1 if obj1[arr2] >= 30] );
