# watch the float casting! here some int/float types changed!
# modified from RhinoPythonPrimer Rev3
import rhinoscriptsyntax as rs

idSurface = rs.GetObject("srf to frame? ", 8, True, True)
intCount = rs.GetReal("# of itera. per direction")

uDomain = rs.SurfaceDomain(idSurface, 0)
vDomain = rs.SurfaceDomain(idSurface, 1)

uStep = (uDomain[1] - uDomain[0]) / intCount
vStep = (vDomain[1] - vDomain[0]) / intCount

rs.EnableRedraw(False)
for u in rs.frange(uDomain[0], uDomain[1], uStep):
    for v in rs.frange(vDomain[0], vDomain[1], vStep):
        pt = rs.EvaluateSurface(idSurface, u, v)
        if rs.Distance(pt, rs.BrepClosestPoint(idSurface, pt)[0]) < 0.1:
            srfFrame = rs.SurfaceFrame(idSurface, [u, v])
            newPlane = rs.AddPlaneSurface(srfFrame, 1.0, 1.0)
            centerPt = rs.SurfaceAreaCentroid(newPlane) # locate center
            # add height guideline from plane's origin
            # how to make all of these lines end at the same?
            # endPt = rs.PointAdd(centerPt[0],(0,0,10))
            rs.AddLine(centerPt[0], rs.PointAdd(centerPt[0], (0,0,10)))
            
rs.EnableRedraw(True)