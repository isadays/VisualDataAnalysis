####### File:        hydrogen.py
####### Description: Iso-contours extraction from a volume
#######              Run this example from a command prompt by typing: 
#######              "python hydrogen.py" or "pvpython hydrogen.py"
##
import sys
import vtk

# image reader

filename = "hydrogen.vtk"
reader = vtk.vtkStructuredPointsReader()
reader.SetFileName(filename)
# must call Update() before we fetch the dimensions
reader.Update()

# get the extent of the data and print it
W, H, D = reader.GetOutput().GetDimensions()
# string formatting
print("Reading '%s', width=%i, height=%i, depth=%i" % (filename, W, H, D))

# create an outline of the dataset
outline = vtk.vtkOutlineFilter()
outline.SetInputData(reader.GetOutput())
outlineMapper = vtk.vtkPolyDataMapper()
outlineMapper.SetInputConnection(outline.GetOutputPort())
outlineActor = vtk.vtkActor()
outlineActor.SetMapper(outlineMapper)

# the actor's property 
outlineActor.GetProperty().SetColor(0.0, 0.0, 1.0)
outlineActor.GetProperty().SetLineWidth(2.0)

# Iso-surface extraction using vtkContourFilter
contourFilter = vtk.vtkContourFilter()
contourFilter.SetInputData(reader.GetOutput())
contourFilter.SetValue(0, 0.03) 

# Colormap the surfaces using vtkColorTransferFunction
colorTransferFunction = vtk.vtkColorTransferFunction()
colorTransferFunction.AddRGBPoint(0.0, 0.0, 0.0, 1.0)  # Blue
colorTransferFunction.AddRGBPoint(1.0, 1.0, 0.0, 0.0)  # Red

# Create a mapper for the contourFilter
isoSurfaceMapper = vtk.vtkPolyDataMapper()
isoSurfaceMapper.SetInputConnection(contourFilter.GetOutputPort())

# Use the color transfer function directly in the mapper
isoSurfaceMapper.SetScalarRange(reader.GetOutput().GetScalarRange())

#isoSurfaceMapper.SetLookupTable(colorTransferFunction)
isoSurfaceMapper.UseLookupTableScalarRangeOn()

# Create an actor for the isosurfaces
isoSurfaceActor = vtk.vtkActor()
isoSurfaceActor.SetMapper(isoSurfaceMapper)

# Add a colorbar to the visualization scene using vtkScalarBarActor
colorBar = vtk.vtkScalarBarActor()
colorBar.SetLookupTable(isoSurfaceMapper.GetLookupTable())
colorBar.SetTitle("Probability")
colorBar.SetNumberOfLabels(5)

# renderer and render window 
ren = vtk.vtkRenderer()
ren.SetBackground(.8, .8, .8)
renWin = vtk.vtkRenderWindow()
renWin.SetSize(400, 400)
renWin.AddRenderer(ren)

# render window interactor
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)

# add the actors
ren.AddActor(outlineActor)
ren.AddActor(isoSurfaceActor)
renWin.Render()

# Set up the scalar bar widget
colorBarWidget = vtk.vtkScalarBarWidget()
colorBarWidget.SetScalarBarActor(colorBar)
colorBarWidget.SetInteractor(iren)  
colorBarWidget.On()

# Create a text actor to display the current isovalue
textActor = vtk.vtkTextActor()
textActor.SetTextScaleModeToNone()
textActor.GetPositionCoordinate().SetCoordinateSystemToNormalizedDisplay()
textActor.SetPosition(0.02, 0.9)  
textActor.GetTextProperty().SetFontSize(16)
textActor.GetTextProperty().SetColor(1.0, 1.0, 1.0) 

# Add the text actor to the renderer
ren.AddActor(textActor)

# Set up animation scene
animationScene = vtk.vtkAnimationScene()
animationScene.SetModeToSequence()

# Set the start and end times for the animation
animationScene.SetStartTime(0)
animationScene.SetEndTime(100)  
animationScene.SetFrameRate(12)

# Function to reset the animation
def resetAnimation(obj, event):
    global animationScene
    animationScene.SetAnimationTime(0)
    animationScene.Play()

# Create a callback command for left-button click
def leftButtonClickCallback(obj, event):
    global clickCount
    clickCount += 1
    if clickCount == 2:
        resetAnimation(obj, event)
        clickCount = 0

# Set up a timer for detecting double-click
clickCount = 0
timer_id = None

def on_timer(obj, event):
    global clickCount, timer_id
    clickCount = 0
    obj.DestroyTimer(timer_id)

iren.AddObserver(vtk.vtkCommand.TimerEvent, on_timer)
iren.AddObserver(vtk.vtkCommand.LeftButtonPressEvent, leftButtonClickCallback)

def resetTimerCallback(obj, event):
    global timer_id
    if timer_id:
        iren.DestroyTimer(timer_id)
    timer_id = iren.CreateRepeatingTimer(500) 

iren.AddObserver(vtk.vtkCommand.LeftButtonPressEvent, resetTimerCallback)


# Add a callback function to update isovalue for each frame
def updateIsovalueCallback(obj, event):
    global contourFilter, renWin
    frame = animationScene.GetAnimationTime()
    if frame is not None:
        isovalue = frame / animationScene.GetEndTime() 
        contourFilter.SetValue(0, isovalue)
        renWin.Render()
        #Update the text actor with the current isovalue
        textActor.SetInput("Probability: {:.2f}".format(isovalue))

# Add the callback function to the animation scene
animationScene.AddObserver("AnimationCueTickEvent", updateIsovalueCallback)

# Start the animation scene
animationScene.Play()


iren.Start()  

