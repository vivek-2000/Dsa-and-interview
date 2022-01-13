def fun(passlist):
    listt=[]
    for i in range(len(passlist)):
        pass_ = passlist[i]
        new_pass = [c for c in pass_] # convert the string in a list of chars
        for j in range(len(pass_)//2):
            new_pass[j], new_pass[j+2] = new_pass[j+2], new_pass[j] # swap

        listt.append(''.join(new_pass))
    return listt
a=fun(["abcd", "bcad"])
print(a)