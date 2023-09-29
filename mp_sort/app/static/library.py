from org.transcrypt.stubs.browser import *
import random

array=None
array_str=None
number=None
seed=None

def gen_random_int(number, seed):
	
	random.seed(seed)   # 设置种子值
	array = []		# 创建一个空列表		
	for i in range(number):		# 循环number次
		array.append(random.randint(0, 100))	# 生成一个0-100的随机整数，并添加到列表中
	return array

def bubble_sort(numbers):
    for i in range(len(numbers)): # loop through the list
        for j in range(len(numbers)-i-1):
            if int(numbers[j]) > int(numbers[j+1]):
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers



	



def generate():
	number = 10
	seed = 200


	array = gen_random_int(number, seed)
	array_str = ""
	for i in range(len(array)):
		array_str += str(array[i])
		if i != len(array) - 1:
			array_str += ", "
		else:
			array_str += "."
		#array = None
		# convert the items into one single string 
		# the number should be separated by a comma
		# and a full stop should end the string.
		#pass

		#array_str = None

		# This line is to placed the string into the HTML
		# under div section with the id called "generate"	
		document.getElementById("generate").innerHTML = array_str

	


		"""
		This function is used in Exercise 1.
		The function is called when the sort button is clicked.

		You need to do the following:
		- get the list of numbers from the "generate" HTML id, use document.getElementById(id).innerHTML
		- create a list of integers from the string of numbers
		- call your sort function, either bubble sort or insertion sort
		- create a string of the sorted numbers and store it in array_str	
		"""
def sortnumber1():
    array_str = document.getElementById("generate").innerHTML
    sortingarray = [int(i) for i in array_str[:-1].split(", ")]
    sortedarray = bubble_sort(sortingarray)
    array_str = "" #清零 value of array_str
    for i in range(len(sortedarray)):
        array_str += str(sortedarray[i])
        if i != len(sortedarray) - 1:
            array_str += ", "
        else:
            array_str += "."
    document.getElementById("sorted").innerHTML = array_str

def sortnumber2():
    '''	This function is used in Exercise 2.
        The function is called when the sort button is clicked.

        You need to do the following:
        - Get the numbers from a string variable "value".
        - Split the string using comma as the separator and convert them to 
            a list of numbers
        - call your sort function, either bubble sort or insertion sort
        - create a string of the sorted numbers and store it in array_str
    '''
    #获得 "numbers"的值
    value = document.getElementsByName("numbers")[0].value

    # 如果用户没有输入任何值，弹出警告
    if value == "":
        window.alert("Your textbox is empty")
        return

    # 将 string 变成 list of numbers
    numbers = [int(num.strip()) for num in value.split(",")]

    # Call  sort function
    sorted_numbers = bubble_sort(numbers)  
    # 转换回去，concert the list of sorted numbers to a string
    array_str = ",".join(str(num) for num in sorted_numbers)

    document.getElementById("sorted").innerHTML = array_str
