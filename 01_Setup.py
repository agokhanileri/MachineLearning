import math
import os
import sys

# -----------------------------------
# SETUP: (from Terminal)
# conda update conda            # --> conda update -n base -c defaults conda
# conda update spyder           #
# conda update ipython          #
# conda install -c anaconda python=3.10  #
# conda update --all            # to fix dependencies
# conda create -n python38 python=3.8 --> better way is to create new env (can use at other proj)
# conda activate python38       # activate
# python                        # start
# quit()                        # quit

# Libs setup: numpy, scipy, pandas, sympy, pylab, pytest


# -----------------------------------
# TEST:
def test_python():
    major = sys.version_info.major
    minor = sys.version_info.minor
    if major == 3:
        pass
    else:        # assert major == 3, "Stopping here - we need Python 3."
        print("You are running Python {}, but we need Python {}.".format(major, 3))
        print("Download and install the Anaconda distribution for Python 3.")
        sys.exit(1)
    if minor >= 7:
        print("Testing Python version-> py{}.{} OK".format(major, minor))
    else:
        print("Warning: You should be running Python 3.7 or newer, " +
              "you have Python {}.{}.".format(major, minor))

def test_numpy():
    try:
        import numpy as np
    except ImportError:
        print("Could not import numpy -> numpy failed")
        return None
    # Simple test
    a = np.arange(0, 100, 1)
    assert np.sum(a) == sum(a)
    print("Testing numpy...      -> numpy OK")

def test_scipy():
    try:
        import scipy
    except ImportError:
        print("Could not import 'scipy' -> scipy failed")
        return None
    # Simple test
    import scipy.integrate
    assert abs(scipy.integrate.quad(lambda x: x * x, 0, 6)[0] - 72.0) < 1e-6
    print("Testing scipy...      -> scipy OK")

def test_pandas():
    try:
        import pandas as pd
    except ImportError:
        print("Could not import pandas -> pandas failed")
        return None
    a = pd.Series(range(10))         # Series test
    assert a.size == 10
    b = pd.DataFrame()              # DF test
    b['day'] = ['Mon', 'Tue', 'Wed']
    assert b.shape == (3, 1)
    print("Testing pandas...     -> pandas OK")

def test_pylab():       # test matplotlib
    try:
        import pylab
    except ImportError:
        print("Could not import 'matplotlib/pylab' -> failed")
        return None

    xvalues = [i * 0.1 for i in range(100)]
    yvalues = [math.sin(x) for x in xvalues]
    pylab.plot(xvalues, yvalues, "-o", label="sin(x)")
    pylab.legend()
    pylab.xlabel('x')
    testfilename = 'pylab-testfigure.png'

    if os.path.exists(testfilename):            # check if the file exists already
        print("Skipping plotting to file as file {} exists already.".format(testfilename))
    else:                                       # write plot to file
        pylab.savefig(testfilename)
        assert os.path.exists(testfilename)     # check if it exists now
        print("Testing matplotlib... -> pylab OK")
        os.remove(testfilename)

def test_sympy():
    try:
        import sympy
    except ImportError:
        print("Could not import 'sympy' -> fail")
        return None

    x = sympy.Symbol('x')
    my_f = x ** 2
    assert sympy.diff(my_f, x) == 2 * x
    print("Testing sympy...      -> sympy OK")

def test_pytest():
    try:
        import pytest
    except ImportError:
        print("Could not import 'pytest' -> fail")
        return None
    print("Testing pytest...     -> pytest OK")

if __name__ == "__main__":
    print("Running using Python {}".format(sys.version))
    test_python(); test_numpy(); test_scipy();  test_pandas()
    test_pylab(); test_sympy(); test_pytest()
