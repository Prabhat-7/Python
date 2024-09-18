import string
import random as r
a= int(input("What do you want to do?(1.Code/2.Decode):"))
str=input("Enter the string:")
match a:
    case 1:
        str=str.split(" ")
        str2=""
        for word in str:
             if(len(word)<=2):
                 str2+=word[::-1]+" "
             else:
                word=word.replace(word[0],"")+ word[0] 
                fstr=""
                lstr=""
                for i in range (3):
                    fstr+=r.choice(string.ascii_letters)
                    lstr+=r.choice(string.ascii_letters)
                str2+=fstr+word+lstr+" "
        print(str2)
    case 2:
        str=str.split(" ")
        str2=""
        for word in str:
            if(len(word)<=2):
                 str2+=word[::-1]+" "
            else:
                word=word[3:-3]
                word= word[-1]+word.replace(word[-1],"")
                str2+=word + " " 
        print(str2)