""" 
Text Type : 
- String
Numeric Type : 
- Interger
- Float
- Complex
Sequence Type: 
- List
- Tuple
- range
Mapping Type:
- Dictionary
Set Type :
- Set
- Frozenset
Binary Type :
- byte
- bytearray
- memoryview
None Type :
- None
Boolean Type :
- bool
"""

student_name = "Today is Great" # str
student_age = 27 # int
student_height = 6.7 # float
student_id = 5j # complex
student_names_list = ["Kola", "Abdul", "Rakiya"] # list
student_names_tuple = ("Kola", "Abdul", "Rakiya") # tuple
student_scores = [1, 2, 3, 4, 5, 6, 7] # list
student_names_range = range(1, 8) # range
all_student_scores = {
"Math" : 87,
"GNS101" : 80,
"COM101" : 80,
} # dictionary
student_grade = {"A1", "B2", "B1", "A1"} #set
student_grade_2 = ({"A1", "B2", "B1", "A1"}) #frozenset
is_today_sunday = True # boolean
is_tomorrow_weekend = False # boolean
my_bytes = b"today is awesome"
my_byte_array = bytearray(55) #bytearray
my_memory_view = memoryview(bytes(4)) #memoryview
my_none = None #NoneType

# check data type of a variable or value
print(type(student_name))
print(type(student_age))
print(type(student_height))
print(type(student_id))
print(type(student_names_list ))
print(type(student_names_tuple))
print(type(student_scores))
print(type(student_names_range))
print(type(student_grade))
print(type(is_today_sunday ))
print(type(is_tomorrow_weekend))
print(type(my_bytes))
print(type(my_byte_array))
print(type(my_memory_view))
print(type(my_none))