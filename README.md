# Binary-Encoder
Encoding strings in a unconventional way

This program takes a string as input and converts it to a float number. This number is encrypted version of that string. using decrypt program can decode the string.

Steps of Encoding:
1. Convert the string to 1 and 0 (binary version of the string)
1. Convert that base2 number to base10
1. Scramble that number
    - Take the length of the number
    - Find the highest divider that is less than 10
    - If number is greater than or equal to 10
        - If highest divider is 1 than split each digit
        - If highest divider is greater than 1 split the number to n number each number containing length/divider digits of the number
    - If number is less than 10
        - Slice the number from the middle
        - (if length is even divider is 0, else divider is -1)
    - Create a new string that starts with the hightest divider and a comma after the divider ('3,')
    - Add chunks of the number in reversed order
    - Finally program gives a float number in string

For decoding, program splits the float number into 2 parts, before and after comma. The part before comma is divider, after comma is the scrambled number. Than program reverses the steps of encoding.
