get_ipython().magic(u'matplotlib inline')
import matplotlib.pylab as plt
import numpy as np
import math
def koch(a1,a2,b1,b2,iteration):
    a = [a1,a2]
    b = [b1,b2]
    theta = np.arctan((b2-a2)/(b1-a1))
    length = np.sqrt((a1-b1)**2+(a2-b2)**2)
    c1 = (2*a1+b1)/3.
    c2 = (2*a2+b2)/3.
    c = [c1,c2]
    d1 = (a1+2*b1)/3.
    d2 = (a2+2*b2)/3.
    d = [d1,d2]
    if c1 >= a1:
        m1 = c1 + (length/3.)*math.cos(theta+math.pi/3.)
        m2 = c2 + (length/3.)*math.sin(theta+math.pi/3.)
    else:
        m1 = c1 + (length/3.)*math.cos(theta-2*math.pi/3.)
        m2 = c2 + (length/3.)*math.sin(theta-2*math.pi/3.)
    m = [m1,m2]
    points = []
    if iteration == 0:
        points.extend([a,b])
    elif iteration == 1:
        points.extend([a, c, m, d, b])
    else:
        points.extend(koch(a1,a2,c1,c2,iteration-1))
        points.extend(koch(c1,c2,m1,m2,iteration-1))
        points.extend(koch(m1,m2,d1,d2,iteration-1))
        points.extend(koch(d1,d2,b1,b2,iteration-1)) 
    return points
points = koch(a1=0,a2=0,b1=1,b2=0,iteration=5)
points1 = koch(a1=1,a2=0,b1=0.5,b2=-np.sqrt(3)/2.,iteration=5)
points2 = koch(a1=0.5,a2=-np.sqrt(3)/2.,b1=0,b2=0,iteration=5)
Points = []
for i in range(len(points)):
    Points.append(np.array(points[i]))
for i in range(len(points1)):
    Points.append(np.array(points1[i]))
for i in range(len(points2)):
    Points.append(np.array(points2[i]))
plt.plot([p[0] for p in Points], [p[1] for p in Points], 'purple')
plt.fill([p[0] for p in Points], [p[1] for p in Points], 'purple')


#######################################
points3 = koch(a1=2,a2=0,b1=3,b2=0,iteration=5)
points4 = koch(a1=3,a2=0,b1=2.5,b2=-np.sqrt(3)/2.,iteration=5)
points5 = koch(a1=2.5,a2=-np.sqrt(3)/2.,b1=2,b2=0,iteration=5)
Points2 = []
for i in range(len(points3)):
    Points2.append(np.array(points3[i]))
for i in range(len(points4)):
    Points2.append(np.array(points4[i]))
for i in range(len(points5)):
    Points2.append(np.array(points5[i]))
plt.plot([p[0] for p in Points2], [p[1] for p in Points2], 'blue')
plt.fill([p[0] for p in Points2], [p[1] for p in Points2], 'blue')


########################################
points6 = koch(a1=1,a2=np.sqrt(3)/3.,b1=2,b2=np.sqrt(3)/3.,iteration=5)
points7 = koch(a1=2,a2=np.sqrt(3)/3.,b1=1.5,b2=-np.sqrt(3)/6.,iteration=5)
points8 = koch(a1=1.5,a2=-np.sqrt(3)/6.,b1=1,b2=np.sqrt(3)/3.,iteration=5)
Points3 = []
for i in range(len(points6)):
    Points3.append(np.array(points6[i]))
for i in range(len(points7)):
    Points3.append(np.array(points7[i]))
for i in range(len(points8)):
    Points3.append(np.array(points8[i]))
plt.plot([p[0] for p in Points3], [p[1] for p in Points3], 'green')
plt.fill([p[0] for p in Points3], [p[1] for p in Points3], 'green')


########################################
points9 = koch(a1=2,a2=-4*np.sqrt(3)/6.,b1=3,b2=-4*np.sqrt(3)/6.,iteration=5)
points10 = koch(a1=3,a2=-4*np.sqrt(3)/6.,b1=2.5,b2=-7*np.sqrt(3)/6.,iteration=5)
points11 = koch(a1=2.5,a2=-7*np.sqrt(3)/6.,b1=2,b2=-4*np.sqrt(3)/6.,iteration=5)
Points4 = []
for i in range(len(points9)):
    Points4.append(np.array(points9[i]))
for i in range(len(points10)):
    Points4.append(np.array(points10[i]))
for i in range(len(points11)):
    Points4.append(np.array(points11[i]))
plt.plot([p[0] for p in Points4], [p[1] for p in Points4], 'cyan')
plt.fill([p[0] for p in Points4], [p[1] for p in Points4], 'cyan')


##########################################
points12 = koch(a1=0,a2=-4*np.sqrt(3)/6.,b1=1,b2=-4*np.sqrt(3)/6.,iteration=5)
points13 = koch(a1=1,a2=-4*np.sqrt(3)/6.,b1=0.5,b2=-7*np.sqrt(3)/6.,iteration=5)
points14 = koch(a1=0.5,a2=-7*np.sqrt(3)/6.,b1=0,b2=-4*np.sqrt(3)/6.,iteration=5)
Points5 = []
for i in range(len(points12)):
    Points5.append(np.array(points12[i]))
for i in range(len(points13)):
    Points5.append(np.array(points13[i]))
for i in range(len(points14)):
    Points5.append(np.array(points14[i]))
plt.plot([p[0] for p in Points5], [p[1] for p in Points5], 'orange')
plt.fill([p[0] for p in Points5], [p[1] for p in Points5], 'orange')


#########################################
points15 = koch(a1=1,a2=-np.sqrt(3),b1=2,b2=-np.sqrt(3),iteration=5)
points16 = koch(a1=2,a2=-np.sqrt(3),b1=1.5,b2=-9*np.sqrt(3)/6.,iteration=5)
points17 = koch(a1=1.5,a2=-9*np.sqrt(3)/6.,b1=1,b2=-np.sqrt(3),iteration=5)
Points6 = []
for i in range(len(points15)):
    Points6.append(np.array(points15[i]))
for i in range(len(points16)):
    Points6.append(np.array(points16[i]))
for i in range(len(points17)):
    Points6.append(np.array(points17[i]))
plt.plot([p[0] for p in Points6], [p[1] for p in Points6], 'gray')
plt.fill([p[0] for p in Points6], [p[1] for p in Points6], 'gray')


#########################################
points18 = koch(a1=1,a2=-np.sqrt(3),b1=1,b2=0,iteration=5)
points19 = koch(a1=1,a2=0,b1=2.5,b2=-np.sqrt(3)/2,iteration=5)
points20 = koch(a1=2.5,a2=-np.sqrt(3)/2,b1=1,b2=-np.sqrt(3),iteration=5)
Points7 = []
for i in range(len(points18)):
    Points7.append(np.array(points18[i]))
for i in range(len(points19)):
    Points7.append(np.array(points19[i]))
for i in range(len(points20)):
    Points7.append(np.array(points20[i]))
plt.plot([p[0] for p in Points7], [p[1] for p in Points7], 'red')
plt.fill([p[0] for p in Points7], [p[1] for p in Points7], 'red')

plt.title("Lv.5")
plt.axis('equal')
plt.axis('on')
plt.show()