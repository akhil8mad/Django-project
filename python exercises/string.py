#Appending new string in the middle of a given string


s1="akhil"
s2="dude"

#getting the middle of string1 
s3=int(len(s1)/2) #it will store midpoint value
string_new=s1[:s3]+s2+s1[s3:]  #accessing the string
print(string_new)




