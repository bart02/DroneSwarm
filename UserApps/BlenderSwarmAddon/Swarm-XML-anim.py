import os
import bpy
import math
import time
from bpy_extras.io_utils import ExportHelper
from bpy.props import StringProperty, BoolProperty, FloatProperty

bl_info = {
    "name": "Export > Drone Swarm animation Export(.xml)",
    "author": "Richard Bartlett, MCampagnini",
    "version": (2, 5, 1),
    "blender": (2, 6, 3),
    "api": 36079,
    "location": "File > Export > Drone Swarm animation Export(.xml)",
    "description": "Export > Drone Swarm animation Export(.xml)",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Import-Export"
}




class ExportXml(bpy.types.Operator, ExportHelper):
    bl_idname = "export.xml"
    bl_label = "Export"
    filename_ext = ".xml"
    filter_glob = StringProperty(default="*.xml", options={'HIDDEN'})

    filepath = StringProperty(
        name="File Path",
        description="File path used for exporting the xml file",
        maxlen=1024,
        default="")

    def execute(self, context):
        save_chan(context, self.filepath)
        return {'FINISHED'}


def menu_func(self, context):
    self.layout.operator(ExportXml.bl_idname, text="Drone Swarm Exporter (.xml)")


def register():
    bpy.utils.register_class(ExportXml)
    bpy.types.INFO_MT_file_export.append(menu_func)


def unregister():
    bpy.utils.unregister_class(ExportXml)
    bpy.types.INFO_MT_file_export.remove(menu_func)

def save_chan(context, filepath):
    filehandle = open(filepath, 'w')
    fw = filehandle.write
    fw('<DroneSwarm>\n')

    scene = context.scene
    obj = context.visible_objects


    f_start = scene.frame_start
    f_end = scene.frame_end

    # fw(str(obj))
    # iterate the frames
    for frame in range(f_start, f_end + 1, 1):

        if frame % 30 == 0:
            fw('\t<time t=\"'+str(frame/30)+'\">\n')

            for o in range(len(obj)):
                myMaterials = obj[o].data.materials

                for material in myMaterials:

                    fw('\t\t<copter n=\"' + str(o+1) + '\">\n')
                    scene.frame_set(frame)

                    mat = obj[o].matrix_world.copy()

                    t = mat.to_translation()
                    m=[]
                    for u in range(3):
                        m.append(int(material.diffuse_color[u]*255))
                    print(str(m))
                    fw("\t\t\t<reach x=\"%f\" y=\"%f\" z=\"%f\"/>\n" % t[:])
                    fw("\t\t\t<led mode=\"fill\" r=\"%i\" g=\"%i\" b=\"%i\"/>\n" % (m[0], m[1], m[2]))

                    fw('\t\t</copter>\n')
            fw('\t</time>\n')
    # after the whole loop close the file

    fw('</DroneSwarm>')
    filehandle.close()

    return {'FINISHED'}


if __name__ == "__main__":
    register()

"""Code by Alexandr Osherov 9B class phone- +79251834732 email - allexandr2001@mail.ru"""
