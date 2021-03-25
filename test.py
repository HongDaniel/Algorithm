punctuations = "'!()-[]{};:\,<>./?@#$%^&*_~"


def remove_puntutions(s):
    new = ""
    for i in range(len(s)):
        if(s[i] in punctuations):
            pass
        else:
            new += s[i]
    return new


string1 = "aFDF#^&$%SFSDsd^~#+_gsd2@#%"
print(string1)
print(remove_puntutions(string1))
