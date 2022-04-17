from time import sleep
list = ['один', 'двa', 'три', 'четыре', 'пять']
input = open('data.txt')
output = open('dataRu.txt', 'w')
k = 0
index = 0
s = ''
for i in input:
	for j in i:
		if j != ' ':
			k+=1
		else:
			break
	output.write(list[index] + i[k:])
	k=0
	index+=1
input.close()
output.close()