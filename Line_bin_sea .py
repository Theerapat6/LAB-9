
def line(ninja,sea,):

   for x in range(len(ninja)):
        if ninja[x] == sea:
            return x

ninja = [7,10,12,14,16,20,29,37]

print("index 14 is",line(ninja,14))
print("index 29 is",line(ninja,29))