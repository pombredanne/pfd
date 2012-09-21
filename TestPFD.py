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
        r = StringIO.StringIO("1 999999\n")
        a = [0, 0]
        b = pfd_initialize(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  1)
        self.assert_(a[1] == 999999)

    def test_initialize_3 (self) :
        r = StringIO.StringIO("10 10\n")
        a = [0, 0]
        b = pfd_initialize(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  10)
        self.assert_(a[1] == 10)

    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2 (self) :
        r = StringIO.StringIO("100 200\n900 1000\n201 210\n1 10\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "100 200 125\n900 1000 174\n201 210 89\n1 10 20\n")

    def test_solve_3 (self) :
        r = StringIO.StringIO("900000 999999\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "900000 999999 507\n")
    def test_solve_4 (self) :
        r = StringIO.StringIO("139163 552953\n776468 628994\n378628 766439\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "139163 552953 470\n776468 628994 504\n378628 766439 509\n")

    def test_solve_5 (self) :
        r = StringIO.StringIO("9043 9820\n3546 2708\n2234 2573\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "9043 9820 260\n3546 2708 217\n2234 2573 209\n")

    # -----------
    # find_target
    # -----------

    def find_target_1 (self) :
        lala

    def find_target_2 (self) :
        lala

    def find_target_3 (self) :
        lala

    # -----
    # clear
    # -----

    def clear_1 (self) :
        lala

    def clear_2 (self) :
        lala

    def clear_3 (self) :
        lala

# ----
# main
# ----

print "TestPFD.py"
unittest.main()
print "Done."
