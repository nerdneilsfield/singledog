import re
import math
class transformathions(object):
	def __init__(self,input):
		self.input = input.replace('translate','#').replace('rotate','$').replace('scale','&')
	def trans(self):
		if len(re.findall(r'[\$\#\&]+',self.input,re.S)) > 0:
			self.translate()
			self.rotate()
			self.scale()
			self.trans()
		else:
			# print(self.input)
	def translate(self):
		transthing = re.findall(r'\#\(([a-z]{3,6}\([0-9\,\.\-]+?\)[0-9\,\.\-]+?\))',self.input,re.S)
		another= re.split(r'\#\([a-z]{3,6}\([0-9\,\.\-]+?\)[0-9\,\.\-]+?\)',self.input,re.S)
		temp = another[0]
		for tans_obj in transthing:
			type_ = re.findall(r"[a-z]{3,6}",tans_obj,re.S)[0]
			params = re.findall(r"\(([0-9\,\.\-]+?)\)",tans_obj,re.S)[0].split(',')
			pingyi = re.findall(r"\)\,([0-9\,\.\-]+?)\)",tans_obj,re.S)[0].split(',')
			if  'line' in type_:
				params[0] = str(float(params[0]) + float(pingyi[0]))
				params[1] = str(float(params[1]) + float(pingyi[1]))
				params[2] = str(float(params[2]) + float(pingyi[0]))
				params[3] = str(float(params[3]) + float(pingyi[1]))
			else:
				params[0] = str(float(params[0]) + float(pingyi[0]))
				params[1] = str(float(params[1]) + float(pingyi[1]))
			temp = temp + type_ +'('+','.join(params)+')'+another[transthing.index(tans_obj)+1]
		self.input = temp
	def scale(self):
		transthing = re.findall(r'\&\(([a-z]{3,6}\([0-9\,\.\-]+?\)[0-9\,\.\-]+?\))',self.input,re.S)
		another= re.split(r'\&\([a-z]{3,6}\([0-9\,\.\-]+?\)[0-9\,\.\-]+?\)',self.input,re.S)
		temp = another[0]
		for tans_obj in transthing:
			type_ = re.findall(r"[a-z]{3,6}",tans_obj,re.S)[0]
			params = re.findall(r"\(([0-9\,\.\-]+?)\)",tans_obj,re.S)[0].split(',')
			scale = float(re.findall(r"\)\,([0-9\,\.\-]+?)\)",tans_obj,re.S)[0])
			if 'line' in type_ or 'rect' in type_:
				params[0] = str(float(params[0]) * scale)
				params[1] = str(float(params[1]) * scale)
				params[2] = str(float(params[2]) * scale)
				params[3] = str(float(params[3]) * scale)
			else:
				params[0] = str(float(params[0]) * scale)
				params[1] = str(float(params[1]) * scale)
				params[2] = str(float(params[2]) * scale)
			temp = temp + type_ +'('+','.join(params)+')'+another[transthing.index(tans_obj)+1]
		self.input = temp
	def rotate(self):
		transthing = re.findall(r'\$\(([a-z]{3,6}\([0-9\,\.\-]+?\)[0-9\,\.\-]+?\))',self.input,re.S)
		another= re.split(r'\$\([a-z]{3,6}\([0-9\,\.\-]+?\)[0-9\,\.\-]+?\)',self.input,re.S)
		temp = another[0]
		for tans_obj in transthing:
			type_ = re.findall(r"[a-z]{3,6}",tans_obj,re.S)[0]
			print(type_)
			params = re.findall(r"\(([0-9\,\.\-]+?)\)",tans_obj,re.S)[0].split(',')
			normal = float(re.findall(r"\)\,([0-9\,\.\-]+?)\)",tans_obj,re.S)[0])
			theata = normal*(math.pi/180)
			if 'line' in type_:
				params[0] = str(float(params[0])*math.cos(theata) - float(params[1])*math.sin(theata))
				params[1] = str(float(params[0])*math.sin(theata) + float(params[1])*math.cos(theata))
				params[2] = str(float(params[2])*math.cos(theata) - float(params[3])*math.sin(theata))
				params[3] = str(float(params[2])*math.sin(theata) + float(params[3])*math.cos(theata))
				print(params)
			elif 'rect' in type_:pass
			elif 'sector' in type_:
				params[0] = str(float(params[0])*math.cos(theata) - float(params[1])*math.sin(theata))
				params[1] = str(float(params[0])*math.sin(theata) + float(params[1])*math.cos(theata))
				params[3] = str(float(params[3])+theata)
				params[4] = str(float(params[4])+theata)
			else:
				params[0] = str(float(params[0])*math.cos(theata) - float(params[1])*math.sin(theata))
				params[1] = str(float(params[0])*math.sin(theata) + float(params[1])*math.cos(theata))
				params[3] = str(float(params[3])+theata)
			temp = temp + type_ +'('+','.join(params)+')'+another[transthing.index(tans_obj)+1]
		self.input = temp
test_case = "rotate(tri(1,2,3,0),3)"
test = transformathions(test_case)
test.trans()