word=input()
i=count1=count2=0
while(word[i]!="("):
    count1+=1
    i+=1
j=len(word)-1
while(word[j]!=")"):
    count2+=1
    j-=1
if(count1==count2):
    print("correct")
else:
    print("fix")
