
# load the dataset
data = open('data/corpus').read()
labels, texts = [], []
eachLine = []
ctr = 0
dist = {}
for i, line in enumerate(data.split("\n")):
    content = line.split()
    if content[0] in dist:
    	dist[content[0]] = dist[content[0]] + 1
    else:
    	dist[content[0]] = 1

print(str(dist))

