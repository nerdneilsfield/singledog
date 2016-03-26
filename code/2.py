import re

def insert_ng(input_str):
	input_str = re.sub(r'\s*','',input_str)
	nglist= re.findall(r'ngon\s*?\(([0-9\,\s]+?)\)',input_str,re.S)
	ngothers = re.split(r'ngon\s*?\([0-9\,\s]+?\)',input_str,re.S )
	ng_tmp = ngothers[0]
	for list_ in nglist:
		temlist = list_.replace(' ','').split(',')
		temlist.insert(3,'0')
		tempstr = ','.join(temlist)
		ng_tmp = ng_tmp + "ngon("+tempstr+')'+ngothers[nglist.index(list_)+1]
	return(ng_tmp)
def inserfilled_ng(input_str):
	input_str = re.sub(r'\s*','',input_str)
	nglist= re.findall(r'filledngon\s*?\(([0-9\,\s]+?)\)',input_str,re.S)
	ngothers = re.split(r'filledngon\s*?\([0-9\,\s]+?\)',input_str,re.S )
	ng_tmp = ngothers[0]
	for list_ in nglist:
		temlist = list_.replace(' ','').split(',')
		temlist.insert(3,'0')
		tempstr = ','.join(temlist)
		ng_tmp = ng_tmp + "filledngon("+tempstr+')'+ngothers[nglist.index(list_)+1]
	return(ng_tmp)
def jiaongxi(input_str,type_):
	input_str = re.sub(r'\s*','',input_str)
	nglist= re.findall(r'%s\s*?\(([0-9\,\s]+?)\)'%type_,input_str,re.S)
	ngothers = re.split(r'%s\s*?\([0-9\,\s]+?\)'%type_,input_str,re.S )
	ng_tmp = ngothers[0]
	for list_ in nglist:
		temlist = list_.replace(' ','').split(',')
		temlist.append('0')
		tempstr = ','.join(temlist)
		ng_tmp = ng_tmp + type_+"("+tempstr+')'+ngothers[nglist.index(list_)+1]
	return(ng_tmp)

test_case = "line(1,2,3,4)"
print(insert_ng(test_case))