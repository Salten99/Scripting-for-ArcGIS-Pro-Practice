import arcpy

arcpy.env.workspace = r"C:\Users\samue\Downloads\PythonStart\PythonStart"
arcpy.env.overwriteOutput = True

zones = r"C:\Users\samue\Downloads\PythonStart\PythonStart\fire_zones.shp"
points = r"C:\Users\samue\Downloads\PythonStart\PythonStart\ambulances.shp"

ambulance_count = r"C:\Users\samue\Downloads\PythonStart\PythonStart\ambulance_count.shp"
arcpy.analysis.SpatialJoin(
    target_features=zones,
    join_features=points,
    out_feature_class=ambulance_count,
    join_operation="JOIN_ONE_TO_ONE",
    join_type="KEEP_ALL",
    match_option="INTERSECT"
)
import arcpy.mp
aprx = arcpy.mp.ArcGISProject("CURRENT")
map_obj = aprx.listMaps("Map")[0]
layer = map_obj.listLayers("ambulance_count")
layer = map_obj.listLayers("ambulance_count")[0]
symbology = layer.symbology
symbology.updateRenderer('GraduatedColorsRenderer')
symbology.renderer.field = 'Join_Count'
color_ramp = arcpy.mp.ColorRamp
layer.symbology=symbology
aprx.save()
