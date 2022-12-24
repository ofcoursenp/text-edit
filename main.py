# text = input("> ")
# whattodo = input("> ").lower()
# newtext = ""
# if whattodo[0] == "r":
#     if whattodo[2] == 'p':
#         splittext = [*text]
#         for i in splittext:
#             if i == "!" or i == ":":
#                 continue
#             else:
#                 newtext = newtext + i

# if whattodo[0] == "r":
#     if whattodo[2] == "s":
#         splittext = [*text]
#         for i in splittext:
#             if i == " " or i == "  ":
#                 continue
#             else:
#                 newtext = newtext + i        
 
# print(newtext)

import string
thelist = list(string.ascii_uppercase)
print(thelist)

text = input()
punc = "off"
space = "off"
capital = "on"
newtext = text
if punc == "on":
    splittext = [*newtext]
    newtext = ''
    for i in splittext:
        if i == "!" or i == ":":
            continue
        else:
            newtext = newtext + i
if space == "on":
    splittext = [*newtext]
    newtext = '' 
    for i in splittext:
        if i == " " or i == "  ":
            continue
        else:
            newtext = newtext + i     
 
if capital == "on":
    splittext = [*newtext]
    newtext = '' 
    for i in splittext:
        if i in thelist:
            continue     
        else:
            newtext = newtext + i     
print(newtext)


