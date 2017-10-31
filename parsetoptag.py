#parseTopTag
import re

read_data = ''
with open('toptags.txt', 'r') as f:
	read_data = f.read()
	print(read_data)
f.closed

print read_data.split('TopItem')[1]

list = read_data.split('TopItem')
data = dict()
for num in range(1,len(list)):
	print(num)
	print(list[num])
	front = list[num].replace('(item=pylast.Tag(u\'','')
	print('front: ', front)
	middle = front.split('\'')[0]
	print('middle: ', middle)
	back = front.split('weight=u\'')[1]
	back = re.findall(r"\d+\.?\d*", back) 
	print('back: ', back)
	data.update({middle:back})
	#exit(0)
print(data)
def parseTopTags(self,toptags):
	list = toptags.split('TopItem')
	for num in range(1,len(list)):
		print(num)
		print(list[num])
		front = list[num].replace('(item=pylast.Tag(u\'','')
		print('front: ', front)
		middle = front.split('\'')[0]
		print('middle: ', middle)
		back = front.split('weight=u\'')[1]
		back = re.findall(r"\d+\.?\d*", back) 
		print('back: ', back)
		exit(0)

