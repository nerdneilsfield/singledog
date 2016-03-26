#!/bin/env python3


import sys
import math
import re

class am_express_input(object):
	def __init__(self,input):
		self.input = re.sub(r'\s',' ',input)
		self.input = self.input.replace('{}','')
		# self.eval_e = r'[^\d\/\*\+\-]([\d\.]+?\s*?[\/\*\+\-]\s*?[\d\.]+)[^\d\/\*\+\-]'
		self.eval_e = r'[^\d\/\*\+\-]([\d\.\-]+?\s+?[\/\*\+\-]\s+?[\d\.\-]+)[^\d\/\*\+\-]'
		self.single_all = r"(\(\s*?[\d\.\-]+?\s*?\))"
		self.single = r"\(\s*?([\d\.\-]+?)\s*?\)"
		self.unary = r"[^\d\/\*\+\-]([sinco]{3}\s*?[\d\.\-]+)"
		self.value = r"[^\d\/\*\+\-][sinco]{3}\s*?([\d\.\-]+)"
	def caculator(self):
		try:
		
			import re
			cacu_thing = re.findall(self.eval_e,self.input,re.S)
			# print(cacu_thing,'\n')
			if not cacu_thing:
				cacu_unary = re.findall(self.unary,self.input,re.S)
				if not cacu_unary:pass 
				else:
					temp = ""
					dus = math.pi/180
					for cacu_ in cacu_unary:
						# print(cacu_)
						pos = self.input.find(cacu_)
						value_ = float(cacu_.split()[1])
						
						if "sin" in cacu_:
							ex_value = math.sin(dus*value_)
							temp = temp + self.input[:pos]+str(ex_value)
						elif "cos" in cacu_:
							ex_value = math.cos(dus*value_)
							temp = temp + self.input[:pos]+str(ex_value)
						self.input = self.input[pos+len(cacu_):]
					temp = temp + self.input
					self.input = self.__noSingle(temp)
					self.caculator()
			else:
				temp = ""
				for cacu_ in cacu_thing:
					pos = self.input.find(cacu_)
					temp = temp + self.input[:pos]+str(eval(cacu_))
					self.input = self.input[pos+len(cacu_):]
				temp = temp + self.input
				# print(temp,"\n")
				self.input = self.__noSingle(temp)
				self.caculator()
		except:pass
	def __noSingle(self,tem):
		import re
		singlers = re.findall(self.single_all,tem,re.S)
		if not singlers:
			return tem
		else:
			temp2 = ""
			# print(singlers)
			for singler_ in singlers:
				# print(singler_)
				pos = tem.find(singler_)
				sig = re.findall(self.single,singler_,re.S)
				# print(sig)
				temp2 = temp2 + tem[:pos] + sig[0]
				tem = tem[pos+len(singler_):]
				# print("end")
			temp2 = temp2 + tem
			return temp2
