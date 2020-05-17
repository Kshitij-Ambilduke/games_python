import itertools

grid = [[0,0,0],
		[0,0,0],
		[0,0,0]]
global fex
fex=0


def win(board):
	#horizontal winner
	
	print("   0  1  2")

	for col, row in enumerate(grid):
		print(col,row)
		if row.count(row[0])==len(grid) and row[0]!=0:
			print(f"!!!!!WINNER  is player {row[0]} "+" won by horizontal matching")
			return(1)

	#vertical winner
	gp3=[]

	for i in range(len(grid)):
		for row in grid:
			gp3.append(row[i])
		if gp3.count(gp3[0])==len(grid) and gp3[0]!=0:
			print(f"!!!!!WINNER!is player {gp3[0]} !"+" won by vertical matching of " + str(i+1) + " column")
			return(1)
		gp3=[]


	#diagonal winner

		# \ type of digonal
	grp1=[]

	for i, row in enumerate(grid):
		grp1.append(row[i])
	if grp1.count(grp1[0])==len(grid) and grp1[0]!=0:
			print(f"!!!!!WINNER!!!  is player {grp1[0]} "+" won by \\ diagonal matching")
			return(1)


		# / type of diagonal
	grp2=[]

	n=list(range(len(grid)))
	m=list(reversed(range(len(grid))))


	for ind, row in zip(n,m):
		grp2.append(grid[ind][row])

	if grp2.count(grp2[0])==len(grid) and grp2[0]!=0:
			print(f"!!!!!WINNER!!  is player {grp2[0]} "+" won by / diagonal matching")
			return(1)
	
print("player 1 will start the game")
players=iter([1,2])
players=itertools.cycle(players)	

count=0
flag1=0
play=True
while play==True:
	count+=1
	if count==9:
		print("This game is a draw")
		play=False
	else:
		eng=win(grid)
		if eng==1:
			play=False
		

		row_choice=int(input("enter a row choice from [0,1,2]"))
		col_choice=int(input("enter a column choice from [0,1,2]"))


		if flag1==1:
			current_player=flag2
	    	
		else:
			current_player=next(players)

		print("\n the move played by ",current_player, "is: ")

		if grid[row_choice][col_choice]!=0:
			print("position already occupied please play again")
			flag1=1
			flag=grid[row_choice][col_choice]
			if flag==1:
				flag2=2
			else:
				flag2=1
		else:
			 grid[row_choice][col_choice]=current_player

  
    