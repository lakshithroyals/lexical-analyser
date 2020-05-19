import re
keyword = ['Begin','End','or', 'exe', 'test', 'int', 'repeat', 'alpha', 'times', 'bool']
oper = ['+', '-', '*', '/', '=', '<', '>', '<=', '>=', '==', '!=']
delim = ['\t','\n','(',')','{','}','[',']', ' ',]
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
boolean=['True','False']
alpha =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','z','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
def is_key(kw):
	if kw in keyword:
		return True
	return False

def is_bool(key):
	if key in boolean:
		return True
	return False
	
def is_delim(char):
	if char in delim:
		return True
	return False

def is_digit(char):
	if char in num:
		return True
	elif char.isdigit()==True:
		return True
	return False

def is_alpha(char):
	if char in alpha:
		return True
	return False

def is_assignope(char):
	if char =='$':
		return True
	return False

def is_seperator(char):
	if char ==',':
		return True
	return False
def is_oper(char):
	if char in oper:
		return True
	return False

fo=open("input",'r')
temp=fo.read()
lexims=re.findall("\s*(?:(\d+)|(\w+)|(.))",temp)
for i in range(len(lexims)):	
	for j in range(len(lexims[i])):
		if(lexims[i][j]!=''):
			print(lexims[i][j], end='			')
			if(is_key(lexims[i][j])==True):
				print("Keyword")
			elif(is_bool(lexims[i][j])==True):
				print("Boolean Values")
			elif(is_delim(lexims[i][j])==True):
				print("Braces")
			elif(is_digit(lexims[i][j])==True):
				print("Integer")
			elif(is_alpha(lexims[i][j])==True):
				print("Alphabet(character)")
			elif(is_oper(lexims[i][j])==True):
				print("Operator")
			elif(is_assignope(lexims[i][j])==True):
				print("Assignment Operator")
			elif(is_seperator(lexims[i][j])==True):
				print("Seperator Operator")
			
			else:
				print("Variable")
