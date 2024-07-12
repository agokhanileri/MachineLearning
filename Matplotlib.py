import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import math
# help('matbplotlib')
plt.close(fig='all')            # close all figs

## a) Basic 2D Plot
x = np.arange(0, 10, 1)

# Syntax: plot([x], y, [fmt], data=None, **kwargs)
  # fmt specifies line color, marker, style --> kwargs override fmt
  # kwargs  //  line label (for auto legends), linewidth, antialiasing, marker face color

# plt.plot(x, x, color='blue', marker='.', linestyle='solid')  # default linewidth = 1
fig = plt.figure('a) Basics')
plt.plot(x, x, '-b', linewidth=2.0, label='line1')     # short declaration, # '-.' = dashdot, ':' = dotted
plt.plot(x, x**2, '--r', linewidth=2.0, label='line2')  # hold on is inherent --> how to append?
plt.legend(loc='best')      # legend comes from the labeling of each plot
plt.title('Title', fontsize=14, fontweight='bold')
plt.ylabel('Ylabel')
plt.xlabel('Xlabel')
plt.grid(color='0.75', linestyle='--', linewidth=0.5)   # grid: 0-1 range to get gray shades
plt.grid(linestyle='--', linewidth=0.5, alpha=0.4)      # alternative
plt.xlim(0, 6)
plt.ylim(0, 40)
# plt.show()     # only for interactive session
# '-' = solid
# '--' = dashed
# ':' = dotted
# '-.' = dot - dashed
# '.' = points
# 'o' = filled circles
# '^' = filled triangles


# # b) Subplot, Append, Size, Limits, Axes
# Matlab way: plt keeps track of the current axes
fig = plt.figure('b) Subplot, Axes')
plt.subplot(1, 2, 1)
plt.plot(x, x*5, '-b', linewidth=2.0, label='line1')
plt.ylabel('yy')
plt.xlabel('xx')
plt.title('subplot1', fontsize=14, fontweight='bold')
plt.subplot(1, 2, 2)
plt.plot(x, x**2, '-r', linewidth=2.0, label='line2')
plt.ylabel('yy')
plt.xlabel('xx')
plt.title('subplot2', fontsize=14, fontweight='bold')
#limits
ybtm, ytop = plt.ylim()            # return the current ylim
plt.subplot(1, 2, 1)
plt.xlim(0, 5)
plt.subplot(1, 2, 2)
plt.ylim(0, 40)
plt.tight_layout()                      # optimizes space

# OOP version, you can loop through the axes instead of repeating
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4), sharey=True, dpi=120)  # returns fig + axes, size = (W,H)
# sharey=True --> shares the Y axes between the subplots
ax1.set(title='subplot1', xlabel='xx', ylabel='yy', xlim=(0, 6), ylim=(0, 12))  # now you got more control
p1  = ax1.plot(x*5, 'b-')                 # dummy plot on 1st subfig
#ax1  = plt.gca()                       # get current axis (subplot)
ax1.clear()                             # don't wanna append it, so clear it
ax2.set(title='subplot2', xlabel='xx', ylabel='yy', xlim=(0, 6), ylim=(0, 12))
p2  = ax2.plot(x**2, 'r-')                 # replot on 2nd subfig
plt.suptitle("General Title")           # super title
plt.tight_layout()                      # optimizes space --> a must

fig = plt.gcf()                         # //   //   figure
fig.clear()                             #  = plt.clf()
fig.canvas.set_window_title('Shared Axes') # canvas title
ax1 = fig.add_subplot(1, 1, 1)
ax1.set_xlabel('x')
ax1.set_ylabel('5x', color='blue')
ax1.plot(x, 5*x, color='blue')
ax1.tick_params(axis='y', labelcolor='blue')
ax2 = ax1.twinx()       # create a clone y-axis that shares same x-axis
ax2.set_ylabel('x^2', color='red')
ax2.plot(x, x**2, color='red')
ax2.tick_params(axis='y', labelcolor='red')
ax1.set_title('Sharing Axes')
plt.tight_layout()


