import random
"""
python string can either be sorrounded by single quote,
double quote, tripple single quote or double tripple quote
"""

# line = "Today is going to be great " # double quote
# line2 = 'Today is going to be great day' # single quote
# poem1 = """
# Tick says te clock, tick, tick
# what you have to do, do quick
# "all that glitter is not Gold" - African proverb
# """
# poem1 = '''
# Tick says te clock, tick, tick
# what you have to do, do quick
# '''

# # string are array in python
#           #0123456789
# a_array = "I am Great"

# print(a_array[1])

# for x in "student name" :
#     print(x)
    
# print(len("I am great"))

# print('am' in a_array)
# print('am' not in a_array)

"""
slicing
0:4
[1, 2, 3, 4]
[1, 2, 3, 4, 5]
[start:end:skip]
"""
# indexing        0123456789
slicing_string = 'files/image/my_real_image.png'
# if you do not specify the start, it automatically extract from the first
# item or character, same thing with the end, by the deafult the skip is 1
# print(slicing_string[12:])
# print(slicing_string[:12])
# print(slicing_string[::-1])

# support negative slicing and indexing
# print(slicing_string[-1])
# print(slicing_string[-5:-1])
# print(slicing_string[-5:-1])
# print(slicing_string[0])

# #slicing
# print(slicing_string[0:3])


# #skipping
# # print(slicing_string[0:9:1])
# print(slicing_string[0:9:2])

# String Methods and modification

""" 
1. capitalize(): Returns a string with the first character capitalized and the rest of the characters in lowercase.
2. casefold(): Returns a string with all characters converted to lowercase and all non-ASCII characters removed.
3. center(): Returns a string centered in a field of a specified width.
4. count(): Returns the number of occurrences of a specified substring in the string.
5. encode(): Encodes the string using a specified encoding (e.g. UTF-8).
6. endswith(): Returns True if the string ends with a specified suffix.
7. expandtabs(): Returns a string with tabs expanded to spaces.
8. find(): Returns the index of the first occurrence of a specified substring in the string.
9. format(): Returns a string formatted with the specified arguments.
10. format_map(): Returns a string formatted with the specified arguments using the format_map protocol.
11. index(): Returns the index of the first occurrence of a specified substring in the string.
12. isalnum(): Returns True if the string contains only alphanumeric characters.
13. isalpha(): Returns True if the string contains only alphabetic characters.
14. isascii(): Returns True if the string contains only ASCII characters.
15. isdecimal(): Returns True if the string contains only decimal characters.
16. isdigit(): Returns True if the string contains only digit characters.
17. isidentifier(): Returns True if the string is a valid identifier (e.g. a variable name).
18. islower(): Returns True if the string contains only lowercase characters.
19. isnumeric(): Returns True if the string contains only numeric characters.
20. isprintable(): Returns True if the string contains only printable characters.
21. isspace(): Returns True if the string contains only whitespace characters.
22. istitle(): Returns True if the string is a title (i.e. the first character of each word is capitalized).
23. isupper(): Returns True if the string contains only uppercase characters.
24. join(): Returns a string joined with the specified separator.
25. ljust(): Returns a string left-justified in a field of a specified width.
26. lower(): Returns a string with all characters converted to lowercase.
27. lstrip(): Returns a string with leading whitespace removed.
28. maketrans(): Returns a translation table for use with the translate() method.
29. partition(): Returns a tuple containing the string partitioned into three parts: the part before the first separator, the separator itself, and the part after the separator.
30. replace(): Returns a string with all occurrences of a specified substring replaced with a new substring.
31. rfind(): Returns the index of the last occurrence of a specified substring in the string.
32. rindex(): Returns the index of the last occurrence of a specified substring in the string.
33. rjust(): Returns a string right-justified in a field of a specified width.
34. rpartition(): Returns a tuple containing the string partitioned into three parts: the part before the last separator, the separator itself, and the part after the separator.
35. rsplit(): Returns a list of substrings split from the string using a specified separator.
36. rstrip(): Returns a string with trailing whitespace removed.
37. split(): Returns a list of substrings split from the string using a specified separator.
38. splitlines(): Returns a list of substrings split from the string using newline characters as separators.
39. startswith(): Returns True if the string starts with a specified prefix.
40. strip(): Returns a string with leading and trailing whitespace removed.
41. swapcase(): Returns a string with all characters converted to the opposite case (i.e. uppercase to lowercase and vice versa).
42. title(): Returns a string with the first character of each word capitalized.
43. translate(): Returns a string translated using a specified translation table.
44. upper(): Returns a string with all characters converted to uppercase.
"""

mod_string = "Frank Barrenson"
slicing_string = 'files/image/my_real_image.png'


# print("Converting to upper : ", mod_string.upper())
# print("Converting to lower : ", mod_string.lower())
# print("change it to lower where there is upper : ", mod_string.casefold())
# print("Capitalize the first letter : ", mod_string.capitalize())
# print("return how many time a subtring appeared : ", mod_string.count("a"))
# print("count specifying index", mod_string.count("a", 3))
# print("check if a string end with a certain substring : ", slicing_string.endswith(".png"))

# all_file = []
# image_folder = []
# for d in range(1000) :
#     list_of_file_extensions = [".png", ".jpg", ".jpeg", ".gif", ".mp4", ".avi", ".mov", ".py", ".pdf"]
#     file_name = "abcdefghijklmnopqrstuvwxyz"
#     list_initial = random.choices(file_name, k=8)
#     name_initial = ""
#     x = name_initial.join(list_initial)
#     x = x + random.choice(list_of_file_extensions)
#     all_file.append(x)
    
# for file in all_file :
#     if file.endswith(".avi") :
#         image_folder.append(file)
        
# print(image_folder)

#concatenating string in python

# my_a = "My name is "
# my_b = "Suleiman Raji"

# print(my_a + my_b)


# string Formatting
# userName = input("Enter your username? : ")
# userAge = int(input("Enter your Age? : "))
# userHeight = float(input("Enter your Height? : "))
# amount_to_pay = int(input("Enter Amount? : "))

# # using the f
# print(f"""
# Your Name is {userName},
# You are {userAge * 5} year old.
# Your height is {userHeight}
# You just pay {amount_to_pay:,}
# """)

# using .format()
# print("""
# Your Name is {},
# You are {} year old.
# Your height is {}
# """.format(userName, userAge, userHeight))

# using key word format()
# print("""
# Your Name is {a},
# You are {b} year old.
# Your height is {c}
# """.format(a = userName, b = userAge, c = userHeight))

# using index format()
# print("""
# You are {1} year old.
# Your Name is {0},
# Your height is {2:.3f}
# """.format(userName, userAge, userHeight))

# using the percent symbol
# print("""
# You are %s year old.
# Your Name is %i,
# Your height is %f
# """%(userName, userAge, userHeight))

# Escape Characters
# quote_of_the_year = "Robert Schuller once said \"Beginning is half start\""
# quote_of_the_year = "Robert Schuller once said \\* Beginning is half start"
# quote_of_the_year = "Robert Schuller once said \n : Beginning is half start" # new line
quote_of_the_year = "\tRobert Schuller once said \n : \tBeginning is half start" # new line

print(quote_of_the_year)