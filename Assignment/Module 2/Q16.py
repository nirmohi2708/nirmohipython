# WAP to count the occurrences of each word in a given sentence

v=input("Enter string:")
a=[]
count=0
a=str.split(" ")
for i in range(0,len(a)):
      if(word==a[i]):
            count=count+1
print("Count of the word is:")
print(count)
