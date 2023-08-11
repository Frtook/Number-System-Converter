def BH(b):
	re='\033[91m'
	wh='\033[m'
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
			r+=4
		while r-len(b):
			b.insert(0,'0')
		B=[]
		i=0
		while i<len(b):
			B.append(b[i]+b[i+1]+b[i+2]+b[i+3])
			i+=4
		for i in B:
			if i =='0000':
				n+='0'
			elif i =='0001':
				n+='1'
			elif i =='0010':
				n+='2'
			elif i =='0011':
				n+='3'
			elif i =='0100':
				n+='4'
			elif i =='0101':
				n+='5'
			elif i =='0110':
				n+='6'
			elif i =='0111':
				n+='7'
			elif i =='1000':
				n+='8'
			elif i =='1001':
				n+='9'
			elif i =='1010':
				n+='A'
			elif i =='1011':
				n+='B'
			elif i =='1100':
				n+='C'
			elif i =='1101':
				n+='D'
			elif i =='1110':
				n+='E'
			elif i =='1111':
				n+='F'
			else:
				print(f'{re}Value Error Enter 0 ot 1 !!{wh}')
				raise Exception('Value Error !!')
		try:
			N+=n
			r=0
			n=''
			while len(f)>=r:
				r+=4
			while r-len(f):
				f.append('0')
			B=[]
			i=0
			while i<len(f):
				B.append(f[i]+f[i+1]+f[i+2]+f[i+3])
				i+=4
			for i in B:
				if i =='0000':
					n+='0'
				elif i =='0001':
					n+='1'
				elif i =='0010':
					n+='2'
				elif i =='0011':
					n+='3'
				elif i =='0100':
					n+='4'
				elif i =='0101':
					n+='5'
				elif i =='0110':
					n+='6'
				elif i =='0111':
					n+='7'
				elif i =='1000':
					n+='8'
				elif i =='1001':
					n+='9'
				elif i =='1010':
					n+='A'
				elif i =='1011':
					n+='B'
				elif i =='1100':
					n+='C'
				elif i =='1101':
					n+='D'
				elif i =='1110':
					n+='E'
				elif i =='1111':
					n+='F'
				else:
					print(f'{re}Value Error Enter 0 or 1 !!{wh}')
					raise Exception('Value Error')
			N+='.'+n
		except Exception as e:
			N=""
			return N
			print(e)
	except Exception as e:
		N=''
		return N
		print(e)
	return N