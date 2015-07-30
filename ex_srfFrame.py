# watch the float casting! here some int/float types changed! == rs.frange
# modified from RhinoPythonPrimer Rev3
import rhinoscriptsyntax as rs

idSurface = rs.GetObject("srf to frame? ", 8, True, True)
intCount = rs.GetReal("# of itera. per direction")

#domains are rough dims of the surface - can check via _what 
uDomain = rs.SurfaceDomain(idSurface, 0)
vDomain = rs.SurfaceDomain(idSurface, 1)

# get size int from domain & / by intended count = increment between surfaces
uStep = (uDomain[1] - uDomain[0]) / intCount
vStep = (vDomain[1] - vDomain[0]) / intCount

#print uStep
#print vStep

rs.EnableRedraw(False)

# loop through size of surface by step increment in both u & v directions
for u in rs.frange(uDomain[0], uDomain[1], uStep):
    for v in rs.frange(vDomain[0], vDomain[1], vStep):
        pt = rs.EvaluateSurface(idSurface, u, v) # get points at each domain step
        if rs.Distance(pt, rs.BrepClosestPoint(idSurface, pt)[0]) < 0.1:
            srfFrame = rs.SurfaceFrame(idSurface, [u, v]) # create ref plane at each division point
            newPlane = rs.AddPlaneSurface(srfFrame, 1.0, 1.0) # create surface at each ref plane
            centerPt = rs.SurfaceAreaCentroid(newPlane) # locate center of each new plane
            # how to make all of these lines end at the same?
            # endPt = rs.PointAdd(centerPt[0],(0,0,10))
            rs.AddLine(centerPt[0], rs.PointAdd(centerPt[0], (0,0,10))) # add height guideline from plane's origin
            
rs.EnableRedraw(True) # refresh viewport at one time only