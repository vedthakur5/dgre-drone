import sensor_msgs.point_cloud2 as pc2
def on_scan(self, scan):
    rospy.loginfo("Got scan, projecting")
    cloud = self.laser_projector.projectLaser(scan)
    gen = pc2.read_points(cloud, skip_nans=True, field_names=("x", "y", "z"))
    self.xyz_generator = gen
