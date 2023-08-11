def HB(n):
	try:
		B=''
		l=n.lower().split('.')
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
				b+='0001'
			elif i ==2:
				b+='0010'
			elif i ==3:
				b+='0011'
			elif i ==4:
				b+='0100'
			elif i==5:
				b+='0101'
			elif i ==6:
				b+='0110'
			elif i ==7:
				b+='0111'
			elif i ==8:
				b+='1000'
			elif i ==9:
				b+='1001'
			elif i==10 or i == 'a':
				b+='1010'
			elif i ==11 or i== 'b':
				b+='1011'
			elif i ==12 or  i== 'c':
				b+='1100'
			elif i ==13 or i== 'd':
				b+='1101'
			elif i ==14 or i== 'e':
				b+='1110'
			elif i == 15 or i== 'f':
				b+='1111'
			elif i ==0 :
				b+='0000'
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
					b+='0001'
				elif i ==2:
					b+='0010'
				elif i ==3:
					b+='0011'
				elif i ==4:
					b+='0100'
				elif i==5:
					b+='0101'
				elif i ==6:
					b+='0110'
				elif i ==7:
					b+='0111'
				elif i ==8:
					b+='1000'
				elif i ==9:
					b+='1001'
				elif i==10 or i == 'a':
					b+='1010'
				elif i ==11 or i== 'b':
					b+='1011'
				elif i ==12 or  i== 'c':
					b+='1100'
				elif i ==13 or i== 'd':
					b+='1101'
				elif i ==14 or i== 'e':
					b+='1110'
				elif i == 15 or i== 'f':
					b+='1111'
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

