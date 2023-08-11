#n=input()
#b=''
#for i in n:
#	i=int(i)
#	if i==1:
#		b+='001'
#	elif i ==2:
#		b+='010'
#	elif i ==3:
#		b+='011'
#	elif i ==4:
#		b+='100'
#	elif i==5:
#		b+='101'
#	elif i ==6:
#		b+='110'
#	elif i ==7:
#		b+='111'
#	elif i ==0 :
#		b+='000'
#	else:
#		b=''
#		print('Error')
#		break
#print(b)
def OB(n):
	try:
		B=''
		l=n.split('.')
		n1=l[0]
		if len(l)>1:	
			n2=l[1]
		b=''
		for i in n1:
			try:
				i=int(i)
			except :
				pass
			if i==1:
				b+='001'
			elif i ==2:
				b+='010'
			elif i ==3:
				b+='011'
			elif i ==4:
				b+='100'
			elif i==5:
				b+='101'
			elif i ==6:
				b+='110'
			elif i ==7:
				b+='111'
			elif i ==0 :
				b+='000'
			else:
				b=''
				print('Error')
				break
		B+=b
		b=''
		if len(l)>1:
			B+='.'
			for i in n2: #float
				try:
					i=int(i)
				except :
					pass
				if i==1:
					b+='001'
				elif i ==2:
					b+='010'
				elif i ==3:
					b+='011'
				elif i ==4:
					b+='100'
				elif i==5:
					b+='101'
				elif i ==6:
					b+='110'
				elif i ==7:
					b+='111'
				elif i ==0 :
					b+='000'
				else:
					B=''
					print('Error')
					break
		B+=b
		return B
	except:
		print('Error')
# print(OB('44'))