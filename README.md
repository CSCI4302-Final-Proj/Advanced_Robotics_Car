# Advanced_Robotics_Car

Please git clone 'carbot' gazebo simulation from lucasw onto your catkin workspace in src.

``` 
git clone https://github.com/lucasw/carbot
```

Afterwards download the nessary dependencies for the controllers

```
sudo apt-get update
sudo apt-get install ros-kinetic-ros-control ros-kinetic-ros-controllers
```

Now compile and source

```
roscd; cd ..;
catkin_make
source devel/setup.bash
```

Now launch the gazebo control file

```
roslaunch carbot_gazebo_control carbot_gazebo_control.launch
```
