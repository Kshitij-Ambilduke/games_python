name1=str(input("Enter your name: "))
name2=str(input("Enter your crush name: "))
nametotal=name1+"loves"+name2
nametotal=list(nametotal)

n=range(len(nametotal))
nums=[]
for i in n:
	if len(nametotal)==0:
		break
	m=nametotal[0]
	x=nametotal.count(m)
	nums.append(x)
	for j in range(x):
		nametotal.remove(m)

i=0
sent=[]


def calc(nums):
	
	sent=[]
	
	if len(nums)%2==0 and len(sent)!=2:#1
		for i in range(len(nums)//2):
			x=nums[i]+nums[-1-i]
			sent.append(x)
		

	elif len(nums)%2!=0 and len(sent)!=2:#2
		for i in range(len(nums)//2):
			x=nums[i]+nums[-1-i]
			sent.append(x)
		sent.append(nums[len(nums)//2])

	sent1=[]	
	sent2=[]

	for i in range(len(sent)):
		if sent[i]>9:
			ex1=sent[i]//10
			ex2=sent[i]%10
			
			sent1=sent[0:i]
			sent2=sent[i+1:]
			sent=sent1+[ex1]+[ex2]+sent2
			
			

	if len(sent)==2:
		print("the love between",name1,"&",name2,"is",sent[0],sent[1],"%")
		return sent

	
	nums=sent
	calc(sent)
	
	


it=calc(nums)

