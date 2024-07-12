import array as ar
import numpy as np                      # allows vectorized ops (apply to whole array) and eliminates loops
# from numpy import *                   # import all --> functions can be called without prefix
import math


print(5)

# Filtering
x = np.r_[0:5:1]                        # = Matlab 0:1:4
idx = (x > 2) & (x < 4)                 # = [F F F T F] --> boolean indexing
x[x<3] = 9                              # = [9 9 9 3 4]
np.isnan(x)                             # = [F F ...]
np.isfinite(x)                          # = [T T ...]
np.sum(x>3)

x = np.r_[0:5:1]                        # re init
y = np.r_[6:3:-1]                       # [6, 5, 4]

np.in1d(x, y)                           # element of x is in y? --> only 4 is there, so [F,F,F,F,T]
np.argmin(x < 10)                       # first index of the min value that satisfies condition
np.histogram(x)                         # 2 arrays: occurences and bins, default n = 10


# dimensions = axes --> rank of an array = # of axes

##### 1) Regular Arrays
ar1 = ar.array('i', [1, 3, 4])          # signed integers, default is float64
ar2 = ar.array('i', [])
ar3 = np.arange(2, 10, dtype = np.float)    # arrange = from [2 to 10)

print (ar1.typecode)                    # returns array type --> i (int)
print(ar1.itemsize)                     # size in bytes --> 1 byte
print(ar1.buffer_info())                # returns array memory address
print(ar1.count(3))                     # returns the # of occurrences in an array --> 1
print(ar1[1])                           # = [1] -> 3
print(ar1[1:3])                         # = [1,3) --> [3, 4]

list1 = [1, 2, 3]
ar2.fromlist(list1)                     # appends a list: [] + [1, 2, 3]
print(ar2)
ar2.extend(ar2)                         # appends an array: [1, 2, 3, 1, 2, 3]
print(ar1.tolist())                     # cast (convert) to list

sum(ar1, 1)                             # (1 + 3 + 4) + 1 = 9
# ar1 + 1                               # can only append an array, not int --> NumPy wins


##### 2) Numpy Arrays
## 2a) Array access
np1 = np.array([1, 3, 4],  int)         # array defininition
np.array([1, 2.0, 3])                   # all float if at least 1 element is

np.ones((1, 5))
np.zeros((2, 4))
np.ones([2, 3, 4])                      # depth, rows, cols
np2 = np.array([],  int)                # empty arrays
np2 = 2*np.ones(3, int)                 # fill it with [2, 2, 2]

list(np.arange(0,1, 0.1))               # linspace like, returns array so cast it to list

print(np1[0:2])                         # [0, 2) --> 1, 3
np1.clip(2, 3)                          # clip magnitudes between min max (voltage rails)

npc = np1.copy()                        # copy and ..
npc.fill(3)                             # fill with a scalar
npc

np1.view(float)                         # view with a custom data type
np1.dtype                               # data type = int --> int64
np1.astype('int').astype('str')         # convert data type from int to string
np.array([1,0,5, 0], dtype='bool')      # casts the array type during creation --> T F T F

np1.tolist()                            # converts to list


## 2b)Array ops
np1*np2                                 # element wise multiply [2, 6, 8]
np1/np2                                 # auto converted to decimal

np1.max()                               # max value
np1.argmax()                            # index of //

np.array([1+1j, 1-2j]).conj()           # complex conj --> 1-1j, 1+2j
np1.cumsum()                            # cumulative sum --> 1, 1+3, 1+3+4 = 1, 4, 8
np1.cumprod()                           # // product --> 1, 1*3, 1*3*4 = 1, 3, 12

np.random.random()                      # random(): [0 1], single number
np.random.rand(3,3)                     # rand(): [0 1], matrix
np.random.randn(3,3)                    # randn(): mean=0, var=1, matrix

np3 = np.array([1, 2, 1, 2, 3])         # unique elements
uniq, count = np.unique(np3, return_counts=True)
uniq                                    # = [1 2 3]
count                                   # = [2 2 1]


## 2c) Array merge
np.concatenate((np1, np2))              # need to pass arrays as a sequence (extra parentheses)
np.array([1, 'a', 2], dtype='object')   # object type allows multiple data types in an array


