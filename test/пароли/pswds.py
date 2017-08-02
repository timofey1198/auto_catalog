f = open('all.txt', 'r')
for i in range(100):
    print(f.readline(), end='')
f.close()