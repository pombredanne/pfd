#!/usr/bin/env python

# -------
# imports
# -------

import sys
import heapq


matrix = []
size = [0]
visited = []
dependencies_list = []
target = -1
targets = []


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
	global dependencies_list
	dependencies_list = [0]*size[0]
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

		dependencies_list[row_index-1]= num_dependencies

		for  n in xrange(2,len(l)):
			matrix[row_index-1][int(l[n])-1] = 1
	return True

def pfd_clear(n):
	global matrix
	r = []
	for i in xrange(size[0]):
		if matrix[i][n] == 1:
			matrix[i][n] = 0
			r.append(i)
	return r

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

def pfd_printd () :
	global dependencies_list
	for i in dependencies_list:
		print i,

def pfd_print () :
	global matrix
	temp = ""
	for i in xrange(size[0]):
		for  n in xrange(len(matrix[i])):
			temp += str(matrix[i][n]) + " "
		temp += "\n"
	print temp

def pfd_find_first_target():
	global dependencies_list
	global targets
	lala = len(dependencies_list)
	for i in xrange(lala):
		if dependencies_list[i] == 0:
			heapq.heappush(targets, i)

# -------------
# collatz_solve
# -------------

def pfd_solve (r, w) :
	global targets
	a = [0, 0]
	pfd_initialize(r, a)
	targets_array = []
	pfd_find_first_target()
	#pfd_printd()
	
	#print "First Targets..."
	#print targets
	
	result = ""
	counter = 0
	
	temp_array = []
	resultArr = []

	while len(targets) > 0:

		target = heapq.heappop(targets)
		#print "Printing heap after taking off an element..."
		#print targets
		#print target+1,
		resultArr.append(target+1)

		new_targets = pfd_clear(target)
		#print new_targets
		for i  in new_targets:
			dependencies_list[i]-=1
			if dependencies_list[i] == 0:
				heapq.heappush(targets,i)
				
	#print "Restul", resultArr
	for i in xrange(len(resultArr)) :
	  print resultArr[i],





	#global visited
	#pfd_printd ()
	#while counter < size[0]:
		#no_dependencies = pfd_find_target()
		#print "No Dependency: ", no_dependencies
		#pfd_clear(no_dependencies)
		#visited[no_dependencies]= 1
		#result +=  str(no_dependencies+1)
		#counter += 1
		#if counter <size[0]:
		#	result += " "
		#pfd_print()
	#w.write(result + "\n")

	#pfd_print()
    	
def getMatrix():
	return matrix
pfd_solve(sys.stdin, sys.stdout)