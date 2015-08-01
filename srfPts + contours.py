# creates interpolated curve from a surface - not sure where this would used

import rhinoscriptsyntax as rs

def ptsOnSrf ():
    surfaceId = rs.GetObject("pick surface", 8, True, True)
    uVal = rs.GetInteger("pick u/row count",4, 1, 20)
    vVal = rs.GetInteger("pick v/col count",4, 1, 20)
    uDomain = rs.SurfaceDomain(surfaceId, 0)
    vDomain = rs.SurfaceDomain(surfaceId, 1)
    uStep = (uDomain[1] - uDomain[0])/ uVal
    vStep = (vDomain[1] - vDomain[0])/ vVal
    count = 0
    allPts = []
    
    for i in rs.frange(uDomain[0], uDomain[1], uStep):
        for j in rs.frange(vDomain[0], vDomain[1], vStep):
            point = rs.EvaluateSurface(surfaceId, i, j)
            newPt = rs.AddPoint(point)
            allPts.append(newPt)
            
    rs.AddInterpCrvOnSrf(surfaceId, allPts)
    rs.DeleteObjects(allPts)

# issue with list types and the unrolling! needs tweaks!
def contour (crvOffset):
    # get geometry
    surfaceId = rs.GetObject("pick surface to contour", 0, True, True)
    startPt = rs.GetPoint("base point of contours")
    endPt = rs.GetPoint("end point of contours")
    count = 0
    
    # make contours
    newCrvs = rs.AddSrfContourCrvs(surfaceId, (startPt, endPt), crvOffset) # output is a list of GUIDs. can't access raw points
    
    # divide the target surface
    printBed = rs.GetObject("pick surface for layout", 8, True, True)
    intCount = len(newCrvs)
    uDomain = rs.SurfaceDomain(printBed, 0)
    vDomain = rs.SurfaceDomain(printBed, 1)
    uStep = (uDomain[1] - uDomain[0]) / intCount
    
    for u in rs.frange(uDomain[0], uDomain[1], uStep):
        target = rs.SurfaceFrame(printBed, [u,1])
        target = target[0] # this is a list of points are the origin points?!?!?
        #print type(target)
        #rs.AddSphere(target, 1)# this is a debug - its making frames in the right place!
    
    # add text, reference and orient!
    for crv in newCrvs:
        count += 1
        crvPl = rs.CurvePlane(crv)
        #crvPl = rs.PointAdd(crvPl[0], (0,0,-1)) # adjust text from plane origin - could fine tune further
        rs.AddText(count, crvPl, 0.25) # should you label on the ground?
        reference = rs.CurveMidPoint(crv) # yes these are 3-d points
        #print type(reference)
        # these are both point lists!!! still throwing a type error?!?!!
        for i in range(0, intCount):
            rs.OrientObject(crv, reference[i], target[i])

contour(1)

#ptsOnSrf()
