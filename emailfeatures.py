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
print("TOTAL:",len(arr))
i = 0
ans = []
for x in arr:
    temp = x.split("@")
    # print(temp)
    arr[i] = temp[0]
    ans.append(temp[1])
    arr[i] = arr[i].split("+")[0]
    temp = ""
    for j in arr[i].split("."):
        temp += j
    arr[i] = temp
    i += 1

for i in range(len(arr)):
    arr[i] = arr[i] + "@" + ans[i]

x = []
for i in arr:
    if i not in x:
        x.append(i)

print(len(x))
