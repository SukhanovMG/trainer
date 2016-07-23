import re
import random

class Trainer:
	__pattern = r"([xX]+)([\+\-\*/\^]+)([xX]*)"
	__settings_req = "Settings: "
	def __init__(self):
		self.__settings_str = input(self.__settings_req)
		self.__match_obj = re.match(self.__pattern, self.__settings_str)
		if not self.__match_obj:
			raise ValueError("Bad settings (match is None)", self.__settings_str)
		self.__match_groups = self.__match_obj.groups()
		if len(self.__match_groups) != 2 and len(self.__match_groups) != 3:
			raise ValueError("Bad settings (number of matched groups)", self.__match_groups)
		self.__len_first = len(self.__match_groups[0])
		

t = Trainer()

