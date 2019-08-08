import re
filepath = "C:/Users/Nisha Devasia/Documents/ff7.txt"
outpath = "C:/Users/Nisha Devasia/Downloads/writeoutff7.txt"

names = ["Cloud", "Tifa", "Aeris", "Barret", "Yuffie", "Vincent", "Zack", "Red",
         "Cid", "Cait", "Cid", "Reno", "Rude", "Elena", "Tseng", "Cissnei", "Veld", "Legend",
         "Sephiroth", "Jenova", "Rufus", "President", "Kadaj", "Loz", "Yazoo", "Hojo", "Weiss", "Nero",
         "Azul", "Rosso", "Shelke", "Genesis", "Hollander", "Angeal", "Biggs", "Wedge", "Jessie", "Reeve", "Shalua",
         "Lucrecia", "Marlene", "Denzel", "Kunsel", "Lazard", "Moogle Girl", "Bugenhagen", "Nanaki", "Scarlet", "Heidegger",
         "Palmer", "Shera"]

f = open(filepath, 'r')
#result = re.sub("[\(\[].*?[\)\]]", "", f.read())
split = re.findall(r"[\w']+", f.read())

name_dict = {}
name_to_index = {}
name_adjacency_dict = {}

for x in range(0, len(split)):
    word = split[x]
    if word in names:
        try:
            name_to_index[word].append(x)
        except:
            name_to_index[word] = [x]

print(name_to_index)

keylist = []

for key in name_to_index.keys():
    keylist.append(key)

for x in range(0, len(keylist)):
    this_list = name_to_index[keylist[x]]
    for y in range(x+1, len(keylist)):
        that_list = name_to_index[keylist[y]]
        for a in this_list:
            for b in that_list:
                if(abs(a-b) < 15):
                    try:
                        name_dict[keylist[x]].append(keylist[y])
                    except:
                        name_dict[keylist[x]] = [keylist[y]]

for key in name_dict.keys():
    temp_dict = {}
    for name in name_dict[key]:
        try:
            temp_dict[name] += 1
        except:
            temp_dict[name] = 1
    name_adjacency_dict[key] = temp_dict

tuplelist = []

for key in name_adjacency_dict.keys():
    for keytwo in name_adjacency_dict[key]:
        tuplelist.append((key, keytwo, name_adjacency_dict[key][keytwo]))

print(tuplelist)
file = open(outpath, 'w')

header = "Source,Target,Weight,Type"
file.write(header)
file.write("\n")

for thing in tuplelist:
   thisthing = str(thing[0])+","+str(thing[1])+","+str(thing[2])+","+"Undirected"
   file.write(thisthing)
   file.write("\n")

file.close()