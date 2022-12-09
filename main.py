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


text = "abc! acde"
punc = "off"
space = "off"
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

print(newtext)


