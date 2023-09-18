# Read operation
myquery = {"id": #whatever input}
results = my_collection.find(myquery)
for result in results:
    print(result)
print()

myquery = {"title": #whatever input}
results = my_collection.find(myquery)
for result in results:
    print(result)
print()

myquery = {"composer": #whatever input}
results = my_collection.find(myquery)
for result in results:
    print(result)
print()

#CREATE NODE TABLE Song(id STRING, title STRING, composer STRING, PRIMARY KEY (id))
#CREATE NODE TABLE Part(id STRING, part_id STRING, song_id STRING, name STRING, PRIMARY KEY (id))