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

from PFD import pfd_initialize, pfd_solve, pfd_clear, pfd_find_target, getMatrix

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
        b = pfd_initialize(r, a)
        matrix = getMatrix()
        self.assert_(b    == True)
        self.assert_(a[0] ==  2)
        self.assert_(a[1] ==  1)
        self.assert_(matrix == [[0, 0],[1, 0]] )

    def test_initialize_2 (self) :
        r = StringIO.StringIO("5 4\n3 2 1 5\n2 2 5 3\n4 1 3\n5 1 1")
        a = [0, 0]
        b = pfd_initialize(r, a)
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
        b = pfd_initialize(r, a)
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
        b = pfd_initialize(r, a)
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
        b = pfd_initialize(r, a)
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
        b = pfd_initialize(r, a)
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


    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = StringIO.StringIO("5 4\n3 2 1 5\n2 2 5 3\n4 1 3\n5 1 1")
        w = StringIO.StringIO()
        pfd_solve(r, w)
        self.assert_(w.getvalue() == "1 5 3 2 4\n" )


    def test_solve_2 (self) :
        r = StringIO.StringIO("2 1\n2 1 1")
        w = StringIO.StringIO()
        pfd_solve(r, w)
        self.assert_(w.getvalue() == "1 2\n" )

    def test_solve_3 (self) :
        dasd

    # -----------
    # find_target
    # -----------

    def find_target_1 (self) :
        lala

    def find_target_2 (self) :
        lala

    def find_target_3 (self) :
        lala

# ----
# main
# ----

print "TestPFD.py"
unittest.main()
print "Done."
