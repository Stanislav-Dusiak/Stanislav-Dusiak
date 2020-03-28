""""Petya started to attend programming lessons. On the first lesson his task
was to write a simple program. The program was supposed to do the following:
in the given string, consisting if uppercase and lowercase Latin letters, it:
deletes all the vowels, inserts a character "." before each consonant, replaces
 all uppercase consonants with corresponding lowercase ones. Vowels are
 letters "A", "O", "Y", "E", "U", "I", and the rest are consonants.
 The program's input is exactly one string, it should return the output as a
 single string, resulting after the program's processing the initial string.
Help Petya cope with this easy task.
Input
The first line represents input string of Petya's program. This string only
consists of uppercase and lowercase Latin letters and its length is
from 1 to 100, inclusive.

Output
Print the resulting string. It is guaranteed that this string is not empty."""

a = input()
b = a.replace('A', '')
b1 = b.replace('O', '')
b2 = b1.replace('Y', '')
b3 = b2.replace('E', '')
b4 = b3.replace('U', '')
b5 = b4.replace('I', '')
b6 = b5.replace('a', '')
b7 = b6.replace('o', '')
b8 = b7.replace('y', '')
b9 = b8.replace('e', '')
b10 = b9.replace('u', '')
b11 = b10.replace('i', '')
c = b11.replace('', '.')
v = c[:-1]
print(v.lower())