class picture(object):
	"""implements all of the draw things"""
	def __init__(self,type,params_list):
		"""Get the params and the type of drawing"""
		self.type = type
		self.params_list = params_list
		# print(params_list)
	def draw(self):
		if self.type == "line":
			self.drawline()
			self.end()
		elif self.type == "rect":
			self.drawrect()
			self.end()
		elif self.type == "tri":
			self.drawtri()
			self.end()
		elif self.type == "square":
			self.drawsquare()
			self.end()
		elif self.type == "penta":
			self.drawpenta()
			self.end()
		elif self.type == "ngon":
			self.drawngon()
			self.end()
		elif self.type == "hexa":
			self.drawhexa()
			self.end()
		elif self.type == "sector":
			self.drawsector()
			self.end()
		elif self.type == "linewidth":
			self.drawlinewidth()
		elif self.type == "color":
			self.setcolor()
		elif 'filled' in self.type:
			self.type = self.type.replace('filled','')
			eval("self.draw"+self.type+'()')
			self.fill()
		else:print("wrong input")
	def end(self):
		print("stroke")
	def fill(self):
		print("fill")
	def setcolor(self):
		r = float(self.params_list[0])
		g = float(self.params_list[1])
		b = float(self.params_list[2])
		print("%f %f %f"%(r,g,b))
	def drawlinewidth(self):
		k = float(self.params_list[0])
		print("%f setlinewidth"%k)
	def drawline(self):
		print("%s %s moveto"%(str(self.params_list[0]),str(self.params_list[1])))
		print("%s %s lineto"%(str(self.params_list[2]),str(self.params_list[3])))
		# print("stroke")
	def drawrect(self):
		x = float(self.params_list[0])
		y = float(self.params_list[1])
		w = float(self.params_list[2])
		h = float(self.params_list[3])
		print("%f %f moveto"%(x,y))
		print("%f %f lineto"%(x+w,y))
		print("%f %f lineto"%(x+w,y+h))
		print("%f %f lineto"%(x,y+h))
		print("%f %f lineto"%(x,y))
	def drawtri(self):
		self.params_list.append(3)
		self.drawngon()		
	def drawsquare(self):
		# x = float(self.params_list[0])
		# y = float(self.params_list[1])
		# r = float(self.params_list[2])
		# print("%f %f moveto"%(x+r,y))
		# print("%f %f lineto"%(x,y+r))
		# print("%f %f lineto"%(x-r,y))
		# print("%f %f lineto"%(x,y-r))
		# print("%f %f lineto"%(x+r,y))
		self.params_list.append(4)
		self.drawngon()
		# print("stroke")
	def drawngon(self):
		x = float(self.params_list[0])
		y = float(self.params_list[1])
		r = float(self.params_list[2])
		n = float(self.params_list[4])
		# print(self.params_list[3])
		normal = float(self.params_list[3])*(math.pi/180)
		theta = 2*math.pi/n
		print("%f %f moveto"%(x+r*math.cos(normal),y+r*math.sin(normal)))
		for i in range(int(n)):
			print("%f %f lineto"%(x+r*math.cos(normal+(i+1)*theta),y+r*math.sin(normal+(i+1)*theta)))
		# print("stroke")
	def drawpenta(self):
		self.params_list.append(5)
		self.drawngon()
	def drawhexa(self):
		self.params_list.append(6)
		self.drawngon()
	def drawsector(self):
		x = float(self.params_list[0])
		y = float(self.params_list[1])
		r = float(self.params_list[2])
		b = float(self.params_list[3])
		e = float(self.params_list[4])
		b_in_r = b*math.pi/180
		e_in_r = e*math.pi/180
		print("%f %f moveto"%(x,y))
		print("%f %f lineto"%(x+r*math.cos(b_in_r),y+r*math.sin(b_in_r)))
		print("%f %f %f %f %f arc"%(x,y,r,b%360,e%360))
		print("%f %f lineto"%(x,y))

class transformathions(object):
	def __init__(self,input):
		self.input = input.replace('translate','#').replace('rotate','$').replace('scale','&')
	def trans(self):
		if len(re.findall(r'[\$\#\&]+',self.input,re.S)) > 0:
			self.translate()
			self.rotate()
			self.scale()
			self.trans()
		else:pass
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
			# print(type_)
			params = re.findall(r"\(([0-9\,\.\-]+?)\)",tans_obj,re.S)[0].split(',')
			normal = float(re.findall(r"\)\,([0-9\,\.\-]+?)\)",tans_obj,re.S)[0])
			# print(params)
			theata = normal*(math.pi/180)
			# print(theata)
			if 'line' in type_:
				# print(math.cos(theata),math.sin(theata))
				# print(float(params[0])*math.sin(theata))
				# print(float(params[1])*math.cos(theata))
				# print((float(params[0])*math.sin(theata)) + (float(params[1])*math.cos(theata)))
				# print(str((float(params[0])*math.sin(theata)) + (float(params[1])*math.cos(theata))))
				x,y,z,t = params[0],params[1],params[2],params[3]
				params[0] = str(float(x)*math.cos(theata) - float(y)*math.sin(theata))
				params[1] = str((float(x)*math.sin(theata)) + (float(y)*math.cos(theata)))
				params[2] = str(float(z)*math.cos(theata) - float(t)*math.sin(theata))
				params[3] = str(float(z)*math.sin(theata) + float(t)*math.cos(theata))
	
			elif 'rect' in type_:pass
			elif 'sector' in type_:
				x,y,z,t = params[0],params[1],params[2],params[3]
				params[0] = str(float(x)*math.cos(theata) - float(y)*math.sin(theata))
				params[1] = str(float(x)*math.sin(theata) + float(y)*math.cos(theata))
				params[3] = str(float(params[3])+normal)
				params[4] = str(float(params[4])+normal)
			else:
				# print('heh')
				# print(params)
				# print(normal)
				x,y,z,t = params[0],params[1],params[2],params[3]
				params[0] = str(float(x)*math.cos(theata) - float(y)*math.sin(theata))
				params[1] = str(float(x)*math.sin(theata) + float(y)*math.cos(theata))
				params[3] = str(float(params[3])+normal)
			temp = temp + type_ +'('+','.join(params)+')'+another[transthing.index(tans_obj)+1]
		self.input = temp

