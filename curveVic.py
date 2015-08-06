# loft between manipulated curves - add detailing!!!
# model units are feet

import rhinoscriptsyntax as rs
import random

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
    for crv in profiles:
        centerPt = rs.CurveAreaCentroid(crv)
        # deg = random.randint(0,360)
        # deg = random.randint(0,4) * 90 very swirly!
        deg = profiles.index(crv) * 10
        rs.RotateObject(crv, centerPt[0], deg)

#    centerPt = rs.CurveAreaCentroid(profiles[3])
#    rs.RotateObject(profiles[3], centerPt[0], 30)
#    centerPt = rs.CurveAreaCentroid(profiles[7])
#    rs.RotateObject(profiles[7], centerPt[0], 30)

    # scale each crv randomly
#    for crv in profiles:
#        centerPt = rs.CurveAreaCentroid(crv)
#        x = random.uniform(.25,2)
#        y = random.uniform(.25,2)
#        z = 1
#        rs.ScaleObject(crv, centerPt[0], (x,y,z) )

    # add dentils and trim. map to surface? project? rs.SporphObject() better to use in GUI flow?
    # is there any flow along surface? no center box?!?! just acquire shape
#    for j in range(len(profiles)):
#       points = rs.DivideCurveEquidistant(profiles[j], 5)
#       for k in points:
#           rs.AddSphere(k, .25)   

    # loft curves and clean up
    finalShape = rs.AddLoftSrf(profiles, closed=False)
    #profiles.append(firstCrv)
    rs.DeleteObjects(profiles)
    rs.CapPlanarHoles(finalShape)
    #rs.ProjectCurveToSurface(pcrv, finalShape, (0,0,-1)) doesn't work so well?
 
curveVic(15)