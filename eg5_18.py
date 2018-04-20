import eg5_1_file
def lealmen():
    f = eg5_1_file.FileInfo(r'\MP3\1.mp3')
for i in range(100):
    lealmen()

class counter:
    count = 0
    def __init__(self):
        self.__class__.count+=1

print("counter:",counter.count)
c = counter()
print("c.count:",c.count)
print("counter:",counter.count)
d = c
print("d.count:",d.count)
print("counter",counter.count)
e = counter()
print("e.counter",e.count)
print("counter",counter.count)
print("c.counter",c.count)

m = eg5_1_file.MP3FileInfo()
# m.__parse(r'\MP3\1.mp3')
# eg5_1_file._MP3FileInfo__parse(r'\MP3\1.mp3')