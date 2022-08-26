from re import X
import rospy
from sensor_msgs.msg import Joy
from std_msgs.msg import Float32, Int32


class Dualshock:
    def __init__(self):
        rospy.init_node('dualshock_to_mavros')

        rospy.Subscriber('/joy', Joy, self.callback, tcp_nodelay=False)

        rospy.spin()

    def callback(self, msg):
        axes = msg.axes
        but = msg.buttons

        x, o, tri, square, direc_left, direc_right, direc_up, direc_down, l3, r3, options, share, l1, r1, touchpad_button, ps, l2_total, r2_total = but[
            3], but[2], but[1], but[0], but[14], but[16], but[15], but[17], but[12], but[13], but[9], but[8], but[4], but[6], but[11], but[10], but[5], but[7]

        l_vert, l_hor, r_vert, r_hor, l2, r2 = axes[1], axes[0], axes[3], axes[2], axes[4], axes[5]

        


if __name__ == '__main__':
    loop = Dualshock()