def insert_ng(input_str):
	input_str = re.sub(r'\s*','',input_str)
	nglist= re.findall(r'ngon\s*?\(([0-9\,\s\.\-]+?)\)',input_str,re.S)
	ngothers = re.split(r'ngon\s*?\([0-9\,\s\-\.]+?\)',input_str,re.S )
	ng_tmp = ngothers[0]
	for list_ in nglist:
		temlist = list_.replace(' ','').split(',')
		temlist.insert(3,'0')
		tempstr = ','.join(temlist)
		ng_tmp = ng_tmp + "ngon("+tempstr+')'+ngothers[nglist.index(list_)+1]
	return(ng_tmp)
def inserfilled_ng(input_str):
	input_str = re.sub(r'\s*','',input_str)
	nglist= re.findall(r'filledngon\s*?\(([0-9\,\s\.\-]+?)\)',input_str,re.S)
	ngothers = re.split(r'filledngon\s*?\([0-9\,\s\.\-]+?\)',input_str,re.S )
	ng_tmp = ngothers[0]
	for list_ in nglist:
		temlist = list_.replace(' ','').split(',')
		temlist.insert(3,'0')
		tempstr = ','.join(temlist)
		ng_tmp = ng_tmp + "filledngon("+tempstr+')'+ngothers[nglist.index(list_)+1]
	return(ng_tmp)
def jiaongxi(input_str,type_):
	input_str = re.sub(r'\s*','',input_str)
	nglist= re.findall(r'%s\s*?\(([0-9\,\s\.\-]+?)\)'%type_,input_str,re.S)
	ngothers = re.split(r'%s\s*?\([0-9\,\s\.\-]+?\)'%type_,input_str,re.S )
	ng_tmp = ngothers[0]
	for list_ in nglist:
		temlist = list_.replace(' ','').split(',')
		temlist.append('0')
		tempstr = ','.join(temlist)
		ng_tmp = ng_tmp + type_+"("+tempstr+')'+ngothers[nglist.index(list_)+1]
	return(ng_tmp)

print("%!PS-Adobe-3.0 EPSF-3.0")
print("%%BoundingBox: 0 0 1239 1752")
# print("test")
# #heta 0 0 1
# heta = picture('hexa',[0,0,1])
# print(heta.type)
# heta.draw()
# square_1 = picture('square',[0,0,1])
# square_2 = picture('ngon',[0,0,1,4])
# square_1.draw()
# square_2.draw()
# reader =[i.replace('(',' ').replace(')',' ').replace(',',' ').split() for i in sys.stdin.readlines()]
inputs = am_express_input(sys.stdin.read())
inputs.caculator()
input_no1 = insert_ng(inserfilled_ng(inputs.input))
input_no = input_no1
for type_ in ['filledtri','filledhexa','filledpenta','filledsquare']:
	input_no = jiaongxi(input_no,type_)
for type_ in ['tri','hexa','penta','square']:
	input_no = jiaongxi(input_no,type_)
transs = transformathions(input_no)
transs.trans()
input_no = transs.input
reader = re.findall('([a-z]*\s*?\(\s?.*?\s?\))',input_no,re.S)
# print(reader)
for element in reader:
	# print(element)
	line = element.replace(')',' ').replace('(',' ').replace(',',' ').split()
	type = line[0]
	# print(type)
	params_list = line[1:]
	# print('/n/n/n')
	pic = picture(type,params_list)
	pic.draw()


