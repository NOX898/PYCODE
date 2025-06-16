import random

# ran_number = random.randint(1, 50)
#
#
# if ran_number % 2 != 0:
#
#     print(f'{ran_number} is a odd number.')
# else:
#     print(f'{ran_number} is a even number')

# answer = random.randint(1, 100)
#
# no_guess = 0
#
# print('Welcome to number guessing game!')
#
# while True:
#
#         print('*****************')
#         print('1. Play. ')
#         print('2. Exit. ')
#         print('*****************')
#         print()
#         choice = int(input('Enter your choice: '))
#
#         if choice == 2:
#             print('Thank you. Have a nice day!')
#             break
#
#         if choice not in range(1, 3):
#             print('Invalid choice!')
#             continue
#         while True:
#             if choice == 1:
#                 guess = int(input('Enter guess: '))
#                 if guess == answer:
#                     print('Nice guess!')
#                     print(f'Number of guesses: {no_guess}')
#                 elif guess > answer:
#                     print('To high!')
#                 elif guess < answer:
#                     print('To low!')
#                 elif guess != answer:
#                     print('Nice try! guess again.')
#NO.1
# odd_sum = 0
#
# print("Odd numbers from 50 to 1:")
#
# for num in range(50, 0, -1):
#     if num % 2 != 0:
#         print(num, end=' ')
#         odd_sum += num
#
# print("\nSum of odd numbers from 50 to 1:", odd_sum)
#
# #NO. 2
#
# num = 10
# total_sum = 0
#
# print("Numbers from 10 to 50:")
#
# # Use while loop to generate numbers from 10 to 50
# while num <= 50:
#     print(num, end=' ')
#     total_sum += num
#     num += 1
#
# print("\nSum of numbers from 10 to 50:", total_sum)

#NO.1
# def area_circle(r):
#     return 3.14 * r * r
#
# def area_square(s):
#     return s * s
#
# r = int(input('Enter the area of circle: '))
# s = int(input('Enter the area of square: '))
# print('The area of the circle:', area_circle(r))
# print('The area of the square:', area_circle(s))

#NO.2
# def characters(text):
#     return len(text)
#
# sentence = input('Enter sentence: ')
# print('Total number of characters in the sentence:', characters(sentence))

# NO.3
# def percentage(score, total):
#     return (score / total) * 100
#
# Score = int(input('Enter your score: '))
# Total = int(input('Enter the Total: '))
# print('Percentage:', percentage(Score, Total),'%')

#NO.4
# def average(no1, no2, no3):
#     return (no1 + no2 + no3) / 3
#
# a = int(input('Enter first number: '))
# b = int(input('Enter second number: '))
# c = int(input('Enter third number: '))
# print('Average:', average(a, b, c))

#NO.5
# def check(username):
#     if username.isalnum() and 8 <= len(username):
#         return True
#     else:
#         return False
#
# name = input('Enter username: ')
#
# if check(name):
#     print('Username is Valid.')
# else:
#     print('Username in not Valid!')

#NO.1

# student_names = []
#
# for i in range(5):
#     names = input(f'ENTER NAME OF STUDENT {i+1}: ')
#     student_names.append(names)
#
# convert_tuple = tuple(student_names)
# print(convert_tuple)
#
# for name in convert_tuple:
#     print(name.upper())

#NO.2

# words = []
#
# for i in range(5):
#     word = input(f'ENTER WORD {i+1}: ')
#     words.append(word)
#
# convert = tuple(words)
#
# for name in convert:
#     if name.endswith('n'):
#         print(name.upper())

#NO.3

# numbers = []
#
# for i in range(10):
#     num = int(input(f'ENTER A NUMBER {i + 1}:'))
#     numbers.append(num)
#
# for num in numbers:
#     if num % 2 == 0 and num % 3 == 0:
#         print(num)

#NO.1

# num_dic = {}
#
# for get in range(5):
#     num = int(input(f'ENTER NUMBER {get + 1}: '))
#     num_dic[num] = num ** 2
#
# print(num_dic)

#NO.2

# names_marks = {}
#
# for get in range(5):
#     name = input(f'ENTER NAME OF STUDENT {get + 1}: ').upper()
#     mark = float(input(f'ENTER THE MARK FOR {name}: '))
#     names_marks[name] = mark
#
# for name, mark in names_marks.items():
#     print(f'{name}: {mark}')

# #NO.3
# words = ['game', 'minecraft', 'mobile']
#
# dic_words = {word: len(words) for word in words}
#
# print(dic_words)

#NO.1

# set1 = {num for num in range(100) if num % 2 != 0}
#
# print(set1)

#NO.2

names = {'anak', 'ama', 'abdula'}

set2 = {name for name in names if name.endswith('a')}

print(set2)
















