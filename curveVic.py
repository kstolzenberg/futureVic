# loft between manipulated curves - add detailing!!!
# model units are feet

import rhinoscriptsyntax as rs

def curveVic ():
    profiles = []
    firstCrv = rs.GetObject("pick a base curve", 4, True, True)
    
    # note offsetCurve is planar. copy will translate and copy!    
    # profiles = rs.OffsetCurve(firstCrv, [0,0,10], 2.0)
    profiles.append(firstCrv)
    profiles.append(rs.CopyObject(firstCrv,[0,0,5]))
    print profiles
    
    # append curves to a list and then loft result!
#    rs.AddLoftSrf(profiles)
#    rs.DeleteObjects(profiles)

curveVic()