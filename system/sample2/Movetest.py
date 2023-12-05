#! /usr/bin/env python3
  
import rospy
from std_msgs.msg import Int8,String
from geometry_msgs.msg import Twist,Pose,PoseStamped
from turtlesim.msg import Pose
import yaml
import rospkg
import tf
import actionlib
from actionlib_msgs.msg import *
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal


with open('/home/rsdlab/catkin_ws/src/seed_r7_ros_pkg/seed_r7_navigation/maps/waypoints_seed.yaml', 'r') as yml:
    config = yaml.safe_load(yml)
  
def finish():
    rospy.loginfo("案内完了")
    rospy.loginfo("目的地を設定してください")

class NaviAction:
  ## @brief コンストラクタ。waypointsの読込とmove_baseのアクションクライアントの定義
  def __init__(self):
    #rospack = rospkg.RosPack()
    #rospack.list() 
    #self.path = rospack.get_path('task_programmer')
    ## @brief /move_baseアクションクライアント
    self.ac = actionlib.SimpleActionClient('move_base', MoveBaseAction)
    while not self.ac.wait_for_server(rospy.Duration(5)):
      rospy.loginfo("Waiting for the move_base action server to come up")
    rospy.loginfo("The server comes up")
    ## @brief MoveBaseGoal型のゴール
    self.goal = MoveBaseGoal()

    self.vel_pub_ = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    self.vel_ = Twist()
    #RTCへの報告用のtopicの作成
    self.return_ = rospy.Publisher('/return', Int8, queue_size=1)
    self.msg = Int8()


  ## @brief ゴールポジションの設定と移動の開始
  # @param _number waypointsの番号(0以上の数値）
  # @return ゴールに到着したか否か（succeeded or aborted）
  def set_goal(self,_number):
    #rospy.on_shutdown(self.shutdown)

    rev = dict(config[_number])

    self.goal.target_pose.header.frame_id = 'map'
    self.goal.target_pose.header.stamp = rospy.Time.now()
    self.goal.target_pose.pose.position.x = rev['pose']['position']['x']
    self.goal.target_pose.pose.position.y = rev['pose']['position']['y']
    self.goal.target_pose.pose.position.z = rev['pose']['position']['z']
    self.goal.target_pose.pose.orientation.x = rev['pose']['orientation']['x']
    self.goal.target_pose.pose.orientation.y = rev['pose']['orientation']['y']
    self.goal.target_pose.pose.orientation.z = rev['pose']['orientation']['z']
    self.goal.target_pose.pose.orientation.w = rev['pose']['orientation']['w']


    rospy.loginfo('Sending goal')
    rospy.loginfo('Sending...')
    self.ac.send_goal(self.goal)
    succeeded = self.ac.wait_for_result(rospy.Duration(60))
    state = self.ac.get_state()
    if succeeded:
      rospy.loginfo("Succeed")
      self.return_.publish(0)
      finish()
      return 'succeeded'
    else:
      rospy.loginfo("Failed")
      return 'aborted'




def root(data):
    rospy.loginfo(data.data)
    na=NaviAction()
    na.set_goal(data.data)


if __name__ == '__main__':
    
    rospy.sleep(5)
    
    rospy.init_node('move_robot')


    while not rospy.is_shutdown():

        rospy.loginfo("目的地を設定してください")
        rospy.Subscriber("/ppp",Int8, root)
        rospy.spin()
   
  