##### 3) NP matrix
## 3a) Matrix access
mtx1 = np.matrix('1 2 3; 4 5 6', int)
mtx1.itemsize                           # size in bytes = 8
mtx1.nbytes                             # total bytes = elements * itemsize = 6*8 = 48
mtx1.diagonal(0)                        # 1st diagonal = [1, 5], 2nd diagonal = [2, 6]

np.size(mtx1)                           # get total element #
len(mtx1[:, 1])                         # get rows # ( = len(mtx1) ) --> 2
len(mtx1[1, :])                         # get cols # --> 3
mtx1.ndim                               # array dimension --> 2
r, c = mtx1.shape                       # r = 2, c = 3
np.shape(mtx1)                          # get the shape (rows, cols)
np.reshape(mtx1, 6)                     # reinserts the elements in a new shape
np.reshape(mtx1, (3,2))                 # != mtx1.T
mtx1.ravel()                            # flattens the matrix = reshape(1,6) --> (1, 2, ..6)
mtx1[1, 1]                              # direct access --> = 5
mtx1[:, 1]                              # = [2, 5]' (returns as a vertical col)
mtx1[:, 1]

## 3b) Matrix merge
np.vstack((mtx1, mtx1))                 # vertical append of arrays/matrices (also hstack)
lst1 = [[1,2,3], [4,5,6], [7,8,9]]      # given a list
np.array((lst1))                        # same if np.matrix


## 3c) Matrix ops
mtx1 + 1                                # adds 1 to each element
mtx1 / mtx1                             # element wise op for +,-,/ --> 1s
mtx1.T                                  # transpose (complex conjugate transpose = mtx1.H)
mtx1.transpose()                        # takes axis as an arg.
mtx1.swapaxes(0, 1)	                    # = transpose
mtx1.A                                  # cast into ndarray object
mtx1.I                                  # multiplicative inverse (if invertible)
mtx1 * mtx1.T                           # matrix mult: (2,3)*(3,2) = (2,2) in size
np.dot(mtx1, 1)                         # dot mult, same result = [[14, 32], [32, 77]]
mtx1.sum(0)                             # vertically --> [(1+4), (2+5), (3+6)] = [5, 7 ,9]
mtx1.prod(0)                            # vertically --> [(1*4), (2*5), (3*6)] = [4, 10 ,18]
np.array([5.12345, 6.12345]).round(3)	# accepts the number of decimal digits to round at --> [5.123, 6.123]

mtx1.nonzero()	                        # indices of nz elements --> [0, 0, 0, 1, 1, 1], [0, 1, 2, 0, 1, 2] (all pairs)
mtx1.ptp(1)
mtx1.max()                              # overall max
mtx1.max(0)                             # axis=0=rows --> return the max (of each col) --> 4, 5, 6
mtx1.max(1)                             # axis=1=cols --> return the max (of each row) --> 3; 6
mtx1.ptp(0)	                            # vertically --> among [(4-1), (5-2), (6-3)] = [[3, 3, 3]] (array)
mtx1.ptp(1)	                            # horizontally --> among [(3-1), (6-4)] = [[2],[2]] (matrix)
np.mean(mtx1)                           # avg of all elements --> 3.5 (can do min/max too)
mtx1.mean()                             # same result
mtx1.var()                              # variance --> 2.916, [axis, dtype, out, ddof])
mtx1.var(0)	                            # variance --> [[2.25, 2.25, 2.25]]
mtx1.std()                              # return the std_dev
mtx1.trace(1, 0)                        # sum along the diagonals --> 2 + 6 = 8, [offset, axis1, axis2, dtype, out]
np.sort(mtx1, axis = None)              # no axis --> flattened --> 1, 2, 3, 4, 5, 6
np.sort(-mtx1, axis = 0)                # vertically --> -4 < -1, -5 < -2, -6 < -3

# tofile(fid[, sep, format])	        # write array to a file as text or binary (default).
# tostring([order])	                    # construct python bytes containing the raw data bytes in the array.W
mtx1.tostring()

mtx1[: : -1, :]                         # reverse the rows --> = mtx1[: : -1, ]  (can omit the final : )
mtx1[:,  : : -1]                        # reverse the cols
mtx1[: : -1,  : : -1]                   # reverse both

