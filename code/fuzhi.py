import re
class fuzhi(object):
	def __init__(self,input):
		self.input = input
	def Fuzhi(self):
		variables = {}
		let_vari = re.findall(r'(let[a-zA-z\_]\w*?\=\d+)',self.input,re.S)
		anther = re.split(r'let[a-zA-z\_]\w*?\=\d+',self.input,re.S)
		print(anther)
		print(len(let_vari),len(anther))
		for vari in let_vari:
			varible = re.findall(r'let([a-zA-z\_]\w*?)\=\d+?',vari,re.S)[0]
			value = float(re.findall(r'\=(\d+)',vari,re.S)[0])
			variables[varible] = value
		print(variables)


test = "leta1a23=12sinw212letcos=12letshit=21212letlet=98"
te = fuzhi(test)
te.Fuzhi()