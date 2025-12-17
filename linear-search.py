# list ke elements ko ek ek krke check krte 
# chahe sorted ho ya unsorted
# for ex: searching th ebook in a row one bby one 
# First element se start karo
# Target se compare karo
# Agar match → mil gaya
# Nahi mila → next element
# End tak pahunch gaye → nahi mila

# def linear_search(arr, target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i
#         return -1   


# def linear_search(arr, target):
#     for  i in range(len(arr)):
#         if arr[i] == target:
#             return i
#         return -1




# FOR EXAMPLE 1:
# employee_ids = [101,102,103,104,105,106]
# target_id = 104

# index = linear_search(employee_id, target_id)

# if index != -1:
#     print("Employee Found at index:", index)
# else:
#     print("Employee not found")



# FOR EXAMPLE 2 :

# book_ids=[123,124,125,126,127,128]
# target_book= 127

# index = linear_search(book_ids, target_book)

# if index != -1:
#     print("Books found at index:", index)
# else:
#     print("Books not found")
