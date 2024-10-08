import arcpy

def generateMap():
    # access the project
    project = arcpy.mp.ArcGISProject(r"C:\Users\dev\Documents\ArcGIS\Projects\MyProject\MyProject.aprx")

    # access a map
    map = project.listMaps("testMap")[0]

    # get the oblast borders layer
    oblasts = map.listLayers("ukraineOblasts")[0]

    # get the mention data from csv and convert to a table
    headlineCSV = "headlineData.csv"
    tableView = "csv_table_view"
    arcpy.management.MakeTableView(headlineCSV, tableView)

    # join the fields
    arcpy.management.AddJoin(oblasts, "ID_1", tableView, "ID_1")

    # access a layout
    layout = project.listLayouts("testLayout")[0]

    # create a symbology
    sym = oblasts.symbology
    sym.updateRenderer('GraduatedColorsRenderer')
    sym.renderer.classificationField = 'Mentions'

    # options
    sym.renderer.classificationMethod = 'NaturalBreaks'
    sym.renderer.breakCount = 5

    oblasts.symbology = sym

    # refresh
    map.clearSelection()

    # export the layout
    layout.exportToJPEG(r"C:\Users\dev\Desktop\ISWbot\mapExport")

    # delete the project instance
    del project
