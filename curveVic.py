# loft between manipulated curves - add detailing!!!
# model units are feet

import rhinoscriptsyntax as rs
import Rhino as r

def curveVic (storyHt):
    profiles = []
    firstCrv = rs.GetObject("pick a base curve", 4, True, True)
    count = rs.GetInteger("how many total curves")
    #dentil = rs.GetObject("pick dentil", 8)
    
    # vertically offset curves
    for i in range(count):
        if count == 0 or count == 1:
            return
        else:
            profiles.append(rs.CopyObject(firstCrv,[0,0,storyHt*i]))
    
    # funk it up - needs to be more randomized?
#    centerPt = rs.CurveAreaCentroid(profiles[2])
    #rs.RotateObject(profiles[2], centerPt[0], 90)
    
    # make scale each step randomly?
#    centerPt = rs.CurveAreaCentroid(profiles[3])
#    rs.ScaleObject(profiles[3], centerPt[0], (1.25, 1.25, 0))
    
    # add dentils and trim. is there any flow along surface
    # no center box?!?! what a pain to build maybe build from addPlaneSurface
    # match the curve profile? array along curve? divide curve into 
    for j in profiles:
        points = rs.DivideCurveEquidistant(profiles[j], 1.5)
        
        for k in points:
            rs.AddSphere(k, .25)
    # rs.CopyObject(
    
    # loft curves and clean up
    finalShape = rs.AddLoftSrf(profiles, closed=False)
    #profiles.append(firstCrv)
    rs.DeleteObjects(profiles)
    rs.CapPlanarHoles(finalShape)

curveVic(15)