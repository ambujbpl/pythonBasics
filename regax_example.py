import re;
text = "qqqqqq ambujdubey89@gmail.com 8 A my name is ambuj dubey ambujdbey89@gmail.com";
regax_pattern = re.compile("ambuj");
result = regax_pattern.search(text);
print(result)
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
regax_pattern1 = re.compile("[ad]");
result1 = regax_pattern1.search(text);
print(result1)
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
regax_pattern2 = re.compile("[a-jA-D0-9]+");
result3 = regax_pattern2.search(text);
print(result3)
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
regax_pattern3 = re.compile("[a-zA-z0-9]+@[a-zA-z0-9]+\.[a-zA-z0-9]+");
result4 = regax_pattern2.findall(text);
print(result4)