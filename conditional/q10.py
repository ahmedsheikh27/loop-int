
#10. Write a program to determine if a given character is a vowel or consonant.

word = input("Please enter a word: ")

vowel = 'aeiou'
find_vowel = [] 
for vowels in word:
 if vowels in vowel:
  find_vowel.append(vowels)
if find_vowel:
    print(f'The word "{word}" has the following vowel(s): {", ".join(find_vowel)}.')
else:
    print(f'The word "{word}" has no vowels in it.')
