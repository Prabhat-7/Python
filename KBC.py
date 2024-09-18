questions=[("What country has the highest life expectancy?","Hong Kong"),("Where would you be if you were standing on the Spanish Steps?","Rome"),("Which language has the more native speakers: English or Spanish?","Spanish"),("What is the most common surname in the United States?","Smith"),("What disease commonly spread on pirate ships?","Scurvy"),("Who was the Ancient Greek God of the Sun?","Apollo"),("What was the name of the crime boss who was head of the feared Chicago Outfit? ","Al Capone"),("What year was the United Nations established? ","1945"),("Who has won the most total Academy Awards?","Walt Disney"),("What artist has the most streams on Spotify?","Drake"),("How many minutes are in a full week?","10080"),("What car manufacturer had the highest revenue in 2020?","Volkswagen"),("How many elements are in the periodic table?","118")]
cash=["1K","2K","5K","10K","20K","50K","100K","200K","500K","1M","2M","5M","10M"]
checkPoints=[11,8,4]
correctAns=0
status=True        
def creds():
   if(status):
        global correctAns
        correctAns+=1
        print("Correct Answer!!\nCurrent Amount=$",cash[correctAns-1])
        if(correctAns==13):
            print("Congratulations!!!\n YOU WON $10M ")
        return 
   else:
       for i in checkPoints:
           if correctAns>=i:
                return print("Wrong Answer\n YOU WON $",cash[i-1])
       return print("Wrong Answer\n YOU WON $0")
           

while(len(questions)!=0 and status):
    q=questions.pop()
    ans=input(q[0])
    if(q[1]==ans):
       status=True
    else:
        status=False
    creds()
   