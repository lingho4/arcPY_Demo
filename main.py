# module containing news data retrieval functions
import newsModule
# module containing gis mapping functions
import gisModule
# module containing functions for posting to x
import xModule

# get data from news api and store in spreadsheet
newsModule.retrieveData()

# Join the spreadsheet with shapefile, generate the map and export it
gisModule.generateMap()


# Post map to X
xModule.postMap()