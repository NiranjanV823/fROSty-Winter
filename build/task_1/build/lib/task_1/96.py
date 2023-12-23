import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class ObstacleAvoidanceNode(Node):
    def __init__(self):
        super().__init__('obstacle_avoidance_node')
        self.cmd_vel_pub = self.create_publisher(Twist, '/cmd_vel', 10)
        self.create_subscription(LaserScan, '/lidar', self.lidar_callback, 10)
        self.rate = self.create_rate(10)  

        self.max_linear_speed = 0.5
        self.max_angular_speed = 0.5
        self.min_dist_to_obstacle = 0.5

    def lidar_callback(self, data):
        # Process lidar data and perform obstacle avoidance
        ranges = data.ranges
        min_distance = min(ranges)

        if min_distance < self.min_dist_to_obstacle:
            # Obstacle detected, perform avoidance
            self.avoid_obstacle()
        else:
            # No obstacle, move forward
            self.move_forward()

    def avoid_obstacle(self):
        # Simple avoidance strategy: turn around
        twist_cmd = Twist()
        twist_cmd.linear.x = 0.0
        twist_cmd.angular.z = self.max_angular_speed
        self.cmd_vel_pub.publish(twist_cmd)

    def move_forward(self):
        # Move forward
        twist_cmd = Twist()
        twist_cmd.linear.x = self.max_linear_speed
        twist_cmd.angular.z = 0.0
        self.cmd_vel_pub.publish(twist_cmd)

    def run(self):
        while rclpy.ok():
            rclpy.spin_once(self)
            self.rate.sleep()

    def shutdown(self):
        # Stop the robot when shutting down the node
        self.get_logger().info("Stopping the robot...")
        twist_cmd = Twist()
        self.cmd_vel_pub.publish(twist_cmd)
        rclpy.shutdown()

def main(args=None):
    rclpy.init(args=args)
    try:
        avoidance_node = ObstacleAvoidanceNode()
        avoidance_node.run()
    except Exception as e:
        avoidance_node.get_logger().info(f"Error in obstacle avoidance node: {e}")
    finally:
        avoidance_node.shutdown()

if __name__ == '__main__':
    main()
