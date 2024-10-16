def circlepropertieschallenge():
    diameter = float(input("Enter the diameter of the circle here. "))
    arcangle = float(input("Enter the arc angle of the circle here. "))
    radius = diameter/2
    print("The radius of this circle is",radius)
    area = (radius*radius)*3.14
    print("The area of this circle is",area)
    circumference = 3.14*diameter
    print("The circumference of this circle is",circumference)
    arclength = (circumference*arcangle)/360
    print ("The arc length is",arclength)
    
circlepropertieschallenge()    
