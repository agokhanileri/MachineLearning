import numpy as np        # no need since numpy functions are imported with scipy
import scipy as sp
import scipy.io as sio
# import Plot as plt  # fix this

### Basics
arr = np.ones((2, 3))       #
arr.ndim

from SciPy.cluster.vq import kmeans,vq,whiten

sp.io.savemat('file.mat', {'a': arr})  # savemat expects a dictionary
%data = spio.loadmat('file.mat')
%data['a']



### Key Packages
# scipy.constants	    Physical and mathematical constants
# scipy.integrate
# scipy.interpolate
# scipy.stats	        Statistics
# scipy.linalg	        Linear algebra


### Other Packages
# scipy.cluster	        Vector quantization / Kmeans
# scipy.fftpack	        Fourier transform
# scipy.io
# scipy.ndimage	        n-dimensional image package
# scipy.odr	            Orthogonal distance regression
# scipy.optimize	    Optimization
# scipy.signal	        Signal processing
# scipy.sparse	        Sparse matrices
# scipy.spatial	        Spatial data structures and algorithms
# scipy.special	        Any special mathematical functions


from scipy.stats import gamma           # try if it works
x = np.r_[0:10:0.1]
plt.plot(x, gamma.pdf(x,2))
plt.plot(x, gamma.pdf(x,2,3))


# lookfor("gaussian", module="scipy") --> can't find lookfor