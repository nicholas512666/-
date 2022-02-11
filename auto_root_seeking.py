#本程序使用python3.6语言，请用python3.6运行
#本程序当且仅当a=0,b=0且c=0时结束(当然也可手动结束)
while 0*0==0:
	print("ax²+bx+c=0")
	a=int(input("a=?"))
	b=int(input("b=?"))
	c=int(input("c=?"))
	while a*a+b*b+c*c>0:
		if a==0 and b!=0:
			x=-c/b
			print("x=",x)
			break
		elif a==0 and b==0:
			print ("式子有毛病啊")
			break
		elif b*b-4*a*c<0:
			print("无实根")
			break
		elif b*b-4*a*c==0:
			x=(-b/2*a)
			print("x1=x2=",x)
			break
		else:
			x1=((-b+(b*b-4*a*c)**0.5)/2*a)
			x2=((-b-(b*b-4*a*c)**0.5)/2*a)
			print("x1=",x1,",x2=",x2)
			break
	else:
		print("结束鸟")
		break
