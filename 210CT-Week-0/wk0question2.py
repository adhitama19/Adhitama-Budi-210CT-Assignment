''' Write a program which reads the planar coordinates of the vertices of
    a triangle, and then describes the relative position (above, below,
    left, or right) of this triangle in relationship with a point in the
    same plane, given by its coordinate. Input a = (3,4), b = (0,5),
    c = (6,9), p = (-2,4) Output = left'''

varAx = 3
varAy = 4

varBx = 0
varBy = 5

varCx = 6
varCy = 9

varPx = -2
varPy = 4

if varPx > varBx and varPx > varCx and varPx > varAx:
    print (" The location of the point is in the left from the triangle")

elif varPx > varBx and varPx > varCx and VarPx > varAx:
    print (" The location of the point is on the right side from the triangle")

elif varPy > varBy and varPy > varCy and varPy > varAy:
    print (" The location of the point is above from the triangle")

elif varPy < varBy and varPy < varCy and varPy < varAy:
    print (" The location of the triangle is located below the triangle")
