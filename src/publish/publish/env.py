import rclpy
import os
from rclpy.node import Node

class cls(Node):

    def __init__(self):
        super().__init__('env')
        os.system("ign gazebo /home/ubuntu/ign_ws/src/publish/publish/model/diff_drive.sdf")
    

def main(args=None):
    rclpy.init(args=args)
    minimal = cls()
    rclpy.spin(minimal)
    rclpy.shutdown()
if __name__ == '__main__':
    main()