## c) Advanced: Ticks, Ticklabels,  Legend
xx  = np.linspace(0, 2*np.pi, 1000)
fig = plt.figure('c) Ticks, Append')
#plt.close(fig='Cosine')           # close using the figure name
ax  = fig.add_subplot(1, 1, 1)
p1,  = ax.plot(xx, np.sin(xx), 'b-') # replot, comma for legend later, because syntax is: handles, labels = ax.plot
# p2 = plt.plot(xx, np.cos(xx), 'r-')
p2, = plt.plot(xx, xx**xx, 'r-')

plt.title(r'$\sin(2 \pi x)$')  # can use LaTeX symbols, 'r' before the string indicates "raw string"

# inwards pointing ticks on all 4 sides
ax.yaxis.set_ticks_position('none')             # disables y-axis ticks
plt.xticks(ticks=np.arange(0, 10, 1), fontsize=11, rotation=30, ha='center', va='top')
plt.yticks(ticks=np.arange(0, 10, 0.5), fontsize=11, rotation=0, ha='right', va='center')
plt.ylim(0,10)
plt.tick_params(axis='both', bottom=True, top=True, left=True, right=True, direction='in', which='major', grid_color='black')
plt.grid(color='0.75', linestyle='--', linewidth=0.5)   # inward ticks + grid looks great

plt.legend([p1, p2], ['line 1', 'line 2'])                  # typical
plt.legend([p1, p2], ['line 1', 'line 2'],                  # typical
           frameon=True,                                    # border
           framealpha=1,                                    #  // transparency
           ncol=2,                                          # num columns
           shadow=True,                                     # shadow on
           borderpad=2,                                     # thickness of border
           title='My Legend',                               # legend title
           loc='upper right')                               # location


## d) 3D Plot
# from mpl_toolkits.mplot3d import Axes3D

xx = np.arange(1, 11, 1)
yy = np.arange(5, 15, 1)
X, Y = np.meshgrid(xx, yy)
zz = np.arange(1, 101, 1)
Z = zz.reshape(X.shape)

fig = plt.figure('d) 3D Plot, Colorbar')
ax = fig.gca(projection='3d')
#ax = plt.axes(projection='3d')
c1 = ax.plot_surface(X, Y, Z,  rstride=8, cstride=8, alpha=0.9, facecolors=cm.jet(Z))
surf = ax.plot_surface(X, Y, Z, cmap=cm.jet, vmin=np.min(Z), vmax=np.max(Z), rstride=1, cstride=1)
cbar = fig.colorbar(surf, shrink=0.5, aspect=5)
cbar.set_label('JinJin', rotation=0,  labelpad=-40, y=1.1)
ax.set_xlabel('X'); ax.set_xlim3d(0, 20)
ax.set_ylabel('Y')
ax.set_ylim3d(0, 20)
ax.set_zlabel('Z')
ax.set_zlim3d(0, 150)



# ax.plot_surface(xx, yy, zz, cmap=plt.cm.jet, rstride=1, cstride=1, linewidth=0)
ax.plot_surface(X, Y, Z, cmap=plt.cm.jet,  vmin=np.min(Z), vmax=np.max(Z))
plt.xlabel('x')
plt.ylabel('y')
#plt.zlabel('z')

g = ax.imshow([X, Y, Z], interpolation='nearest', vmin=1, vmax=9)
plt.colorbar(g)

#plt.colorbar(Z, ax = ax)

# pos = ax.imshow(Z, cmap='jet', interpolation='none')
fig.colorbar(Z, ax=ax)

# fig.colorbar(surf, shrink=.5, aspect= 9, extend='both')




#ax.plot3D(xx, yy, zz)

## e) Contour Plot
fig = plt.figure('e) Contour Plot, Colorbar')



## f) Histogram Plot
data = np.random.rand(1000)                 #  
np.mean(data)
np.std(data)

fig = plt.figure('f) Histogram Plot')
plt.hist(data);
ax = fig.gca()
ax.set_xlabel('Bins'); 
ax.set_ylabel('Occurences')
plt.show()  


## g) Other Types: Box, Pie
# https://365datascience.com/chart-types-and-how-to-select-the-right-one/\
fig = plt.figure('g) Box, Chart, Pie')
labels = 'pie1', 'pie2', 'pie3'
sizes = [20, 30, 50]
explode = (0, 0.1, 0)                    # separate the 2nd slice by 0.1

ax = fig.gca()
ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)

ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()


#Skip: Treemap, Stacked Area, Doughnut, Bridge,
