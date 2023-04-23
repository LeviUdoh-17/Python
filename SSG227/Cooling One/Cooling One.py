# Author-OA Fakinlede
# Description-Furnace Wall Simulation: 
# Creates a parametric drawing of the cooling system 
#   on a heated wall for CFD simulation

# Date Created:     August 9, 2020
# Last Edited:      August 11, 2020   

# Motivation: Need to automate the CGD simulation process 

import adsk.core, adsk.fusion, traceback, math


def run(context):
    zero = adsk.core.ValueInput.createByReal(0)
    jot = adsk.core.ValueInput.createByReal(.2)
    fLen = 25
    width = 1000/10
    height = width/2
    thickNess = height/10
    pipes = 7
    pipeDia = width/100
    pipeThickNess = pipeDia/10
    halfPipeLen = 0.8 * height / 2
    ui = None
    try:
        #  Get the User Interface, used for outputting the message box to the user       
        app = adsk.core.Application.get()
        ui  = app.userInterface
        # Get the Root Component of the active design
        design = app.activeProduct
        rootComp = design.rootComponent
        features = rootComp.features
        # Create the extrusion.
        extrudes = rootComp.features.extrudeFeatures
        # Create sketch 1 on the xy plane. 
        # First access the sketches collection of the root component
        sketches = rootComp.sketches
        # Get the xy construction plane from the root component
        xyPlane = rootComp.xZConstructionPlane
        xzPlane = rootComp.xYConstructionPlane
        extrPlane = rootComp.xZConstructionPlane
        # Add sketch 1 to the sketch collection using the xy plane
        sketch1 = sketches.add(xyPlane)
        sketch2 = sketches.add(xzPlane)
        skeXtr = sketches.add(extrPlane)
        # Centerlines of all internal pipes. 
        # Begins with the central pipe and then to the left and right pipes         
        lineXtr = skeXtr.sketchCurves.sketchLines
        lines = sketch1.sketchCurves.sketchLines
        arcs = sketch1.sketchCurves.sketchArcs
        ptEks = 0
        ptWai = halfPipeLen
        ptZed = 0
        ptOrigin = adsk.core.Point3D.create(0,  0, 0)
        ptOne = adsk.core.Point3D.create(ptEks,  ptWai, ptZed)
        ptTwo = adsk.core.Point3D.create(ptEks, - ptWai, ptZed)
        lineZero = lines.addByTwoPoints(ptOne, ptTwo)
        circles = sketch2.sketchCurves.sketchCircles
        circle1 = circles.addByCenterRadius(ptOrigin, width/100)
        circle2 = circles.addByCenterRadius(ptOrigin, width/125)
        # Create a set to collect the lines and arcs
        collection = adsk.core.ObjectCollection.create()
        collection.add(lineZero) # Add the zeroth line
        sweeps = rootComp.features.sweepFeatures
        #pipeLine = features.createPath(lineZero)
        ptWai1 = - halfPipeLen
        # Sign changer
        prod = - 1
        for i in range(pipes // 2):
            prod *= -1
            ptEks1 = (i + 1) * width/(pipes+1)
            ptZed1 = 0
            rad = prod * (ptEks -  ptEks1)/2
            ptWaiPlus =  ptWai1 + rad 
            avg = (ptEks1 + ptEks)/2
            ptOneRight = adsk.core.Point3D.create(ptEks1, - ptWai1, ptZed1)
            ptTwoRight = adsk.core.Point3D.create(ptEks1, ptWai1, ptZed1)
            ptThreeRight = adsk.core.Point3D.create(avg, - ptWaiPlus, ptZed1)
            ptOneLeft = adsk.core.Point3D.create(- ptEks1, - ptWai1, ptZed1)
            ptTwoLeft = adsk.core.Point3D.create(- ptEks1, ptWai1, ptZed1)
            ptThreeLeft = adsk.core.Point3D.create(-avg, ptWaiPlus, ptZed1)
            lineRight = lines.addByTwoPoints(ptOneRight, ptTwoRight)
                   
            arcRight = arcs.addByThreePoints(ptOne,  ptThreeRight, ptOneRight)
            collection.add(arcRight)
            collection.add(lineRight) 
            lineLeft = lines.addByTwoPoints(ptOneLeft, ptTwoLeft)            
            arcLeft = arcs.addByThreePoints(ptTwo, ptThreeLeft, ptTwoLeft)
            # Merge the two lines   
            collection.add(arcLeft)
            collection.add(lineLeft) 
            # Create a path and let it find connected curves automatically
            ptEks = ptEks1
            ptWai1 = - ptWai1
            ptOne = ptTwoRight
            ptTwo = ptOneLeft

        #pipeLine.addCurves(arcs, 2) 
        if (((pipes + 1) / 2) % 2):
            yVal = - 0.8 * height / 2
            yValPlus = - 1.5 * height / 2
        else:
            yVal = 0.8 * height / 2
            yValPlus = 1.5 * height / 2

        ptOneLeft = adsk.core.Point3D.create(-50 + 100/(pipes + 1), yVal, ptZed1)
        ptTwoLeft = adsk.core.Point3D.create(-50 + 100/(pipes + 1), yValPlus, ptZed1)
        lineExtLeft = lines.addByTwoPoints(ptOneLeft, ptTwoLeft) 
        collection.add(lineExtLeft)       
        
        ptOneRight = adsk.core.Point3D.create(50 - 100/(pipes + 1), - yVal, ptZed1)
        ptTwoRight = adsk.core.Point3D.create(50 - 100/(pipes + 1), - yValPlus, ptZed1)
        lineExtRight = lines.addByTwoPoints(ptOneRight, ptTwoRight) 
        collection.add(lineExtRight) 

        pipeLine = features.createPath(collection) 
        sweepInput = sweeps.createInput(sketch2.profiles[0], pipeLine, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        # Create the sweep.
        sweep = sweeps.add(sweepInput)

        # The wall profile is now drawn
        #  Draw a rectangle by a center point.
        recLines = lineXtr.addCenterPointRectangle(adsk.core.Point3D.create(0, 0, 0), adsk.core.Point3D.create(width/2, (width/4)*(6/5) , 0))
        extrudeInput1 = extrudes.createInput(skeXtr.profiles[0], adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        # Create a distance extent definition           
        # extrudeInput.setOneSideExtent(extentDist, adsk.fusion.ExtentDirections.PositiveExtentDirection)
        dist = adsk.core.ValueInput.createByReal(width/20)
        extrudeInput1.setDistanceExtent(True, dist)        
        startOffset1 = adsk.fusion.OffsetStartDefinition.create(zero)
        # Set the start extent of the extrusion
        extrudeInput1.startExtent = startOffset1
        extrudeInput1.opacity = 0.4
        # Create the extrusion
        extrude1 = extrudes.add(extrudeInput1)
        #There are three sweeps:
        # 1. Create the passage inside the wall to contain the pipe
        # 2. Create the solid pipe
        # 3. Make the Pipe hollow        
        sweepInput1 = sweeps.createInput(sketch2.profiles[1], pipeLine, adsk.fusion.FeatureOperations.CutFeatureOperation)
        # Create the sweep.
        sweep = sweeps.add(sweepInput1)      
        sweepInput2 = sweeps.createInput(sketch2.profiles[0], pipeLine, adsk.fusion.FeatureOperations.CutFeatureOperation)
        # Create the sweep.
        sweep = sweeps.add(sweepInput2)      
        sweepInput3 = sweeps.createInput(sketch2.profiles[0], pipeLine, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        # Create the sweep.
        sweep = sweeps.add(sweepInput3)

        # Sealing the Pipes
        planes = rootComp.constructionPlanes
        planeInput = planes.createInput()
        planeInput.setByDistanceOnPath(pipeLine, adsk.core.ValueInput.createByReal(0))
        plane1 = planes.add(planeInput)
        planeInput.setByDistanceOnPath(pipeLine, adsk.core.ValueInput.createByReal(1))
        plane2 = planes.add(planeInput)
        skPlug1 = sketches.add(plane1)
        skPlug2 = sketches.add(plane2)
        circlePlug1 = skPlug1.sketchCurves.sketchCircles
        plg1Prof = circlePlug1.addByCenterRadius(ptOrigin, width/100)
        circlePlug2 = skPlug2.sketchCurves.sketchCircles
        plg2Prof = circlePlug2.addByCenterRadius(ptOrigin, width/100)
        ext = extrudes.addSimple(skPlug1.profiles[0], jot, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        ext = extrudes.addSimple(skPlug2.profiles[0], jot, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)

        # Create the Fins
        #  Draw a rectangle by a center point.
        recLines = lineXtr.addCenterPointRectangle(adsk.core.Point3D.create(0, 0, 0), adsk.core.Point3D.create(.75 * width/2, .5 , 0))
        extrudeInput1 = extrudes.createInput(skeXtr.profiles[1], adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        # Create a distance extent definition           
        # extrudeInput.setOneSideExtent(extentDist, adsk.fusion.ExtentDirections.PositiveExtentDirection)
        fStart = dist
        dist = adsk.core.ValueInput.createByReal(fLen)
        extrudeInput1.setDistanceExtent(False, dist)        
        startOffset1 = adsk.fusion.OffsetStartDefinition.create(fStart)
        # Set the start extent of the extrusion
        extrudeInput1.startExtent = startOffset1
        extrudeInput1.opacity = 0.4
        # Create the extrusion
        extrude1 = extrudes.add(extrudeInput1)
        # Get the body for pattern
        partBody = extrude1.bodies[0]

        # Create input entities for rectangular pattern
        inputEntites = adsk.core.ObjectCollection.create()
        inputEntites.add(partBody)
        
        # Get x and y axes for rectangular pattern
        zAxis = rootComp.zConstructionAxis
        yAxis = rootComp.yConstructionAxis
        
        # Quantity and distance
        quantityOne = adsk.core.ValueInput.createByString('5')
        distanceOne = adsk.core.ValueInput.createByString('-20  cm')
        distanceTwo = adsk.core.ValueInput.createByString('20  cm')
        
        # Create the input for rectangular pattern
        rectangularPatterns = rootComp.features.rectangularPatternFeatures
        rectangularPatternInput = rectangularPatterns.createInput(inputEntites, zAxis, quantityOne, distanceOne, adsk.fusion.PatternDistanceType.ExtentPatternDistanceType)
        anotherPatternInput = rectangularPatterns.createInput(inputEntites, zAxis, quantityOne, distanceTwo, adsk.fusion.PatternDistanceType.ExtentPatternDistanceType)
        # Create the rectangular pattern
        rectangularFeature = rectangularPatterns.add(rectangularPatternInput)
        anotherFeature = rectangularPatterns.add(anotherPatternInput)
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
