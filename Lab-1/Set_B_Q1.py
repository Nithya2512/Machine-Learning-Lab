def counting(arr):
    vowels=0
    consonants=0
    for i in arr:
        if i in "aeiouAEIOU":
            vowels+=1
        if i in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ":
            consonants+=1
    return vowels,consonants

sentence=input()
vowels,consonants=counting(sentence)
print("Vowels count=",vowels)
print("Consonants count=",consonants)