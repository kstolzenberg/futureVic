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
        deg = profiles.index(crv) * 30
        rs.RotateObject(crv, centerPt[0], deg)

    # scale each crv randomly
    for crv in profiles:
        centerPt = rs.CurveAreaCentroid(crv)
        x = random.uniform(.25,2)
        y = random.uniform(.25,2)
        z = random.uniform(.25,2)
        rs.ScaleObject(crv, centerPt[0], (x,y,z) )

    # add dentils and trim. is there any flow along surface? no center box?!?! just acquire shape
    # for j in range(len(profiles)):
    #    points = rs.DivideCurveEquidistant(profiles[j], 1.5)
    #    for k in points:
    #        rs.AddSphere(k, .25)

    # loft curves and clean up
    finalShape = rs.AddLoftSrf(profiles, closed=False)
    #profiles.append(firstCrv)
    rs.DeleteObjects(profiles)
    rs.CapPlanarHoles(finalShape)
    
    # add some trim?

curveVic(15)