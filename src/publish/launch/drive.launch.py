import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess, IncludeLaunchDescription
from launch.actions import RegisterEventHandler
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    config = os.path.join(
        get_package_share_directory('publish'),
        'config',
        'params.yaml'
    )
    return LaunchDescription([

        #IncludeLaunchDescription(
         #  PythonLaunchDescriptionSource(
          #      [os.path.join(get_package_share_directory('publish'),
          #                    'launch', 'ign_gazebo.launch.py')]),
          #  launch_arguments=[('ign_args', [' -r -v 4 diff_drive.sdf'])]),
   
        #Node(
        #package='ros_ign_gazebo',
        #executable='create',
        #output='screen',
        #arguments=['-string', doc.toxml(),
                  # '-name', 'cartpole',
                  # '-allow_renaming', 'true'],
       # ),
        Node(
            package='publish',
            executable='env',
            name='simulation'
        ),
        Node(
            package='ros_ign_bridge',
            executable='parameter_bridge',
            arguments=['/model/vehicle_blue/cmd_vel@geometry_msgs/msg/Twist@ignition.msgs.Twist'],
            output='screen'
        ),
        Node(
            package='publish',
            executable='publisher',
            parameters=[config],
            output='screen',
            emulate_tty=True
        ),
    ])

        # Node(
        #     package='my_pkg',
        #     executable='test_params_rclpy',
        #     parameters=[config],
        #     output='screen',
        #     emulate_tty=True
        # )
          # Node(
      #      package='turtlesim',
       #     namespace='turtlesim1',
        #    executable='turtlesim_node',
         #   name='sim'
        #),
       # Node(
        #package='ros_ign_gazebo',
        #executable='create',
        ##output='screen',
        #arguments=['-string', doc.toxml(),
         #          '-name', 'cartpole',
          #         '-allow_renaming', 'true'],
       # ),
    