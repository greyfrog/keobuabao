
import random
state=("keo","bua","bao")

play =False
nextRound="n"
print("toi luot ban, ban chon keo, bua hay bao\n")
playerState=input()

while(playerState!="keo" and playerState!="bua" and playerState!="bao" ):
	print( "nhap sai vui long nhap lai\n")
	print("toi luot ban, ban chon keo, bua hay bao\n")
	playerState=input()
if playerState=="keo" or playerState=="bua" or playerState=="bao":
	play=True
while play:
  	computerState=random.choice(state)
  	if computerState=="keo" and playerState=="keo":
  		print("Your choice is: "+ playerState+"\n")
  		print("Computer choice is: "+computerState+"\n")
  		print("draw\n")
  		play=False
  		print("wanna play next Round? y or n\n")
  		nextRound=input()
  		while nextRound!="y" and nextRound!="n":
  			print("wanna play next Round? y or n\n")
  			nextRound=input()
  		if nextRound=="y":
  			print("toi luot ban, ban chon keo, bua hay bao\n")
  			playerState=input()
  			while(playerState!="keo" and playerState!="bua" and playerState!="bao" ):
  				print( "nhap sai vui long nhap lai\n")
  				print("toi luot ban, ban chon keo, bua hay bao\n")
  				playerState=input()
  			if playerState=="keo" or playerState=="bua" or playerState=="bao":
  				play=True
  		elif nextRound=="n":
  			print("Game stop")
  			play=False
  	if computerState=="keo" and playerState=="bua":
   	
  		print("Your choice is: "+ playerState+"\n")
  		print("Computer choice is: "+computerState+"\n")
  		print("win\n")
  		play=False
  		print("wanna play next Round? y or n\n")
  		nextRound=input()
  		while nextRound!="y" and nextRound!="n":
  			print("wanna play next Round? y or n\n")
  			nextRound=input()
  		if nextRound=="y":
  			print("toi luot ban, ban chon keo, bua hay bao\n")
  			playerState=input()
  			while(playerState!="keo" and playerState!="bua" and playerState!="bao" ):
  				print( "nhap sai vui long nhap lai\n")
  				print("toi luot ban, ban chon keo, bua hay bao\n")
  				playerState=input()
  			if playerState=="keo" or playerState=="bua" or playerState=="bao":
  				play=True
  		elif nextRound=="n":
  			print("Game stop")
  			play=False
  	if computerState=="keo" and playerState=="bao":
  		print("Your choice is: "+ playerState+"\n")
  		print("Computer choice is: "+computerState+"\n")
  		print("lose\n")
  		play=False
  		print("wanna play next Round? y or n\n")
  		nextRound=input()
  		while nextRound!="y" and nextRound!="n":
  			print("wanna play next Round? y or n\n")
  			nextRound=input()
  		if nextRound=="y":
  			print("toi luot ban, ban chon keo, bua hay bao\n")
  			playerState=input()
  			while(playerState!="keo" and playerState!="bua" and playerState!="bao" ):
  				print( "nhap sai vui long nhap lai\n")
  				print("toi luot ban, ban chon keo, bua hay bao\n")
  				playerState=input()
  			if playerState=="keo" or playerState=="bua" or playerState=="bao":
  				play=True
  		elif nextRound=="n":
  			print("Game stop")
  			play=False
  	if computerState=="bua" and playerState=="keo":
  		print("Your choice is: "+ playerState+"\n")
  		print("Computer choice is: "+computerState+"\n")
  		print("lose\n")
  		play=False
  		print("wanna play next Round? y or n\n")
  		nextRound=input()
  		while nextRound!="y" and nextRound!="n":
  			print("wanna play next Round? y or n\n")
  			nextRound=input()
  		if nextRound=="y":
  			print("toi luot ban, ban chon keo, bua hay bao\n")
  			playerState=input()
  			while(playerState!="keo" and playerState!="bua" and playerState!="bao" ):
  				print( "nhap sai vui long nhap lai\n")
  				print("toi luot ban, ban chon keo, bua hay bao\n")
  				playerState=input()
  			if playerState=="keo" or playerState=="bua" or playerState=="bao":
  				play=True
  		elif nextRound=="n":
  			print("Game stop")
  			play=False
  	if computerState=="bua" and playerState=="bua":
  		print("Your choice is: "+ playerState+"\n")
  		print("Computer choice is: "+computerState+"\n")
  		print("draw\n")
  		play=False
  		print("wanna play next Round? y or n\n")
  		nextRound=input()
  		while nextRound!="y" and nextRound!="n":
  			print("wanna play next Round? y or n\n")
  			nextRound=input()
  		if nextRound=="y":
  			print("toi luot ban, ban chon keo, bua hay bao\n")
  			playerState=input()
  			while(playerState!="keo" and playerState!="bua" and playerState!="bao" ):
  				print( "nhap sai vui long nhap lai\n")
  				print("toi luot ban, ban chon keo, bua hay bao\n")
  				playerState=input()
  			if playerState=="keo" or playerState=="bua" or playerState=="bao":
  				play=True
  		elif nextRound=="n":
  			print("Game stop")
  			play=False
  	if computerState=="bua" and playerState=="bao":
  		print("Your choice is: "+ playerState+"\n")
  		print("Computer choice is: "+computerState+"\n")
  		print("win\n")
  		play=False
  		print("wanna play next Round? y or n\n")
  		nextRound=input()
  		while nextRound!="y" and nextRound!="n":
  			print("wanna play next Round? y or n\n")
  			nextRound=input()
  		if nextRound=="y":
  			print("toi luot ban, ban chon keo, bua hay bao\n")
  			playerState=input()
  			while(playerState!="keo" and playerState!="bua" and playerState!="bao" ):
  				print( "nhap sai vui long nhap lai\n")
  				print("toi luot ban, ban chon keo, bua hay bao\n")
  				playerState=input()
  			if playerState=="keo" or playerState=="bua" or playerState=="bao":
  				play=True
  		elif nextRound=="n":
  			print("Game stop")
  			play=False
  	if computerState=="bao" and playerState=="keo":
  		print("Your choice is: "+ playerState+"\n")
  		print("Computer choice is: "+computerState+"\n")
  		print("win\n")
  		play=False
  		print("wanna play next Round? y or n\n")
  		nextRound=input()
  		while nextRound!="y" and nextRound!="n":
  			print("wanna play next Round? y or n\n")
  			nextRound=input()
  		if nextRound=="y":
  			print("toi luot ban, ban chon keo, bua hay bao\n")
  			playerState=input()
  			while(playerState!="keo" and playerState!="bua" and playerState!="bao" ):
  				print( "nhap sai vui long nhap lai\n")
  				print("toi luot ban, ban chon keo, bua hay bao\n")
  				playerState=input()
  			if playerState=="keo" or playerState=="bua" or playerState=="bao":
  				play=True
  		elif nextRound=="n":
  			print("Game stop")
  			play=False
  	if computerState=="bao" and playerState=="bua":
  		print("Your choice is: "+ playerState+"\n")
  		print("Computer choice is: "+computerState+"\n")
  		print("lose\n")
  		play=False
  		print("wanna play next Round? y or n\n")
  		nextRound=input()
  		while nextRound!="y" and nextRound!="n":
  			print("wanna play next Round? y or n\n")
  			nextRound=input()
  		if nextRound=="y":
  			print("toi luot ban, ban chon keo, bua hay bao\n")
  			playerState=input()
  			while(playerState!="keo" and playerState!="bua" and playerState!="bao" ):
  				print( "nhap sai vui long nhap lai\n")
  				print("toi luot ban, ban chon keo, bua hay bao\n")
  				playerState=input()
  			if playerState=="keo" or playerState=="bua" or playerState=="bao":
  				play=True
  		elif nextRound=="n":
  			print("Game stop")
  			play=False
  	if computerState=="bao" and playerState=="bao":
  		print("Your choice is: "+ playerState+"\n")
  		print("Computer choice is: "+computerState+"\n")
  		print("draw\n")
  		play=False
  		print("wanna play next Round? y or n\n")
  		nextRound=input()
  		while nextRound!="y" and nextRound!="n":
  			print("wanna play next Round? y or n\n")
  			nextRound=input()
  		if nextRound=="y":
  			print("toi luot ban, ban chon keo, bua hay bao\n")
  			playerState=input()
  			while(playerState!="keo" and playerState!="bua" and playerState!="bao" ):
  				print( "nhap sai vui long nhap lai\n")
  				print("toi luot ban, ban chon keo, bua hay bao\n")
  				playerState=input()
  			if playerState=="keo" or playerState=="bua" or playerState=="bao":
  				play=True
  		elif nextRound=="n":
  			print("Game stop")
  			play=False















  	


