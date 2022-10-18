import rospy
from std_msgs.msg import Float32
flag =1
lastP = 0
lastAngle = 0
Angle = 0

def callback(angle):
    Angle = filteration(angle.data)
    rospy.loginfo(rospy.get_caller_id() + "angle is %f", Angle)

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("chatter", Float32, callback)
    rospy.spin()

def talker():
    #intializing publisher
    pub = rospy.Publisher('imuAngle', Float32, queue_size=10)
    #intializing node
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        if Angle != 0:
            rospy.loginfo(Angle)
            pub.publish(Angle)
            rate.sleep()

if __name__ == '__main__':
    listener()
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

def filteration(measuredAngle):
    #intial values 
    intialP = 10000
    initialAngle = 0
    
    q = 0.15 #process noise variance
    
    #intiallizing values at first itteration
    if flag == 1:
        lastP = intialP+q
        lastAngle = initialAngle
        flag = 0
    
    
    standardDeviation = 0.1 #standard deviation
    r = standardDeviation  **2 #varience

    #Kalman Gain
    k = lastP/(lastP+r) 

    #State Update
    currentAngle = lastAngle + k*(measuredAngle - lastAngle ) 
    
    #Covariance Update
    currentP = (1-k)*lastP
    
    #State Extrapolation
    nextAngle = currentAngle
    
    #Covariance Extrapolation
    nextP = currentP + q

    #saving values
    lastP = nextP
    lastAngle = nextAngle

    #returning filtered angle
    return currentAngle
