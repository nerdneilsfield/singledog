import re

test_case = "penta(2,\
\
\
	\
3,4)\
tri(1,\
2,	3)\
tri(2,3,4)line(7,8,9,10)\
ngon(2,3,4,5)hexa(1,2,3)penta(1,2,3)\
line(1,2,3,4)ngon(1,2,3)penta(7,8,9)hexa(7,8,9)"

test_case2 = "hexa(1,2,3,4)hexa(1,2,3,4)"
def changgetongon(input_str):
	input_str = re.sub(r'\s*','',input_str)
	nglist= re.findall(r'ngon\s*?\(([0-9\,\s]+?)\)',input_str,re.S)
	ngothers = re.split(r'ngon\s*?\([0-9\,\s]+?\)',input_str,re.S )
	ng_tmp = ngothers[0]
	for list_ in nglist:
		temlist = list_.replace(' ','').split(',')
		temlist.append('0')
		tempstr = ','.join(temlist)
		ng_tmp = ng_tmp + "ngon("+tempstr+')'+ngothers[nglist.index(list_)+1]
	print(ng_tmp)
	trilist= re.findall(r'tri\s*?\(([0-9\,\s]+?)\)',ng_tmp,re.S)
	triothers = re.split(r'tri\s*?\([0-9\,\s]+?\)',ng_tmp,re.S )
	temp = triothers[0]
	for list_ in trilist:
		temlist = list_.replace(' ','').split(',')
		temlist.append('3')
		temlist.append('0')
		tempstr = ','.join(temlist)
		temp = temp + "ngon("+tempstr+')'+triothers[trilist.index(list_)+1]
	print(temp)
	sqlist= re.findall(r'square\s*?\(([0-9\,\s]+?)\)',temp,re.S )
	sqothers = re.split(r'square\s*?\([0-9\,\s]+?\)',temp,re.S )
	# print(sqlist)
	# print(sqothers)
	temp_sq = sqothers[0]
	for list_ in sqlist:
		temlist = list_.replace(' ','').split(',')
		temlist.append('4')
		temlist.append('0')
		tempstr = ','.join(temlist)
		temp_sq = temp_sq + "ngon("+tempstr+')'+sqothers[sqlist.index(list_)+1]
	print(temp_sq)
	hxlist= re.findall(r'hexa\s*?\(([0-9\,\s]+?)\)',temp_sq,re.S )
	hxothers = re.split(r'hexa\s*?\([0-9\,\s]+?\)',temp_sq,re.S )
	# print(hxlist)
	# print(hxothers)
	temp_hx = hxothers[0]
	for list_ in hxlist:
		temlist = list_.replace(' ','').split(',')
		temlist.append('6')
		temlist.append('0')
		tempstr = ','.join(temlist)
		temp_hx = temp_hx + "ngon("+tempstr+')'+hxothers[hxlist.index(list_)+1]
	print(temp_hx)
	ptlist= re.findall(r'penta\s*?\(([0-9\,\s]+?)\)',temp_hx,re.S )
	ptothers = re.split(r'penta\s*?\([0-9\,\s]+?\)',temp_hx,re.S )
	temp_pt = ptothers[0]
	for list_ in ptlist:
		temlist = list_.replace(' ','').split(',')
		temlist.append('5')
		temlist.append('0')
		tempstr = ','.join(temlist)
		temp_pt= temp_pt + "ngon("+tempstr+')'+ptothers[ptlist.index(list_)+1]
	return temp_pt


x = changgetongon(test_case2)
print(x)