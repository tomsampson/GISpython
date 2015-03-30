import arcpy

arcpy.env.workspace = r"C:\Users\tomsampson\Documents\ArcGIS\_analysis\MoyMPW_design_Q2-Q10.gdb"

arcpy.MakeFeatureLayer_management ("QW93TTF1_Outline", "Q10_design_Outline")
fc = "Q10_design_Outline"
split = "Q10_design_Outline_split"
select = "InlandWater"
watercourse = "Western_Merged_AsSurveyed_v2_25102013"
arcpy.MultipartToSinglepart_management (fc, split)
fc = "Q10_design_Outline_split"
outfc = arcpy.Describe(fc).baseName + "_cleaned" #sets output name
arcpy.SelectLayerByLocation_management (fc, "intersect", select)
arcpy.SelectLayerByLocation_management (fc, "intersect", watercourse, "0", "add_to_selection")
arcpy.CopyFeatures_management (fc, outfc)