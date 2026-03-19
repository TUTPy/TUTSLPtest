# Problem 1: Check if a sequence of numbers appears in the list
#Check if a sequence of numbers appears in the list

def list_check(num):
    return 3 in num
print(list_check([0, 2, 3]))


#Problem 2: Extract every second character
def string_bit(str):
    return str[::2]
print(string_bit("heeololeo"))


#Problem 3: Check if one string is the end of the other
def end_other(a, b):
    a, b = a.lower(), b.lower()
    return a.endswith(b) or b.endswith(a)
print(end_other("Charles", "char")) 


#Problem 4: Double characters
def double_char(str):
    '''
    Return a string where for every char in the original, there are two chars.
    '''
    return ''.join([char * 2 for char in str])  

print(double_char("Hope"))

#Problem 5

def fix_teen(n: int) -> int:
    """
    Takes an integer and returns 0 if it's a 'teen' (13-19) except for 15 and 16.
    """
    return 0 if 13 <= n <= 19 and n not in (15, 16) else n

def no_teen_sum(a: int, b: int, c: int) -> int:
    """
    Returns the sum of three numbers, treating most teen numbers (13-19) as 0,
    except for 15 and 16, which are counted normally.
    """
    return fix_teen(a) + fix_teen(b) + fix_teen(c)

print(no_teen_sum(1, 15, 19))     
	
#Problem 6: Count even numbers

def count_evens(nums):
    return sum(1 for num in nums if num % 2 == 0)
print(count_evens([2, 1, 2, 6, 4]))