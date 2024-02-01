# trace generated using paraview version 5.10.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

#### import the simple module from the paraview
from paraview.simple import *
import sys
import pandas as pd
import vtk
import csv
import os
from pathlib import Path


#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

    
#LoadPlugin('/Applications/ParaView-5.10.1.app/Contents/Plugins/TopologyToolKit.so', remote=False, ns=globals())

def find_topology_toolkit_path(paraview_version):
    # Specify the base directory where ParaView is installed
    paraview_base_path = f'/Applications/ParaView-{paraview_version}.app/Contents/'

    # Specify the subdirectory where the plugin is located
    plugin_subdirectory = 'Plugins'

    # Specify the name of the plugin file
    plugin_filename = 'TopologyToolKit.so'

    # Construct the full path to the plugin
    plugin_path = Path(paraview_base_path) / plugin_subdirectory / plugin_filename

    # Check if the plugin file exists
    if plugin_path.exists():
        return str(plugin_path)
    else:
        return None

# Specify the ParaView version
paraview_version = '5.10.1'  

# Find the path of the 'TopologyToolKit.so' plugin for the specified ParaView version
topology_toolkit_path = find_topology_toolkit_path(paraview_version)

# Check if the plugin is found
if topology_toolkit_path is None:
    print(f"Error: 'TopologyToolKit.so' not found for ParaView version {paraview_version}.")
else:
    # Load the plugin with the detected path
    LoadPlugin(topology_toolkit_path, remote=False, ns=globals())

