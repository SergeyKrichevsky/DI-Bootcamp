#CH1

MATRIX_STR = '''
7ii
Tsx
h%?
i #
sM 
$a 
#t%'''       


# Step 1: Transforming the String into a 2D List

rows = MATRIX_STR.strip().split('\n')
#print(rows)

new_matrix_as_2d_list = []

for index, str in enumerate(rows):
    new_matrix_as_2d_list.append(list(str))
#print(new_matrix_as_2d_list)


# Step 2: Processing Columns 
# &
# Step 3: Filtering Alpha Characters

temp_str = ''

for i in range(len(new_matrix_as_2d_list[0])):
    for row_index, row in enumerate(new_matrix_as_2d_list):
        char = new_matrix_as_2d_list[row_index][i]
        if char.isalpha():
            temp_str = f'{temp_str}{char}'
print(temp_str)

char_index = 0

for i in range(len(new_matrix_as_2d_list[0])):
    for row_index, row in enumerate(new_matrix_as_2d_list):
        char = new_matrix_as_2d_list[row_index][i]
        if char.isalpha():
            char_index += 1
            #print(char_index)
        else:
            if temp_str[char_index] != ' ':
                       print(temp_str)#
                       print(char_index)#
                       print(temp_str[char_index])#
                       temp_str = temp_str[: char_index+1] + ' ' + temp_str[char_index+1 :]
                       print(temp_str)#
                       char_index += 1
                       #print(char_index)#
     

### QUESTION TO THE TEACHER:
        
# for i in range(len(new_matrix_as_2d_list[0])):
#     for row_index, row in enumerate(new_matrix_as_2d_list):
#         char = new_matrix_as_2d_list[row_index][i]
#         if char.isalpha():
#             char_index += 1
#             #print(char_index)
#         else:
#             if temp_str[char_index] != ' ':
#                        print(temp_str)#
#                        print(char_index)#
#                        print(temp_str[char_index])#
#                        temp_str = temp_str[: char_index+1] + ' ' + temp_str[char_index+1 :]
#                        print(temp_str)#
#                        char_index += 1
#                        #print(char_index)#
     


# print(char_index)
# print(temp_str)
        


# Step 4: Replacing Symbols with Spaces

# a = 10
# a += 1
# print(a)