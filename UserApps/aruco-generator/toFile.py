ORIGIN = "local_origin"
ORIGIN_UD = "local_origin_upside_down"

std = '''<launch>
    <remap from="image" to="main_camera/image_raw"/>
    <remap from="camera_info" to="main_camera/camera_info"/>

    <node pkg="nodelet" type="nodelet" name="aruco_pose" args="load aruco_pose/aruco_pose nodelet_manager" clear_params="true">
        <param name="frame_id" value="aruco_map_raw"/> 
        <param name="type" value="gridboard"/>
        <param name="markers_x" value="{0}"/>
        <param name="markers_y" value="{1}"/>
        <param name="first_marker" value="{2}"/>
        <param name="markers_side" value="{3}"/>
        <param name="markers_sep" value="{4}"/>


		<rosparam param="marker_ids">{7}</rosparam>
    </node>

    <node pkg="nodelet" type="nodelet" name="aruco_vpe" args="load clever/aruco_vpe nodelet_manager" clear_params="true">
        <param name="aruco_orientation" value="{6}"/>

        <param name="use_mocap" value="{5}"/>
    </node>
</launch>
'''



def toFile(fn, x, y, first, side, sep, mocap, origin, map):
    if origin:
        origin = "local_origin"
    else:
        origin = "local_origin_upside_down"
    with open(fn, 'w') as f:
        f.write(std.format(x, y, first, side, sep, str(mocap).lower(), origin, map))
