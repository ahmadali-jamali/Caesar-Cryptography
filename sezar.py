
#sezar coding:

def encrypt(text,s):
    
   result = ""
   # transverse the plain text
   for i in range(len(text)):
      char = text[i]
      if ord(char)>=65 and ord(char)<=90 or ord(char)>=97 and ord(char)<=122:
         # Encrypt uppercase characters in plain text
         
         if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
         # Encrypt lowercase characters in plain text
         else:
            result += chr((ord(char) + s - 97) % 26 + 97)
      else:
          result = result+char
          
   return result

#main function:
def main():
    
    s = int(input())
    text = str(input())
    print(encrypt(text,s))
    
#running
if __name__ == "__main__" :
    
    main()
    