def generate_isocontours(csv_file, isovalue1,isovalue2,isovalue3, output_filename):

    # create a new 'CSV Reader'
    a2d_scalar_fieldcsv = CSVReader(registrationName='csv_file', FileName=[csv_file])

    # get active view
    renderView1 = GetActiveViewOrCreate('RenderView')

    # get the material library
    materialLibrary1 = GetMaterialLibrary()

    # Properties modified on renderView1
    renderView1.OrientationAxesVisibility = 0

    # Create a new 'SpreadSheet View'
    spreadSheetView1 = CreateView('SpreadSheetView')
    spreadSheetView1.ColumnToSort = ''
    spreadSheetView1.BlockSize = 1024

    # show data in view
    a2d_scalar_fieldcsvDisplay = Show(a2d_scalar_fieldcsv, spreadSheetView1, 'SpreadSheetRepresentation')

    # get layout
    layout1 = GetLayoutByName("Layout #1")

    # add view to a layout so it's visible in UI
    AssignViewToLayout(view=spreadSheetView1, layout=layout1, hint=0)

    # Properties modified on a2d_scalar_fieldcsvDisplay
    a2d_scalar_fieldcsvDisplay.Assembly = ''

    # update the view to ensure updated data information
    spreadSheetView1.Update()

    # hide data in view
    Hide(a2d_scalar_fieldcsv, spreadSheetView1)

    # destroy spreadSheetView1
    Delete(spreadSheetView1)
    del spreadSheetView1

    # close an empty frame
    #layout1.Collapse(2)

    # set active view
    SetActiveView(renderView1)

    # create a new 'Table To Points'
    tableToPoints1 = TableToPoints(registrationName='TableToPoints1', Input=a2d_scalar_fieldcsv)
    tableToPoints1.XColumn = 'S'
    tableToPoints1.YColumn = 'S'
    tableToPoints1.ZColumn = 'S'

    # Properties modified on tableToPoints1
    tableToPoints1.XColumn = 'x'
    tableToPoints1.YColumn = 'y'
    tableToPoints1.KeepAllDataArrays = 1

    # show data in view
    tableToPoints1Display = Show(tableToPoints1, renderView1, 'GeometryRepresentation')

    # trace defaults for the display properties.
    tableToPoints1Display.DataAxesGrid.XTitle = 'X'
    tableToPoints1Display.DataAxesGrid.YTitle = 'Y'
    tableToPoints1Display.DataAxesGrid.ZTitle = 'Z'
    tableToPoints1Display.DataAxesGrid.GridColor = [0.0, 0.0, 0.0]
    tableToPoints1Display.Representation = 'Surface'
    tableToPoints1Display.ColorArrayName = [None, '']
    tableToPoints1Display.SelectTCoordArray = 'None'
    tableToPoints1Display.SelectNormalArray = 'None'
    tableToPoints1Display.SelectTangentArray = 'None'
    tableToPoints1Display.OSPRayScaleArray = 'S'
    tableToPoints1Display.OSPRayScaleFunction = 'PiecewiseFunction'
    tableToPoints1Display.SelectOrientationVectors = 'None'
    tableToPoints1Display.ScaleFactor = 1.2566000000000002
    tableToPoints1Display.SelectScaleArray = 'None'
    tableToPoints1Display.GlyphType = 'Arrow'
    tableToPoints1Display.GlyphTableIndexArray = 'None'
    tableToPoints1Display.GaussianRadius = 0.06283000000000001
    tableToPoints1Display.SetScaleArray = ['POINTS', 'S']
    tableToPoints1Display.ScaleTransferFunction = 'PiecewiseFunction'
    tableToPoints1Display.OpacityArray = ['POINTS', 'S']
    tableToPoints1Display.OpacityTransferFunction = 'PiecewiseFunction'
    tableToPoints1Display.PolarAxes = 'PolarAxesRepresentation'

    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    tableToPoints1Display.ScaleTransferFunction.Points = [-1.6361, 0.0, 0.5, 0.0, 1.9496999999999998, 1.0, 0.5, 0.0]

    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    tableToPoints1Display.OpacityTransferFunction.Points = [-1.6361, 0.0, 0.5, 0.0, 1.9496999999999998, 1.0, 0.5, 0.0]

    # reset view to fit data
    renderView1.ResetCamera(False)

    # update the view to ensure updated data information
    renderView1.Update()

    # hide data in view
    Hide(tableToPoints1, renderView1)

    # create a new 'Delaunay 2D'
    delaunay2D1 = Delaunay2D(registrationName='Delaunay2D1', Input=tableToPoints1)

    # show data in view
    delaunay2D1Display = Show(delaunay2D1, renderView1, 'GeometryRepresentation')

    # trace defaults for the display properties.
    # Properties modified on delaunay2D1Display.DataAxesGrid
    delaunay2D1Display.DataAxesGrid.XTitle = 'X'
    delaunay2D1Display.DataAxesGrid.YTitle = 'Y'
    delaunay2D1Display.DataAxesGrid.ZTitle = 'Z'
    delaunay2D1Display.DataAxesGrid.GridColor = [0.0, 0.0, 0.0]

    delaunay2D1Display.Representation = 'Surface'
    delaunay2D1Display.ColorArrayName = [None, '']
    delaunay2D1Display.SelectTCoordArray = 'None'
    delaunay2D1Display.SelectNormalArray = 'None'
    delaunay2D1Display.SelectTangentArray = 'None'
    delaunay2D1Display.OSPRayScaleArray = 'S'
    delaunay2D1Display.OSPRayScaleFunction = 'PiecewiseFunction'
    delaunay2D1Display.SelectOrientationVectors = 'None'
    delaunay2D1Display.ScaleFactor = 1.2566000000000002
    delaunay2D1Display.SelectScaleArray = 'None'
    delaunay2D1Display.GlyphType = 'Arrow'
    delaunay2D1Display.GlyphTableIndexArray = 'None'
    delaunay2D1Display.GaussianRadius = 0.06283000000000001
    delaunay2D1Display.SetScaleArray = ['POINTS', 'S']
    delaunay2D1Display.ScaleTransferFunction = 'PiecewiseFunction'
    delaunay2D1Display.OpacityArray = ['POINTS', 'S']
    delaunay2D1Display.OpacityTransferFunction = 'PiecewiseFunction'
    delaunay2D1Display.DataAxesGrid = 'GridAxesRepresentation'
    delaunay2D1Display.PolarAxes = 'PolarAxesRepresentation'

    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    delaunay2D1Display.ScaleTransferFunction.Points = [-1.6361, 0.0, 0.5, 0.0, 1.9496999999999998, 1.0, 0.5, 0.0]

    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    delaunay2D1Display.OpacityTransferFunction.Points = [-1.6361, 0.0, 0.5, 0.0, 1.9496999999999998, 1.0, 0.5, 0.0]

    # reset view to fit data
    renderView1.ResetCamera(False)

    # hide data in view
    Hide(tableToPoints1, renderView1)

    # update the view to ensure updated data information
    renderView1.Update()

    # reset view to fit data
    renderView1.ResetCamera(False)

    # hide data in view
    Hide(delaunay2D1, renderView1)

    # create a new 'Contour'
    contour1 = Contour(registrationName='Contour1', Input=delaunay2D1)
    contour1.ContourBy = ['POINTS', 'S']
    contour1.Isosurfaces = [isovalue1, isovalue2, isovalue3]

    contour1.PointMergeMethod = 'Uniform Binning'

    # Properties modified on renderView1.AxesGrid
    renderView1.AxesGrid.Visibility = 1

    # show data in view
    contour1Display = Show(contour1, renderView1, 'GeometryRepresentation')

    # get color transfer function/color map for 'S'
    sLUT = GetColorTransferFunction('S')

    # trace defaults for the display properties.
    contour1Display.Representation = 'Surface'
    contour1Display.ColorArrayName = ['POINTS', 'S']
    contour1Display.LookupTable = sLUT
    contour1Display.SelectTCoordArray = 'None'
    contour1Display.SelectNormalArray = 'None'
    contour1Display.SelectTangentArray = 'None'
    contour1Display.OSPRayScaleArray = 'S'
    contour1Display.OSPRayScaleFunction = 'PiecewiseFunction'
    contour1Display.SelectOrientationVectors = 'None'
    contour1Display.ScaleFactor = 1.2565999656011684
    contour1Display.SelectScaleArray = 'S'
    contour1Display.GlyphType = 'Arrow'
    contour1Display.GlyphTableIndexArray = 'S'
    contour1Display.GaussianRadius = 0.06282999828005842
    contour1Display.SetScaleArray = ['POINTS', 'S']
    contour1Display.ScaleTransferFunction = 'PiecewiseFunction'
    contour1Display.OpacityArray = ['POINTS', 'S']
    contour1Display.OpacityTransferFunction = 'PiecewiseFunction'
    contour1Display.PolarAxes = 'PolarAxesRepresentation'
    # Properties modified on contour1Display.DataAxesGrid
    contour1Display.DataAxesGrid.XTitle = 'X'
    contour1Display.DataAxesGrid.YTitle = 'Y'
    contour1Display.DataAxesGrid.ZTitle = 'Z'
    contour1Display.DataAxesGrid.GridColor = [0.0, 0.0, 0.0]
    # reset view to fit data
    renderView1.ResetCamera(False)

    # hide data in view
    Hide(delaunay2D1, renderView1)

    text1 = Text(registrationName='Text1')
    # Properties modified on text1
    text1.Text = 'Iso-contours'

    # show data in view
    text1Display = Show(text1, renderView1, 'TextSourceRepresentation')


    # show color bar/color legend
    contour1Display.SetScalarBarVisibility(renderView1, True)
    # Properties modified on renderView1.AxesGrid
    renderView1.AxesGrid.XTitle = 'X'
    renderView1.AxesGrid.YTitle = 'Y'
    renderView1.AxesGrid.ZTitle = 'Z'

    # update the view to ensure updated data information
    renderView1.Update()

    # Properties modified on sLUT
    sLUT.InterpretValuesAsCategories = 1
    sLUT.AnnotationsInitialized = 1

    sLUT.Annotations = [str(isovalue1), str(isovalue1), str(isovalue2), str(isovalue2), str(isovalue3), str(isovalue3)]
    # Properties modified on sLUT
    sLUT.IndexedColors = [0.3333333333333333, 0.0, 0.0, 0.0, 0.0, 0.3686274509803922, 1.0, 0.3333333333333333, 0.0]
    sLUT.IndexedOpacities = [1.0, 1.0, 1.0]

    sLUTColorBar = GetScalarBar(sLUT, renderView1)

    # Properties modified on sLUTColorBar
    sLUTColorBar.TitleFontFamily = 'Times'
    sLUTColorBar.TitleFontSize = 12
    sLUTColorBar.LabelFontFamily = 'Times'
    sLUTColorBar.LabelFontSize = 12
    sLUTColorBar.ScalarBarLength = 0.2
    # Properties modified on sLUTColorBar
    sLUTColorBar.HorizontalTitle = 1

    # Properties modified on sLUTColorBar
    sLUTColorBar.WindowLocation = 'Upper Right Corner'
    sLUTColorBar.TextPosition = 'Ticks left/bottom, annotations right/top'


    # change scalar bar placement
    sLUTColorBar.WindowLocation = 'Any Location'
    sLUTColorBar.Position = [0.9, 0.75]
    sLUTColorBar.ScalarBarLength = 0.19999999999999984


    #change interaction mode for render view
    renderView1.InteractionMode = '2D'
    

    #================================================================
    # addendum: following script captures some of the application
    # state to faithfully reproduce the visualization during playback
    #================================================================

    # saving camera placements for views

    # current camera placement for renderView1
    renderView1.InteractionMode = '2D'
    renderView1.CameraPosition = [1.7199415847102273e-07, 1.7199415847102273e-07, 35.47660999206554]
    renderView1.CameraFocalPoint = [1.7199415847102273e-07, 1.7199415847102273e-07, 0.95]
    renderView1.CameraParallelScale = 8.936144228773554

    #--------------------------------------------
    # uncomment the following to render all views
    # RenderAllViews()
    # alternatively, if you want to write images, you can use SaveScreenshot(...).
    #--------------------------------------------

    # Set the desired width and height
    width = 1920
    height = 1080


    # Take screenshot with specified dimensions
    WriteImage(output_filename, view=renderView1, ImageResolution=[width, height])

     #Now, the next step of our task is to find the critical points


    # create a new 'TTK ScalarFieldCriticalPoints'
    tTKScalarFieldCriticalPoints1 = TTKScalarFieldCriticalPoints(registrationName='TTKScalarFieldCriticalPoints1', Input=delaunay2D1)
    tTKScalarFieldCriticalPoints1.ScalarField = ['POINTS', 'S']
    tTKScalarFieldCriticalPoints1.InputOffsetField = ['POINTS', 'S']
    # Export the view to a CSV file - In this case, an error occured to generate the CSV file so we will export as a vtk file 
    output_scalarfield_vtk = 'TTK_Outputs/scalarfieldcroutput.vtk'
    SaveData(output_scalarfield_vtk, proxy=tTKScalarFieldCriticalPoints1)
    vtk_reader = LegacyVTKReader(FileNames=[output_scalarfield_vtk])
    csv_file_path = 'TTK_Outputs/scalarfieldcroutput.csv'
    SaveData(csv_file_path, proxy=vtk_reader)
    
     # create a new 'TTK PersistenceDiagram'
    #tTKPersistenceDiagram1 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram1', Input=delaunay2D1)
    #tTKPersistenceDiagram1.ScalarField = ['POINTS', 'S']
    #tTKPersistenceDiagram1.InputOffsetField = ['POINTS', 'S']
    # Please comment the following step (or change the path '/path/to/output/folder/persistenceoutput.csv')
    #Extracting data from the Filter
    #output_persistence = 'TTK_Outputs/persistenceoutput.csv'
    # Save the output of the TTKMergeandContourTreeFTM filter
    #SaveData(output_persistence, proxy=tTKPersistenceDiagram1)    

    # create a new 'TTK Merge and Contour Tree (FTM)'
    #tTKMergeandContourTreeFTM1 = TTKMergeandContourTreeFTM(registrationName='TTKMergeandContourTreeFTM1', Input=delaunay2D1)
    #tTKMergeandContourTreeFTM1.ScalarField = ['POINTS', 'S']
    #tTKMergeandContourTreeFTM1.InputOffsetField = ['POINTS', 'S']
    #Extracting data from the Filter
    #output_contourtree = 'TTK_Outputs/contourtreeoutput.csv'
    # Save the output of the TTKMergeandContourTreeFTM filter
    #SaveData(output_contourtree, proxy=tTKMergeandContourTreeFTM1)    

    # create a new 'TTK MorseSmaleComplex'
    #tTKMorseSmaleComplex1 = TTKMorseSmaleComplex(registrationName='TTKMorseSmaleComplex1', Input=delaunay2D1)
    #tTKMorseSmaleComplex1.ScalarField = ['POINTS', 'S']
    #tTKMorseSmaleComplex1.OffsetField = ['POINTS', 'S']
    #Extracting data from the Filter
    #output_morse_vtk = 'TTK_Outputs/morseoutput.vtk'
    # Save the output of the TTKMergeandContourTreeFTM filter
    #SaveData(output_morse_vtk, proxy=tTKMorseSmaleComplex1)
    # Export the view to a CSV file - In this case, an error occured to generate the CSV file so we will export as a vtk file 
    #vtk_reader2 = LegacyVTKReader(FileNames=[output_morse_vtk])
    #csv_file_path2 = 'TTK_Outputs/output_morse.csv'
    #SaveData(csv_file_path2, proxy=vtk_reader2)

    # create a new 'TTK Reeb graph (FTR)'
    #tTKReebgraphFTR1 = TTKReebgraphFTR(registrationName='TTKReebgraphFTR1', Input=delaunay2D1)
    #tTKReebgraphFTR1.ScalarField = ['POINTS', 'S']
    #tTKReebgraphFTR1.InputOffsetField = ['POINTS', 'S']
    #Extracting data from the Filter
    #output_reeb = 'TTK_Outputs/reeboutput.csv'
    # Save the output of the TTKMergeandContourTreeFTM filter
    #SaveData(output_reeb, proxy=tTKReebgraphFTR1)

    # Load the CSV file
    csv_file = 'TTK_Outputs/scalarfieldcroutput.csv'
    df = pd.read_csv(csv_file)

    # Define a function to classify the 'CriticalType'
    def classify_critical_type(row):
        if row['CriticalType'] == 0:
            return 'Local Minimum'
        elif row['CriticalType'] == 1:
            return 'Saddle Type 1'
        elif row['CriticalType'] == 2:
            return 'Saddle Type 2'
        elif row['CriticalType'] == 3:
            return 'Local Maximum'
        elif row['CriticalType'] == 4:
            return 'Degenerate'
        elif row['CriticalType'] == 5:
            return 'Regular'
        else:
            return 'Unknown'

    # Apply the classification function to the 'CriticalType' column
    df['Classification'] = df.apply(classify_critical_type, axis=1)

    # Save the modified DataFrame to the CSV file
    output_csv_file = 'TTK_Outputs/scalarfieldcroutputClass.csv'
    df.to_csv(output_csv_file, index=False)
    # Print counts of maxima, minima, and saddle points
    maxima_count = df[df['Classification'] == 'Local Maximum'].shape[0]
    minima_count = df[df['Classification'] == 'Local Minimum'].shape[0]
    saddle_count = df[(df['Classification'] == 'Saddle Type 1') | (df['Classification'] == 'Saddle Type 2')].shape[0]

    print(f"Number of Local Maxima: {maxima_count}")
    print(f"Number of Local Minima: {minima_count}")
    print(f"Number of Saddle Points: {saddle_count}")
    

if __name__ == "__main__":
    if len(sys.argv) != 6:
        print("Usage: pvpython code.py <csv_file> <isovalue1> <isovalue2> <isovalue3> <output_filename>")
        sys.exit(1)

    csv_file = sys.argv[1]
    isovalue1 = float(sys.argv[2])
    isovalue2 = float(sys.argv[3])
    isovalue3 = float(sys.argv[4])
    output_filename = sys.argv[5]

    generate_isocontours(csv_file, isovalue1, isovalue2, isovalue3, output_filename)


    
