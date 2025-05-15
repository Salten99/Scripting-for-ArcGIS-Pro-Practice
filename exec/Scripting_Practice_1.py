import arcpy
#set environment workspace#
arcpy.env.workspace = r"C:\Users\samue\Downloads\PythonStart\PythonStart"
arcpy.env.overwriteOutput = True
#input feature classes
zones = r"C:\Users\samue\Downloads\PythonStart\PythonStart\fire_zones.shp"
points = r"C:\Users\samue\Downloads\PythonStart\PythonStart\ambulances.shp"
#output feature class
arcpy.analysis.SpatialJoin()
﻿Traceback (most recent call last):
﻿  File "<string>", line 1, in <module>
﻿  File "C:\Users\samue\AppData\Local\Programs\ArcGIS\Pro\Resources\ArcPy\arcpy\analysis.py", line 1020, in SpatialJoin
﻿    raise e
﻿  File "C:\Users\samue\AppData\Local\Programs\ArcGIS\Pro\Resources\ArcPy\arcpy\analysis.py", line 1000, in SpatialJoin
﻿    gp.SpatialJoin_analysis(
﻿  File "C:\Users\samue\AppData\Local\Programs\ArcGIS\Pro\Resources\ArcPy\arcpy\geoprocessing\_base.py", line 532, in <lambda>
﻿    return lambda *args: val(*gp_fixargs(args, True))
﻿                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
﻿arcgisscripting.ExecuteError: Failed to execute. Parameters are not valid.
 ERROR 000735: Target Features: Value is required
 ERROR 000735: Join Features: Value is required
 ERROR 000669: output Output Feature Class is same as overlay Join Features
Failed to execute (SpatialJoin).

arcpy.analysis.SpatialJoin(
    target_features=zones,
    join_features=points,
    out_feature_class=ambulance_count,
    join_operation="JOIN_ONE_TO_ONE",
    join_type="KEEP_ALL",
    match_option="INTERSECT"
)
﻿Traceback (most recent call last):
﻿  File "<string>", line 4, in <module>
﻿NameError: name 'ambulance_count' is not defined
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
symbology.updateRenderer('GraduatedColors')
﻿Traceback (most recent call last):
﻿  File "<string>", line 1, in <module>
﻿  File "C:\Users\samue\AppData\Local\Programs\ArcGIS\Pro\Resources\ArcPy\arcpy\utils.py", line 154, in fn_
﻿    raise ValueError(
﻿ValueError: Invalid value for renderer_name: 'GRADUATEDCOLORS' (choices are: ['SimpleRenderer', 'GraduatedColorsRenderer', 'GraduatedSymbolsRenderer', 'UniqueValueRenderer', 'UnclassedColorsRenderer'])
symbology.updateRenderer('GraduatedColorsRenderer')
symbology.renderer.field = 'Join_Count'
symbology.renderer.classBreaks[0].symbol.color = [255, 0, 0]
﻿Traceback (most recent call last):
﻿  File "C:\Users\samue\AppData\Local\Programs\ArcGIS\Pro\Resources\ArcPy\arcpy\arcobjects\_base.py", line 99, in _set
﻿    return setattr(self._arc_object, attr_name, cval(val))
﻿           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
﻿AttributeError: can't set attribute
﻿
﻿During handling of the above exception, another exception occurred:
﻿
﻿Traceback (most recent call last):
﻿  File "<string>", line 1, in <module>
﻿  File "C:\Users\samue\AppData\Local\Programs\ArcGIS\Pro\Resources\ArcPy\arcpy\arcobjects\_base.py", line 102, in _set
﻿    raise NameError(
﻿NameError: The attribute 'color' is not supported on this instance of Symbol.
color_ramp=arcpy.mp.ListColorRamps("Inferno")[0]
﻿Traceback (most recent call last):
﻿  File "<string>", line 1, in <module>
﻿AttributeError: module 'arcpy.mp' has no attribute 'ListColorRamps'
color_ramp = arcpy.mp.ColorRamp("Inferno")[0]
﻿Traceback (most recent call last):
﻿  File "<string>", line 1, in <module>
﻿TypeError: 'ColorRamp' object is not subscriptable
color_ramp = arcpy.mp.ColorRamp[0]
﻿Traceback (most recent call last):
﻿  File "<string>", line 1, in <module>
﻿TypeError: type 'ColorRamp' is not subscriptable
color_ramp = arcpy.mp.ColorRamp
color_ramp=color_ramp[0]
﻿Traceback (most recent call last):
﻿  File "<string>", line 1, in <module>
﻿TypeError: type 'ColorRamp' is not subscriptable
layer.symbology=symbology
aprx.save()
