import requests

"""

Reference  :https://medium.com/@suneandreasdybrodebel/pythonic-dependency-injection-a-practical-guide-83a1b1299280

In this example the RobotControls class implicitly depends on an abstract interface that defines a send_command method. 
Since RobotControls doesn’t use any imports but instead receives this dependency through its constructor, 
we rather grandiosely say that the dependency is injected.
"""


class RobotApi:
    url = 'http://robot-api.com'

    def send_command(self, command, data):
        formatted_url = f'{self.url}/{command}'
        requests.post(formatted_url, data=data)


class RobotControls:
    def __init__(self, api):
        self.api = api

    def move_west(self):
        self.api.send_command('move_west', data={'meters': 1})

    def move_east(self):
        self.api.send_command('move_east', data={'meters': 1})

    def move_north(self):
        self.api.send_command('move_north', data={'meters': 1})

    def move_south(self):
        self.api.send_command('move_south', data={'meters': 1})


########################################################################

# The main disadvantage of injecting dependencies through __init__ is that it requires us to construct an object that has a send_command method before we can instantiate a RobotControls.
# This may not seem like a huge problem in our example,
# but consider the case when we want to inject RobotControls in a new class,
# and we want to inject that class as a dependency in another class and so on and so on.
# Take for example our FenceGuardingRobot class

"""
In order to instantiate this class, we now have to write:
fence_guarding_robot = FenceGuardingRobot(RobotControls(RobotApi()))
"""


class FenceGuardingRobot:
    fence_length = 20

    def __init__(self, robot_controls):
        self.robot_controls = robot_controls

    def guard(self):
        for _ in range(self.fence_length):
            self.robot_controls.move_north()
        for _ in range(self.fence_length):
            self.robot_controls.move_south()


########################################################################

"""
We can of course use default parameter values to reduce this problem,
but then you run the risk of programming against concretions rather than abstractions

One way of avoiding this pain is by using a pattern built around the super keyword in Python.
"""


class RobotApi:
    url = 'http://robot-api.com'

    def send_command(self, command, data):
        formatted_url = f'{self.url}/{command}'
        requests.post(formatted_url, data=data)


class RobotControls(RobotApi):
    def move_west(self):
        super().send_command('move_west', data={'meters': 1})

    def move_east(self):
        super().send_command('move_east', data={'meters': 1})

    def move_north(self):
        super().send_command('move_north', data={'meters': 1})

    def move_south(self):
        super().send_command('move_south', data={'meters': 1})


class FenceGuardingRobot(RobotControls):
    fence_length = 20

    def guard(self):
        for _ in range(self.fence_length):
            super().move_north()
        for _ in range(self.fence_length):
            super().move_south()
