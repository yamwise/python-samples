# write a function that takes a string and reverses it in place

def reverse(string):
    if string == "":
        return
    mid = len(string) // 2
    for i in range(mid):
        string[i], string[-(i+1)] = string[-(i+1)], string[i]
    return


string1 = ['h', 'a', 'l', 'o', '2']
string2 = ['j', 'e', 'd', 'i']

print(string1)
reverse(string1)
print(string1)

print(string2)
reverse(string2)
print(string2)
