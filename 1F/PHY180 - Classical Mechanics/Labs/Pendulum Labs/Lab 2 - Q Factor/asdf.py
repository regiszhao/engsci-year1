rawdata = open('rawdata.txt', 'r')
mydata = open('mydata.txt', 'w')

for line in rawdata.readlines():
    x, y = float(line.split()[0]), float(line.split()[1])
    print(x,y)
    mydata.write(str(x) + ' ' + str(y) + ' 0.0005' +  ' 0.05' + '\n')

rawdata.close()
mydata.close()