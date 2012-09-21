#!/usr/bin/env python

# -------
# imports
# -------

import sys

matrix = []
size = [0]
visited = []
# ------------
# pfd_read
# ------------

def pfd_initialize (r, a) :
	"""
	reads two ints into a[0] and a[1]
	r is a  reader
	a is an array of int
	return true if that succeeds, false otherwise
	"""
	s = r.readline()
	if s == "" :
		return False
	l = s.split()
	if len(l) > 2:
		return False
	a[0] = int(l[0])
	a[1] = int(l[1])
	assert a[0] > 0
	assert a[1] > 0
	size[0] = a[0]
	#print "Size...", size
	global matrix
	matrix = []*size[0]
	global visited
	visited = [0]*size[0]
	for i in xrange(a[0]):
		matrix.append([0]*a[0])

	for i in xrange(a[1]):
		s = r.readline()

		l = s.split()

		row_index = int(l[0])

		num_dependencies = int(l[1])

		for  n in xrange(2,len(l)):
			matrix[row_index-1][int(l[n])-1] = 1
	return True

def pfd_clear(n):
	global matrix
	for i in xrange(size[0]):
		if matrix[i][n] == 1:
			matrix[i][n] = 0

def pfd_find_target() :
	target = -1
	global matrix
	for i in xrange(size[0]):
		
		found = False
		for n in xrange(size[0]):
			
			if matrix[i][n] == 1:
				found = True
		if not found and visited[i] == 0:
			target = i
			return target

	return target



def pfd_print () :
	global matrix
	temp = ""
	for i in xrange(size[0]):
		for  n in xrange(len(matrix[i])):
			temp += str(matrix[i][n]) + " "
		temp += "\n"
	print temp

# -------------
# collatz_solve
# -------------

def pfd_solve (r, w) :

	a = [0, 0]
	pfd_initialize(r, a)
	result = ""
	counter = 0
	global visited

	while counter < size[0]:
		no_dependencies = pfd_find_target()
		#print "No Dependency: ", no_dependencies
		pfd_clear(no_dependencies)
		visited[no_dependencies]= 1
		result +=  str(no_dependencies+1) + " "
		counter += 1
		#pfd_print()
	print(result)
	#pfd_print()
    	
# ----
# main
# ----

pfd_solve(sys.stdin, sys.stdout)