s=input('Enter a string:\n')
s=s.lower()
l=s.split()
n=len([i for i in l if i=='a' or i=='an' or i=='the'])
print(n)