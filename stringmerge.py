#merging the list of two strings using zip command
string2=["i","am","fine","thank","you","hey"]
string3=["hi","hello","how","are","you","hi"]
string3=[(i,j) for i,j in zip(string2,string3)]
print(string3)
