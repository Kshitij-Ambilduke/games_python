import random2
import msvcrt
import os

def start():
	try:
		print("PLEASE ENTER THE SIZE OF THE GRID AND THE WINNING NUMBER:\n IF AN INTEGER IS NOT ENTERED DEFAULT VALUE FOR SIZE AND WINNIN NUMBER WILL BE TAKEN\n(5x5,2048) ")
		cet=True
		while cet:
			x=int(input())	
			y=int(input())
			bin_win_number=list(bin(y))
			bin_win_number.pop(0)
			bin_win_number.pop(0)
			if bin_win_number.count('1')==1 and x>0 and y>1:
				cet=False
			else:
				print("*** size should be positive integer and winning number should be a power of 2 ***")
				print("ENTER VALID CHOICE")
		return x,y
	except:
		return 5,2048
			
def user_input():
	x=msvcrt.getch()
	return x

def shift_right(grid):
	for row in grid:
		for i in range(len(grid)-1):
			if row[-1-i]==0:
				row[-1-i],row[-2-i]=row[-2-i],row[-1-i]
	return(grid)
def final_right(grid):

	for i in range(len(grid)):
		grid=shift_right(grid)

	for row in grid:
		for i in range(len(grid)-1):
			if row[-1-i]==row[-2-i]:
				row[-1-i]=2*row[-1-i]
				row[-2-i]=0

	for i in range(len(grid)):
		grid=shift_right(grid)
	return grid


def shift_left(grid):
	for row in grid:
		for i in range(len(grid)-1):
			if row[i]==0:
				row[i],row[i+1]=row[i+1],row[i]
	return(grid)
def final_left(grid):
	for i in range(len(grid)):
		grid=shift_left(grid)

	for row in grid:
		for i in range(len(row)-1):
			if row[i]==row[i+1]:
				row[i]=2*row[i]
				row[i+1]=0

	for i in range(len(grid)):
		grid=shift_left(grid)
	return grid


def final_down(grid):
	grid=rot_grid(grid)
	grid=final_right(grid)
	grid=undo_rot_grid(grid)
	return(grid)


def final_up(grid):
	grid=rot_grid(grid)
	grid=final_left(grid)
	grid=undo_rot_grid(grid)
	return(grid)


def rot_grid(grid):
	rotated_grid=[]
	for i in list(reversed(range(len(grid)))):		
		temp=[]		
		for j in range(len(grid)):
			temp.append(grid[j][i])
		rotated_grid.append(temp)	
	return rotated_grid

def undo_rot_grid(grid):
	for i in range(3):
		grid=rot_grid(grid)
	return grid


def initial_grid(size):
	grid=[]
	for i in range(size):
		row=[]
		for j in range(size):
			row.append(0)
		grid.append(row)
	return grid


def random(grid):
	avail_spots=[]
	avail_spots_rows=[]
	avail_spots_cols=[]
	for i in range(len(grid)):
		for j in range(len(grid)):
			if grid[i][j]==0:
				avail_spots_rows.append(i)
				avail_spots_cols.append(j)
	avail_spots=list(zip(avail_spots_rows,avail_spots_cols))
	len_avail_spots=len(avail_spots)	
	if len_avail_spots-1==0:
		row,col=avail_spots[0]
		return row,col
	spot=random2.randint(0,len_avail_spots-1)
	row,col=avail_spots[spot]
	return row,col


def draw_grid(grid):
	os.system('cls')
	temp=[]
	temp2=[]
	for row in grid:
		for i in row:
			temp.append(i)
			temp2.append(i)
	for i in range(len(grid)):
		for j in range(len(grid)):
			if temp[j]==0:
				count=1
			else:	
				count=0
				while temp2[j]!=0:
					count+=1
					temp2[j]=temp2[j]//10

			print(temp[j],end=" ")
			for x in range(6-count):
				print(end=' ')
		print()
		print()
		for a in range(len(grid)):
			temp.pop(0)
			temp2.pop(0)


def invalid_move(grid,move):
	iterations=0
	if move==b's':
		x=list(range(len(grid)))
		y=list(range(len(grid)-1))
		for i in x:
			for j in y:
				if grid[j][i]!=grid[j+1][i] and grid[j+1][i]!=0:
					iterations+=1
				elif grid[j+1][i]==grid[j][i]==0:
					iterations+=1						
	elif move==b'a':
		x=list(reversed(range(len(grid))))
		y=list(reversed(range(len(grid)-1)))
		for i in x:
			for j in y:
				if grid[i][j+1]!=grid[i][j] and grid[i][j]!=0:
					iterations+=1		
				elif grid[i][j+1]==grid[i][j]==0:
					iterations+=1		
	elif move==b'w':
		x=list(reversed(range(len(grid))))
		y=list(reversed(range(len(grid)-1)))
		for i in x:
			for j in y:
				if grid[j+1][i]!=grid[j][i] and grid[j][i]!=0:
					iterations+=1
				elif grid[j+1][i]==grid[j][i]==0:
					iterations+=1									
	elif move==b'd':
		x=list(range(len(grid)))
		y=list(range(len(grid)-1))
		for i in x:
			for j in y:
				if grid[i][j]!=grid[i][j+1] and grid[i][j+1]!=0:
					iterations+=1
				elif grid[i][j]==grid[i][j+1]==0:
					iterations+=1
	mult=len(grid)**2 - len(grid)
	if mult==iterations:
		print("*** INVALID MOVE ***")
		main(grid)


def loser(grid):
	dek=[]
	a=0
	b=0
	for row in grid:
		for i in row:
			dek.append(i)
	c=dek.count(0)
	if c==0:
		for i in range(len(grid)):
			for j in range(len(grid)-1):
				if grid[i][j]==grid[i][j+1]:
					a=1
				if grid[j][i]==grid[j+1][i]:
					b=1
		if a==0 and b==0:
			draw_grid(grid)
			print()
			print("*** YOU HAVE LOST THE GAME ***")
			quit()

def winner(grid):
	for row in grid:
		for i in row:
			if i==win_number:
				print("****CONGRATULATIONS ON COMPLETING THE GAME****")
				quit()

def main(grid):
	play=True
	while play:				
		print()
		print()
		winner(grid)
		move=user_input()
		invalid_move(grid,move)
		if move==b'd':
			grid=final_right(grid)
		elif move==b'a':
			grid=final_left(grid)
		elif move==b'w':
			grid=final_up(grid)
		elif move==b's':
			grid=final_down(grid)
		else:
			print("*** PLEASE USE VALID KEYS FOR MOVES ***")
			main(grid)

		rnd=0
		for row in grid:
			for i in row:
				if i==0:
					rnd+=1
		if rnd!=0:
			row,col=random(grid)
			grid[row][col]=2
		loser(grid)
		draw_grid(grid)
			
size,win_number=start()
grid=initial_grid(size)
row=random2.randint(0,size-1)
col=random2.randint(0,size-1)
grid[row][col]=2
draw_grid(grid)
winner(grid)
loser(grid)
main(grid)




















