#!/usr/bin/env python

# -------
# imports
# -------

import sys
import heapq


matrix = []
size = [0]
dependencies_list = []
target = -1
targets = []


# ------------
# pfd_initialize
# ------------

def pfd_initialize (r, a, b) :
	"""
	reads two ints into a[0] and a[1]
	r is a  reader
	a is an array of int
	return true if that succeeds, false otherwise
	"""
	s = r.readline()
	if s == "\n" :
		s = r.readline()
		if s == "" :
			return False
	if s == "" :
		return False
	l = s.split()
	if len(l) > 2:
		return False
	a[0] = int(l[0])
	a[1] = int(l[1])
	assert a[0] > 0
	if(a[1]==0):
		b[0] = 0
		for i in xrange(a[0]):
			print i+1,
		print "\n"
		return True;
	size[0] = a[0]
	global matrix
	global dependencies_list
	dependencies_list = [0]*size[0]
	matrix = []*size[0]

	assert len(dependencies_list) > 0

	for i in xrange(a[0]):
		matrix.append([0]*a[0])

	assert len(matrix) > 0 		

	for i in xrange(a[1]):
		s = r.readline()
		l = s.split()

		row_index = int(l[0])
		num_dependencies = int(l[1])
		dependencies_list[row_index-1]= num_dependencies

		for  n in xrange(2,len(l)):
			matrix[row_index-1][int(l[n])-1] = 1
	b[0] = 1
	return True

# ------------
# pfd_clear
# ------------

def pfd_clear(n):
	"""
	n is the column to clear out
	return array of affected rows
	"""
	global matrix
	r = []
	for i in xrange(size[0]):
		if matrix[i][n] == 1:
			matrix[i][n] = 0
			r.append(i)
	return r


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


# ------------
# pfd_find_first_target
# ------------
def pfd_find_first_target():
	"""
	Fills array with all the zero-dependency
	"""
	global dependencies_list
	global targets
	num_dependencies = len(dependencies_list)
	for i in xrange(num_dependencies):
		if dependencies_list[i] == 0:
			heapq.heappush(targets, i)

# -------------
# pfd_solve
# -------------

def pfd_solve (r, w) :
	"""
	r is a reader
	w is a writer
	executes algorithm
	"""
	global targets
	targets = []

	a = [0, 0]
	b = [0]
	while pfd_initialize(r, a,b) :
		if b[0] == 1:
			#pfd_initialize(r, a)
			targets_array = []
			pfd_find_first_target()
			
			resultArr = []


			while len(targets) > 0:
				target = heapq.heappop(targets)
				resultArr.append(target+1)
				new_targets = pfd_clear(target)

				for i  in new_targets:
					dependencies_list[i]-=1
					if dependencies_list[i] == 0:
						heapq.heappush(targets,i)
						
			#Prints the result
			w_str = ""
			for i in xrange(len(resultArr)) :
				w_str += str(resultArr[i])
				if i != len(resultArr)-1:
					w_str +=" "
				#print resultArr[i],
			resultArr = []
			w.write(w_str + "\n\n")

# -------------
# getMatrix
# -------------   	
def getMatrix():
	"""
	method used for the unit test
	returns global matrix
	"""
	return matrix
def getTargets():
	"""
	method used for the unit test
	returns global matrix
	"""
	return targe