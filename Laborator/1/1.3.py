#!/usr/bin/python

def prod_matr(a, b):
	prod = list()
	
	for line_iter in range(len(a)):
		prod_line = list()
		
		for column_iter in range(len(b[0])):
			sum = 0
			for el_iter in range(len(b)):
				sum += a[line_iter][el_iter] * b[el_iter][column_iter]
		
			prod_line.append(sum)
		prod.append(prod_line)

	return prod	

a = [[1, 2, 3, 4], [11, 12, 13, 14], [21, 22, 23, 24]]
b = [[2], [-5], [7], [-10]]

print(prod_matr(a, b))
