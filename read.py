data =[]
count =0
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count %10000 ==0 :
		  print(len(data))
print('讀取完畢,總共有',len(data),'筆資料')

sum_len =0
for d in data:
	sum_len =sum_len +len(d)
	
print('每筆平均是',sum_len /len(data))


new=[]
for d in data:
	if len(d) <100:
		new.append(d)

print('一共有',len(new),'筆資料小於100')
print(new[0])
