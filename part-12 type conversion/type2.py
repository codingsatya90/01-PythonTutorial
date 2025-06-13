# data = 1
# result1 = data+1
# print(result1)   #output--->2

# =====================

# data = "1"
# result2 = data+1
# print(result2)   #TypeError: can only concatenate str (not "int") to str


# =====================

data = "1"
result3 = data+"1"
print(result3)  # output --->11

# ============Type Conversion
data = "1"
result3 = int(data) + 1  # string data convert to intger data
print(result3)


# boolean (True or False)
# " ",0,None =False else True

data = "False"
result = bool(data)  # convert string to boolean

print(type(data))  # str data type

print(type(result))  # bool data type

print(result)
