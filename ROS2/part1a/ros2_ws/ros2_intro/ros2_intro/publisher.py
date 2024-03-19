#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Publisher(Node):

    def __init__(self):
        super().__init__("publisher_node")
        self.std_msgs_pub = self.create_publisher(
            String,
            "/chatter",
            10
        )
        self.timer = self.create_timer(0.1, self.send_text)
        self.get_logger().info("Publisher node started")

    def send_text(self):
        msg = String()
        msg.data = "Hello! ROS2 is fun"
        self.std_msgs_pub.publish(msg)
        self.get_logger().info("Sent data : " + msg.data)


def main(args = None):
    rclpy.init(args=args)
    node = Publisher()
    rclpy.spin(node)
    rclpy.shutdown()