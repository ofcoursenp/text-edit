text = input("> ")
whattodo = input("> ").lower()
newtext = ""
if whattodo[0] == "r":
    if whattodo[2] == 'p':
        splittext = [*text]
        for i in splittext:
            if i == "!" or i == ":":
                continue
            else:
                newtext = newtext + i

print(newtext)


