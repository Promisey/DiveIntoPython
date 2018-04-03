# -*- coding:utf-8 -*-
def fib(n):
	'''计算一个数的阶乘并返回结果。'''
	print 'n=', n
	if n > 1:
		return n*fib(n-1)
	else:
		print "end of the line"
		return 1

n = input ("input: ")
print(fib(n))