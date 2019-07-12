z=input()
if(z=='a' or z=='A' or z=='e' or z=='E' or z=='i' or z=='I' or z=='o' or z=='O' or z=='u' or z=='U'):
  print("Vowel")
elif(z=='!' or z=='@' or z=='#' or z=='$' or z=='&' or z=='^' or z=='~' or z=='*' or z=='%' or z=='(' or z==')' or z=='_' or z=='-' or z=='=' or z=='[' or z==']' or z=='{' or z=='}' or z=='<' or z=='>' or z=='?' or z=='/' or z==';' or z=='.'):
  print("invalid")
else:
  print("Consonant")
