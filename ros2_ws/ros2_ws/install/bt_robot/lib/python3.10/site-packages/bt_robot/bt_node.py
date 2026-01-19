import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class BTRobot(Node):
    def __init__(self):
        super().__init__('bt_robot')
        self.front_distance = 10.0  # default jauh

        # Subscriber Lidar
        self.sub = self.create_subscription(
            LaserScan,
            '/scan',
            self.laser_callback,
            10
        )

        # Publisher Twist
        self.pub = self.create_publisher(
            Twist,
            '/cmd_vel',
            10
        )

        # Timer untuk behavior
        self.timer = self.create_timer(0.1, self.behavior)

    def laser_callback(self, msg: LaserScan):
        """
        Ambil rata-rata jarak di depan robot untuk menghindari noise.
        Asumsi: indeks tengah dari msg.ranges adalah depan.
        """
        num_points = len(msg.ranges)
        # Ambil 10 titik di tengah (depan)
        front_angles = msg.ranges[num_points//2 - 5 : num_points//2 + 5]

        # Buang nilai 0.0 (noise) dan ekstrem
        valid_ranges = [d for d in front_angles if d > 0.05]

        if valid_ranges:
            # rata-rata jarak depan
            self.front_distance = sum(valid_ranges) / len(valid_ranges)
        else:
            self.front_distance = 10.0  # default jauh

    def behavior(self):
        """
        Robot maju jika jarak depan > threshold,
        belok jika ada halangan di depan.
        """
        cmd = Twist()
        threshold = 0.5  # jarak minimum sebelum belok

        # Debug jarak depan
        self.get_logger().info(f'Front distance: {self.front_distance:.2f} m')

        if self.front_distance < threshold:
            # Belok ke kiri
            cmd.angular.z = 0.5
            cmd.linear.x = 0.0
        else:
            # Maju lurus
            cmd.linear.x = 0.2
            cmd.angular.z = 0.0

        self.pub.publish(cmd)

def main():
    rclpy.init()
    node = BTRobot()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
