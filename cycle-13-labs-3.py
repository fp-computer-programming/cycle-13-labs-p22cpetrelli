#author CJP 03/14/2022
#define function
def r_max(nested_num_lst):
# for loop
    for element in nested_num_lst:
        if type(element) == list:
            return max(element)
            
print(r_max([3, 4, 8, [30, 6]]))