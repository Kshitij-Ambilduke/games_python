import itertools 

hangman=iter(["h","a","g","g","m","a","n"])	
vowels=["a","e","i","o","u"]
word_chosen = "nacreous"
word=list(word_chosen)
temp=[]

for letter in word:
	x=vowels.count(letter)
	if x==0:
		temp.append("*")
		print("*",end="")
	else:
		temp.append(letter)
		print(letter,end="")

temp3=[]

def inputx():
	print()
	choice=True
	while choice==True:
		guess=str(input("Enter a letter"))
		if len(guess)!=1:
			print("please enter a single letter: ")
		else:
			choice=False
			return(guess)




def check(temp,word,guess):
	mkb=0
	
	temp=[]
	for letter in word:
		
		if letter == guess:
			vowels.append(letter)
			mkb=1
	
	if mkb==0:
		j=next(hangman)
		print("*!*!*!*!*you have consumed!*!*!*!*!* ",j)
		if j=="n":
			print("#### YOU ARE A HANG MAN, LOOOOSERRRRR ###")
			return False

	for letter in word:
		
		x=vowels.count(letter)
		if x==0:
			temp.append("*")
			print("*",end="")
		else:
			temp.append(letter)
			print(letter,end="")

	n=temp.count("*")
	if n==0:
		print("   *********YOU HAVE COMPLETED THE QUEST************")
		return False
	else:
		return True



play=True
while play==True:
	guess=inputx()
	play=check(temp,word,guess)