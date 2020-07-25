readbook = open('book.txt', "r+", encoding="utf8")
clean = open('dettol.txt', 'r+', encoding='utf8')
word_count = {}
words = []
kill = str.maketrans('', '', r"a-zA-Z0-9")
flag = 0
for item in readbook:
    if item[0:3] == "***":
        flag += 1
    elif flag == 1:
        clean.write(item)

for line in clean:
    line = line.lower()
    words = line.split()
    for count in words:
        for char in count:
            if not char.isdigit() and not char.isalpha():
                if char != " " or char != "\n":
                    count = count.replace(char, "")
        # count = count.translate(kill)
        if count not in word_count:
            word_count[count] = 1
        else:
            word_count[count] = word_count[count] + 1


final = sorted(word_count.keys())
result = open('result.txt', 'r+')

for k in final:
    print(k, word_count[k])
    result.write(k + ":" + str(word_count[k]) + "\n")
