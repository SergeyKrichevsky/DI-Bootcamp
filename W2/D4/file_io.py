import os

dir_path = os.path.dirname(os.path.realpath(__file__))

# File I/O - INPUT/ OUTPUT

# OLD SCHOOL EAY OF OPENING A FILE WITH PYTHON
# file_object = open(r"W2\D4\secrets.txt")
# print(file_object)

# MODERN PYTHON WAY (AUTOMATICLY CLODED)

# with open(r"W2\D4\secrets.txt", encoding='utf-8') as file_obj:
#     # READING METHODS
    
#     # output = file_obj.read() # returns the whole content of the file
#     # output = file_obj.readline() #return one line
#     # output = file_obj.readlines() # return a list, where each line ia na alement
    
#     # print(output)
#     pass

# with open(r'W2\D4\starwars.txt', encoding='utf-8') as starwars_file:
#     # output = starwars_file.read()
#     # print(output)
#     # print('=' * 50)

#     # starwars_file.seek(0)

#     # output = starwars_file.readline()
#     # print(output.strip())
#     # print('=' * 50)
    
#     while True:
#         line = starwars_file.readline()
#         if not line:
#             break
#         print(line)

#     # output = starwars_file.readlines()
#     # print(output[4])

# MODE "w" - will rewrite the file
# with open(r"W2\D4\secrets.txt", 'w', encoding='utf-8') as file_obj:
#     file_obj.writelines('Hello Python I/O')

# MODE "a" - Adds writing
# with open(r"W2\D4\secrets.txt", 'a', encoding='utf-8') as file_obj:
    
#     file_obj.writelines('\nHello Python I/O')


# with open(f"{dir_path}/secrets.txt", 'a', encoding='utf-8') as file_obj:
#     file_obj.writelines('\nHello ----')


with open(f"{dir_path}/starwars.txt", 'r+', encoding='utf8') as sw_f:
    
    # lines_list = file_obj.readlines()
    # # print(lines_list)

    # # for line in lines_list:
    

    # for line in lines_list:
    #     if line == 'Luke':
    #         line.append(' SkyWalker')

    # for line in lines_list:
    #     print(line)

    list_str = sw_f.readlines()
    print(list_str)

    # splited_list = []
    # for line in list_str:
    #     splited_list.append(line.split())
    # print(splited_list)

    # for line in list_str:
    #     print(line.split())

    updated_name = []
    for line in list_str:
        if line == 'Luke\n':
            updated_name.append('Luke SkuWalker')

        output = ' '.join(updated_name)
        print(output)