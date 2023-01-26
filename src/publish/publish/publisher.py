import sys
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('publisher')
        self.publisher_ = self.create_publisher(
            Twist, '/model/vehicle_blue/cmd_vel', 1)
        timer_period = 0.5  # seconds
        self.i = 0.0
        self.timer_ = self.create_timer(timer_period, self.publish_message)
        self.declare_parameters(
            namespace='',
            parameters=[
                ('lx', 1.00),
                ('ly', 1.00),
                ('az', 1.00),
            ]
        )

    def publish_message(self):
        message = Twist()
        (lx, ly, az) = self.get_parameters(
            ['lx', 'ly', 'az'])
        message.linear.x = float(lx.value)
        message.angular.z = float(az.value)
        self.get_logger().info('Sending - Linear Velocity : %f, Angular Velocity : %f' %
                               (message.linear.x, message.angular.z))
        self.publisher_.publish(message)
       


def main(args=None):
    rclpy.init(args=args)
    minimal_publisher = MinimalPublisher()
    rclpy.spin(minimal_publisher)
    minimal_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
