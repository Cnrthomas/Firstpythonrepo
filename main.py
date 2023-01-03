print(30) #you can print values directly

age = 30 #you can set a value as a variable
print(age) #and then print that variable

print('hello world') #you can print text as a string using '' around the text

#numbers come in 2 forms, integers and floats
age = 30 #integers are whole numbers
Pi = 3.14159 #floats are decimals

math_test = 1+3*4/2-2
#python can evaluate all basic math operations using PEMDAS, so the above equation will give the answer 5
print(math_test)
#using division will always provide the answer in float form, even if the answer is a whole number. So the above result prints as 5.0

#to remove the data after the decimal when dividing, just add an extra slash as shown in division_test2 below
division_test = 8/3
print(division_test)
division_test2 = 8//3
print(division_test2)
#note that this does not round the number up or down, it simply removes the data after the decimal

#to find the remainder when dividing, use the percent symbol % which is called the modulus operator in python. It will replace the slash we normally use to divide and instead of giving us the float answer, it will complete the division and let us know what is left over. See below.
remainder_test = 13%5
print(remainder_test)
#5 goes into 13 2 times, with a remainder of 3. If we want the exact answer of 13 divided by 5, we format the variable as 13/5, if we want how many times 5 goes into 13, we format it as 13//5, and if we want what's left over after 5 has gone into 13 as much as it can, we format it as 13%5

print('yeehaw')

#the modulus operator can be used to determine if a number is odd or even, which is quite useful when coding(think about alternating the colors of rows in a table). To do this, simply divide your number by 2 using the modulus operator. If the result is 0, the number is even; and if the result is 1, the number is odd. See below.
print(12%2)
print(13%2)
x = 17
y = 24
print(x%2)
print(y%2)
