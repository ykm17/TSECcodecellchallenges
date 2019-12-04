arr = ["tseccodecell@gmail.com",
       "tseccode.cell@gmail.com",
       "tsec+codecell@gmail.com",
       "tse.ccodecell@gmail.com",
       "tsec.codecell@gmail.com",
       "tseccodecell+tsec@gmail.com",
       "tsec.codecell@gmail.com",
       "tseccode+cell@gmail.com",
       "tsec+codecell@gmail.com",
       "tsec+codecell@gmail.com",
       "code@tsec.com",
       "tsec@gmail.com",
       "tsec@tsec.codecell.com",
       "cod.e@tsec.com",
       "code@tsec.com",
       "tsec@tseccodecell.com",
       "code+cell@tsec.com",
       "codecell@tsec.com",
       "code+cell@tsec.com",
       "tsec@gmail.com",
       "tsec@tseccodecell.com",
       "code@tsec+code.com",
       "tsec@tseccodecell.com"]

i = 0
for x in arr:
    arr[i] = x.split("@")[0]
    arr[i] = arr[i].split("+")[0]
    temp = ""
    for j in arr[i].split("."):
        temp += j
    arr[i] = temp
    i += 1
ans = []
for i in arr:
    if i not in ans:
        ans.append(i)

print(len(ans))
