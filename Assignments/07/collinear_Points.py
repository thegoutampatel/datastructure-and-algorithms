# Given three points, check whether they lie on a straight (collinear) or not. [Google]
# For example:
# Input- [(1,1), (1,6), (0,9)] Output- No
# Input- [(1,1), (1,4), (1,5)] Output- Yes


def Collinear(points):

    (x1,y1), (x2,y2),(x3,y3) = points
     
    area = 0.5 * abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2))

    if area == 0:
        return "Yes"
    
    else:
        return "no"


points =  [(1,1), (1,4), (1,5)]
result = Collinear(points)
print(result)