dic = {}

with open("poem.txt", 'r', encoding = "utf-8") as file:
    for content in file:
        tokens = content.split(' ') #return a list
        for token in tokens:
            token = token.replace('\n','')
            if token in dic:
                dic[token] += 1
            else:
                dic[token] = 1
print(dic)
