S= input()
punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
no_semicolon=""
for k in S:
   if k not in punctuations:
       no_semicolon+=char
print(no_semicolon)
