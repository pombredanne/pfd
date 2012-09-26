#!/usr/bin/env python

"""
To test the program:
    % python TestPFD.py >& TestPFD.py.out
    % chmod ugo+x TestPFD.py
    % TestPFD.py >& TestPFD.py.out
"""

# -------
# imports
# -------

import StringIO
import unittest

from PFD import pfd_initialize, pfd_solve, pfd_clear, pfd_find_first_target, getMatrix

# -----------
# TestCollatz
# -----------

class TestPFD (unittest.TestCase) :
    # ----
    # read
    # ----

    def test_initialize_1 (self) :
        r = StringIO.StringIO("2 1\n2 1 1")
        a = [0, 0]
        c = [0]
        b = pfd_initialize(r, a, c)
        matrix = getMatrix()
        self.assert_(b    == True)
        self.assert_(a[0] ==  2)
        self.assert_(a[1] ==  1)
        self.assert_(matrix == [[0, 0],[1, 0]] )

    def test_initialize_2 (self) :
        r = StringIO.StringIO("5 4\n3 2 1 5\n2 2 5 3\n4 1 3\n5 1 1")
        a = [0, 0]
        c = [0]
        b = pfd_initialize(r, a, c)
        matrix = getMatrix()
        self.assert_(b    == True)
        self.assert_(a[0] ==  5)
        self.assert_(a[1] ==  4)
        self.assert_(matrix == [[0, 0, 0, 0, 0],
                                [0, 0, 1, 0, 1],
                                [1, 0, 0, 0, 1],
                                [0, 0, 1, 0, 0],
                                [1, 0, 0, 0, 0]] )

    def test_initialize_3 (self) :
        r = StringIO.StringIO("2 1\n2 1 1")
        a = [0, 0]
        c = [0]
        b = pfd_initialize(r, a, c)
        matrix = getMatrix()
        self.assert_(b    == True)
        self.assert_(a[0] ==  2)
        self.assert_(a[1] ==  1)
        self.assert_(matrix == [[0, 0],[1, 0]] )

    # -----
    # clear
    # -----

    def test_clear_1 (self) :
        r = StringIO.StringIO("5 4\n3 2 1 5\n2 2 5 3\n4 1 3\n5 1 1")
        a = [0, 0]
        c = [0]
        b = pfd_initialize(r, a, c)
        matrix = getMatrix()
        self.assert_(b    == True)
        self.assert_(a[0] ==  5)
        self.assert_(a[1] ==  4)
        self.assert_(matrix == [[0, 0, 0, 0, 0],
                                [0, 0, 1, 0, 1],
                                [1, 0, 0, 0, 1],
                                [0, 0, 1, 0, 0],
                                [1, 0, 0, 0, 0]] )
        pfd_clear(0)
        matrix = getMatrix()
        self.assert_(matrix == [[0, 0, 0, 0, 0],
                                [0, 0, 1, 0, 1],
                                [0, 0, 0, 0, 1],
                                [0, 0, 1, 0, 0],
                                [0, 0, 0, 0, 0]] )

    def test_clear_2 (self) :
        r = StringIO.StringIO("2 1\n1 1 2")
        a = [0, 0]
        c = [0]
        b = pfd_initialize(r, a, c)
        matrix = getMatrix()
        self.assert_(b    == True)
        self.assert_(a[0] ==  2)
        self.assert_(a[1] ==  1)
        self.assert_(matrix == [[0, 1],[0, 0]] )
        pfd_clear(1)
        matrix = getMatrix()
        self.assert_(matrix == [[0, 0],[0, 0]] )

    def test_clear_3 (self) :
        r = StringIO.StringIO("5 4\n3 2 1 5\n2 2 5 3\n4 1 3\n5 1 1")
        a = [0, 0]
        c = [0]
        b = pfd_initialize(r, a, c)
        matrix = getMatrix()
        self.assert_(b    == True)
        self.assert_(a[0] ==  5)
        self.assert_(a[1] ==  4)
        self.assert_(matrix == [[0, 0, 0, 0, 0],
                                [0, 0, 1, 0, 1],
                                [1, 0, 0, 0, 1],
                                [0, 0, 1, 0, 0],
                                [1, 0, 0, 0, 0]])
        pfd_clear(0)
        matrix = getMatrix()
        self.assert_(matrix == [[0, 0, 0, 0, 0],
                                [0, 0, 1, 0, 1],
                                [0, 0, 0, 0, 1],
                                [0, 0, 1, 0, 0],
                                [0, 0, 0, 0, 0]] )
        pfd_clear(4)
        matrix = getMatrix()
        self.assert_(matrix == [[0, 0, 0, 0, 0],
                                [0, 0, 1, 0, 0],
                                [0, 0, 0, 0, 0],
                                [0, 0, 1, 0, 0],
                                [0, 0, 0, 0, 0]] )
        pfd_clear(2)
        matrix = getMatrix()
        self.assert_(matrix == [[0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0]] )



    # -----------
    # find_target
    # -----------

    def test_find_first_target_1 (self) :
        r = StringIO.StringIO("2 1\n2 1 1")
        a = [0, 0]
        c = [0]
        b = pfd_initialize(r, a, c)
        matrix = getMatrix()
        pfd_find_first_target()


    def test_find_first_target_2  (self) :        
        r = StringIO.StringIO("5 4\n3 2 1 5\n2 2 5 3\n4 1 3\n5 1 1")
        a = [0, 0]
        c = [0]
        b = pfd_initialize(r, a, c)
        matrix = getMatrix()
        pfd_find_first_target()


    def test_find_first_target_3 (self) :
        r = StringIO.StringIO("2 1\n2 1 1")
        a = [0, 0]
        c = [0]
        b = pfd_initialize(r, a, c)
        matrix = getMatrix()
        pfd_find_first_target()
    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = StringIO.StringIO("5 4\n3 2 1 5\n2 2 5 3\n4 1 3\n5 1 1\n")
        w = StringIO.StringIO()
        pfd_solve(r, w)
        self.assert_(w.getvalue() == "1 5 3 2 4\n\n" )

    def test_solve_2 (self) :
        r = StringIO.StringIO("2 1\n2 1 1")
        w = StringIO.StringIO()
        pfd_solve(r, w)
        self.assert_(w.getvalue() == "1 2\n\n" )

    def test_solve_3 (self) :
        r = StringIO.StringIO("18 14\n 3 1 18\n7 1 2\n10 1 7\n12 1 18\n6 2 3 5\n13 2 2 7\n4 1 12\n15 4 2 3 6 13\n9 3 2 7 15\n11 3 18 7 4\n17 4 6 13 4 9\n1 3 10 8 12\n16 6 2 7 8 5 4 11\n14 3 13 4 1\n")
        w = StringIO.StringIO()
        pfd_solve(r, w)
        self.assert_(w.getvalue() == "2 5 7 8 10 13 18 3 6 12 1 4 11 14 15 9 16 17\n\n" )


# ----
# main
# ----

print "TestPFD.py"
unittest.main()
print "Done."
