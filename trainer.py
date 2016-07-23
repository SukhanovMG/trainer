import re
import random

class Operand:
	def __init__(self, length = 2):
		if length <= 0:
			raise ValueError("Operand length must be greater than zero")
		self.__length = length
		self.__bounds = (10**(length - 1), 10**length - 1)
		self.__last = 0

	# get operator length
	def get_length(self):
		return self.__length

	# get a random operand within inited bounds
	def get(self):
		self.__last = random.randint(self.__bounds[0], self.__bounds[1])
		return self.__last

	# return last generated operand
	def get_last(self):
		return self.__last

class Operation:
	__pattern = r"([\+\-\*/\^])"
	__operation_dict = {
		"+" : lambda x, y : x +  y,
		"-" : lambda x, y : x -  y,
		"*" : lambda x, y : x *  y,
		"/" : lambda x, y : x /  y,
		"^" : lambda x    : x ** 2
	}

	def __init__(self, operator_string = "+-"):
		# find all valid operands in string
		self.__operators = re.findall(self.__pattern, operator_string)
		if len(self.__operators) == 0:
			raise ValueError("Operator string does not contain valid operators")
		# remove dublicates
		self.__operators = list(set(self.__operators))
		self.__last = (self.__operators[0], self.__operation_dict[self.__operators[0]])
		
	# get a random function
	def get(self):
		operator_index = random.randint(0, len(self.__operators) - 1)
		operator = self.__operators[operator_index]
		self.__last = (operator, self.__operation_dict[operator])
		return self.__last

	def get_last(self):
		return self.__last




class Trainer:
	__pattern = r"([xX]+)([\+\-\*/\^]+)([xX]*)"
	def __init__(self, settings_str):
		self.__match_obj = re.match(self.__pattern, settings_str)
		if not self.__match_obj:
			raise ValueError("Bad settings (match is None)", settings_str)
		self.__match_groups = self.__match_obj.groups()
		if len(self.__match_groups) != 2 and len(self.__match_groups) != 3:
			raise ValueError("Bad settings (number of matched groups)", self.__match_groups)
		self.__left_operand = Operand(len(self.__match_groups[0]))
		self.__right_operand = Operand(self.__match_groups[2] and len(self.__match_groups[2]) or 1)
		self.__op = Operation(self.__match_groups[1])

	def train(self):
		while True:
			l = self.__left_operand.get()
			r = self.__right_operand.get()
			op = self.__op.get()
			ask_str = "{} {} {} = ".format(l, op[0], r)
			res_str = "{} {} {} = {}".format(l, op[0], r, op[1](l, r))
			input(ask_str)
			print(res_str)

		

random.seed()
settings = input("Settings: ")
t = Trainer(settings)
t.train()

