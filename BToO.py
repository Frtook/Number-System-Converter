def BO(b):
	try:
		N=''
		f=[]
		n=''
		b=list(b)
		if '.' in b:
			b.reverse()
			for i in b[::]:
				if i =='.':
					b.remove(i)
					break
				f.append(i)
				b.remove(i)
			b.reverse()
			f.reverse()
		r=0
		while len(b)>=r:
			r+=3
		while r-len(b):
			b.insert(0,'0')
		B=[]
		i=0
		while i<len(b):
			B.append(b[i]+b[i+1]+b[i+2])
			i+=3
		for i in B:
			if i =='000':
				n+='0'
			elif i =='001':
				n+='1'
			elif i =='010':
				n+='2'
			elif i =='011':
				n+='3'
			elif i =='100':
				n+='4'
			elif i =='101':
				n+='5'
			elif i =='110':
				n+='6'
			elif i =='111':
				n+='7'
			else:
				print('Error 1')
		try:
			if f == True:
				raise Exception()
			N+=n
			r=0
			n=''
			while len(f)>=r:
				r+=3
			while r-len(f):
				f.append('0')
			B=[]
			i=0
			while i<len(f):
				B.append(f[i]+f[i+1]+f[i+2])
				i+=3
			for i in B:
				if i =='000':
					n+='0'
				elif i =='001':
					n+='1'
				elif i =='010':
					n+='2'
				elif i =='011':
					n+='3'
				elif i =='100':
					n+='4'
				elif i =='101':
					n+='5'
				elif i =='110':
					n+='6'
				elif i =='111':
					n+='7'
				else:
					print('Error 2 ')
			N+='.'+n
		except:
			print('Error 1')
	except:
		print('Error 2')
	return N