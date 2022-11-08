
#!/usr/bin/env python3
import rospy
import odrive
from std_msgs.msg import Float32
setpoint =0

def odriveControl():
    odrv0 = odrive.find_any(serial_number="208737963548")
    axis0 = odrv0.axis0
    axis0.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL
    axis0.controller.config.input_filter_bandwidth = 2.0
    axis0.controller.config.input_mode = INPUT_MODE_POS_FILTER
    axis0.controller.input_pos = setpoint

def callback(Setpoint):
    setpoint = Setpoint.data
    odriveControl()
    

def listener():
    rospy.init_node('odrive', anonymous=True)
    rospy.Subscriber("speed", Float32, callback)
    rospy.spin()



if __name__ == '__main__':
    listener()
    


