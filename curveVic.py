# loft between manipulated curves - add detailing!!!
# model units are feet

import rhinoscriptsyntax as rs

def curveVic ():
    profiles = []
    firstCrv = rs.GetObject("pick a base curve", 4, True, True)
    count = rs.GetInteger("how many total curves")
    
    # vertically offset curves
    for i in range(count):
        if count == 0 or count == 1:
            return
        else:
            profiles.append(rs.CopyObject(firstCrv,[0,0,5*i]))
    
    # loft curves and clean up
    rs.AddLoftSrf(profiles, closed=True)
    profiles.append(firstCrv)
    rs.DeleteObjects(profiles)

curveVic()