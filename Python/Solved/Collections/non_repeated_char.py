from collections import OrderedDict
dict_values = OrderedDict()
string = "abcdcd"

for char in string:
   if char in dict_values:
       dict_values[char] += 1
   else:
       dict_values[char] = 1

for key, value in dict_values.items():
    if value == 1:
       print ("First non repeated character is %s" % key)
       break
    else:
       pass
