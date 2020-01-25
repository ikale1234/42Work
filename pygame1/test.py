word = input("Type a word: ")

count = 0
v= 0
c = 0
vowels = ["a","e","i","o","u"]
cons = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
while count< len(word):
    if word[count] in vowels:
        v+=1
    if word[count] in cons:
        c+=1
    count+=1
print ("The word has "+str(v)+" vowels and "+str(c)+" consonants.")
