#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Subscriber(Node):

    def __init__(self):
        super().__init__("subscriber_node")
        self.std_msgs_pub = self.create_subscription(
            String,
            "/chatter",
            self.data_received_callback,
            10
        )
        self.get_logger().info("Subscriber node started")

    def data_received_callback(self, msg : String):
        self.get_logger().info("Received data : " + msg.data)


def main(args = None):
    rclpy.init(args=args)
    node = Subscriber()
    rclpy.spin(node)
    rclpy.shutdown()