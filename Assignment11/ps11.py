# Problem Set 11: Simulating robots
# Name: Lin Jiang
# Collaborators: None
# Time:

import math
import random
import pylab
import ps11_visualize

# === Provided classes

class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """

    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).

        x: a real number indicating the x-coordinate
        y: a real number indicating the y-coordinate
        """
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self, newx):
        self.x = newx

    def setY(self, newy):
        self.y = newy

    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: integer representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)


# === Problems 1 and 2

class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """

    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.
        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """
        self.width = width
        self.height = height
        self.cleanTile = []
        # Done

    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.
        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        if (int(pos.x), int(pos.y)) not in self.cleanTile:
            self.cleanTile.append((int(pos.x), int(pos.y)))
            # Done

    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        return (m, n) in self.cleanTile
        # Done

    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        return self.width * self.height
        # Done

    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        return len(self.cleanTile)
        # Done

    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        return Position(random.uniform(0, self.width), random.uniform(0, self.height))
        # Done

    def isPositionInRoom(self, pos):
        """
        Return True if POS is inside the room.

        pos: a Position object.
        returns: True if POS is in the room, False otherwise.
        """
        if 0 <= pos.x <= self.width and 0 <= pos.y <= self.height:
            return True
        return False
        # Done


class BaseRobot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in
    the room.  The robot also has a fixed speed.

    Subclasses of BaseRobot should provide movement strategies by
    implementing updatePositionAndClean(), which simulates a single
    time-step.
    """

    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified
        room. The robot initially has a random direction d and a
        random position p in the room.

        The direction d is an integer satisfying 0 <= d < 360; it
        specifies an angle in degrees.

        p is a Position object giving the robot's position.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        self.room = room
        self.s = speed
        self.d = random.randint(0, 359)
        self.p = self.room.getRandomPosition()
        # Done

    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        return self.p
        # Done

    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        return self.d
        # Done

    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        self.p = position
        # Done

    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        self.d = direction
        # Done


class Robot(BaseRobot):
    """
    A Robot is a BaseRobot with the standard movement strategy.

    At each time-step, a Robot attempts to move in its current
    direction; when it hits a wall, it chooses a new direction
    randomly.
    """

    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        # newPos = self.getRobotPosition().getNewPosition(self.getRobotDirection(), self.s)
        # while not self.room.isPositionInRoom(newPos):
        #     self.setRobotDirection(random.randint(0, 359))
        #     newPos = self.getRobotPosition().getNewPosition(self.getRobotDirection(), self.s)
        # self.setRobotPosition(newPos)
        # self.room.cleanTileAtPosition(self.getRobotPosition())


        upper = 359
        lower = 0
        if self.s <= 1:
            newPos = self.getRobotPosition().getNewPosition(self.getRobotDirection(), self.s)
            while not self.room.isPositionInRoom(newPos):
                self.setRobotDirection(random.randint(lower, upper))
                newPos = self.getRobotPosition().getNewPosition(self.getRobotDirection(), self.s)
            self.setRobotPosition(newPos)
            self.room.cleanTileAtPosition(self.getRobotPosition())
        else:
            speed = self.s
            while speed > 1:
                newPos = self.getRobotPosition().getNewPosition(self.getRobotDirection(), 1)
                while not self.room.isPositionInRoom(newPos):
                    self.setRobotDirection(random.randint(lower, upper))
                    newPos = self.getRobotPosition().getNewPosition(self.getRobotDirection(), 1)
                self.setRobotPosition(newPos)
                self.room.cleanTileAtPosition(self.getRobotPosition())
                speed -= 1
            newPos = self.getRobotPosition().getNewPosition(self.getRobotDirection(), speed)
            while not self.room.isPositionInRoom(newPos):
                self.setRobotDirection(random.randint(lower, upper))
                newPos = self.getRobotPosition().getNewPosition(self.getRobotDirection(), speed)
            self.setRobotPosition(newPos)
            self.room.cleanTileAtPosition(self.getRobotPosition())

        # Done


# room = RectangularRoom(2, 2)
# r = Robot(room, 1)
# print r.getRobotPosition().getX(), r.getRobotPosition().getX()
# r.updatePositionAndClean()
# print r.getRobotPosition().getX(), r.getRobotPosition().getY()

# === Problem 3

def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type, visualize):
    """
    Runs NUM_TRIALS trials of the simulation and returns a list of
    lists, one per trial. The list for a trial has an element for each
    timestep of that trial, the value of which is the percentage of
    the room that is clean after that timestep. Each trial stops when
    MIN_COVERAGE of the room is clean.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE,
    each with speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    Visualization is turned on when boolean VISUALIZE is set to True.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. Robot or
                RandomWalkRobot)
    visualize: a boolean (True to turn on visualization)
    """

    trialLists = []
    for trial in range(num_trials):
        if visualize:
            anim = ps11_visualize.RobotVisualization(num_robots, width, height, 1)
        room = RectangularRoom(width, height)
        coverage = 0
        robotList = []
        cleanPercent = []
        for i in range(num_robots):
            robotList.append(robot_type(room, speed))
        while coverage < min_coverage:
            for i in range(num_robots):
                robotList[i].updatePositionAndClean()
            if visualize:
                anim.update(room, robotList)
            coverage = round(float(room.getNumCleanedTiles()) / room.getNumTiles(), 3)
            cleanPercent.append(coverage)
        trialLists.append(cleanPercent)
    return trialLists

    # Done

# runSimulation(2, 3.0, 10, 10, 0.5, 1, Robot, True)


def simulationOutcome(num_robots, speed, width, height, min_coverage, num_trials, robot_type, visualize):
    outcome = runSimulation(num_robots, speed, width, height, min_coverage, num_trials, robot_type, visualize)
    tot = 0
    for trial in outcome:
        tot += len(trial)
    ticks = float(tot)/num_trials
    if num_robots == 1:
        print 'One robot takes around %d clock ticks to clean %2d%% of a %dx%d room. ' % (ticks, min_coverage*100, width, height)
    else:
        print '%d robots take around %d clock ticks to clean %2d%% of a %dx%d room. ' % (num_robots, ticks, min_coverage * 100, width, height)


# width = 10
# height = 10
# room = RectangularRoom(width, height)
# runSimulation(1, 3.3, width, height, 0.7, 1, Robot, True)
# simulationOutcome(1, 1.0, width, height, 0.75, 1000, Robot, False)
# robots = [Robot(room, 1.0), Robot(room, 1.0)]


# for l in avg:
#     print avg.index(l), " : ", l
# simulationOutcome(2, 1.4, 10, 10, 0.75, 30, Robot, False)

# === Provided function



def computeMeans(list_of_lists):
    """
    Returns a list as long as the longest list in LIST_OF_LISTS, where
    the value at index i is the average of the values at index i in
    all of LIST_OF_LISTS' lists.

    Lists shorter than the longest list are padded with their final
    value to be the same length.
    """
    # Find length of longest list
    longest = 0
    for lst in list_of_lists:
        if len(lst) > longest:
            longest = len(lst)
    # Get totals
    tots = [0] * (longest)
    for lst in list_of_lists:
        for i in range(longest):
            if i < len(lst):
                tots[i] += lst[i]
            else:
                tots[i] += lst[-1]
    # Convert tots to an array to make averaging across each index easier
    tots = pylab.array(tots)
    # Compute means
    means = tots / float(len(list_of_lists))
    return means


# === Problem 4
def meanTimeCalc(num_robots, speed, width, height, min_coverage, num_trials,
                  Robot, False):
    trialLists = runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                               Robot, False)
    tot = 0
    for trial in trialLists:
        tot += len(trial)
    timeStep = float(tot) / num_trials
    return timeStep


def showPlot1():
    """
    Produces a plot showing dependence of cleaning time on room size.
    """
    # Done
    # roomArea, meanTime = simulation1(1, 1.0, 5, 25, 0.75, 50)
    meanTime = []
    roomArea = []
    for width in range(5, 26):
        meanTime.append(meanTimeCalc(1, 1.0, width, width, 0.75, 10, Robot, False))
        roomArea.append(width*width)
    pylab.figure()
    pylab.plot(roomArea, meanTime)
    pylab.ylabel('Timesteps')
    pylab.xlabel('Room area')
    pylab.title('Time to clean 75% of a square room with 1 robot, for various room sizes')
    pylab.show()

# showPlot1()

def showPlot2():
    """
    Produces a plot showing dependence of cleaning time on number of robots.
    """
    # Done
    meanTime = []
    robotNum = []
    for num_robots in range(1, 11):
        meanTime.append(meanTimeCalc(num_robots, 1.0, 25, 25, 0.75, 50, Robot, False))
        robotNum.append(num_robots)
    pylab.figure()
    pylab.plot(robotNum, meanTime)
    pylab.ylabel('Timesteps')
    pylab.xlabel('Number of robots')
    pylab.title('Time to clean 75% of a 25*25 square room with various numbers of robots')
    pylab.show()

# showPlot2()


def showPlot3():
    """
    Produces a plot showing dependence of cleaning time on room shape.
    """
    # Done
    room = [(20, 20), (25, 16), (40, 10), (50, 8), (80, 5), (100, 4)]
    meanTime = []
    shape = [float(w)/h for w, h in room]
    for w, h in room:
        meanTime.append(meanTimeCalc(2, 1.0, w, h, 0.75, 1000, Robot, False))
    pylab.figure()
    pylab.plot(shape, meanTime)
    pylab.ylabel('Timesteps')
    pylab.xlabel('Width to height ratio')
    pylab.title('Time to clean 75% of a room of area 400 with 2 robots, for various room shapes')
    pylab.show()

# showPlot3()


def showPlot4():
    """
    Produces a plot showing cleaning time vs. percentage cleaned, for
    each of 1-5 robots.
    """
    # Done
    minCover = pylab.np.linspace(0.1, 1.0, 10)
    pylab.figure()
    pylab.ylabel('Timesteps')
    pylab.xlabel('Minimum coverage ')
    pylab.title('Time to clean 75% of a 25*25 room of with 1-5 robots, for various minimum coverage')
    for num in range(1, 6):
        meanTime = []
        for cover in minCover:
            meanTime.append(meanTimeCalc(num, 1.0, 25, 25, cover, 10, Robot, False))
        pylab.plot(minCover, meanTime, label='%d robots' % num)
    pylab.legend(loc='upper left')
    pylab.show()

# showPlot4()

# === Problem 5

class RandomWalkRobot(BaseRobot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement
    strategy: it chooses a new direction at random after each
    time-step.
    """
    # Done
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        upper = 359
        lower = 0
        if self.s <= 1:
            newPos = self.getRobotPosition().getNewPosition(self.getRobotDirection(), self.s)
            while not self.room.isPositionInRoom(newPos):
                self.setRobotDirection(random.randint(lower, upper))
                newPos = self.getRobotPosition().getNewPosition(self.getRobotDirection(), self.s)
            self.setRobotPosition(newPos)
            self.room.cleanTileAtPosition(self.getRobotPosition())
        else:
            speed = self.s
            while speed > 1:
                newPos = self.getRobotPosition().getNewPosition(self.getRobotDirection(), 1)
                while not self.room.isPositionInRoom(newPos):
                    self.setRobotDirection(random.randint(lower, upper))
                    newPos = self.getRobotPosition().getNewPosition(self.getRobotDirection(), 1)
                self.setRobotPosition(newPos)
                self.room.cleanTileAtPosition(self.getRobotPosition())
                speed -= 1
            newPos = self.getRobotPosition().getNewPosition(self.getRobotDirection(), speed)
            while not self.room.isPositionInRoom(newPos):
                self.setRobotDirection(random.randint(lower, upper))
                newPos = self.getRobotPosition().getNewPosition(self.getRobotDirection(), speed)
            self.setRobotPosition(newPos)
            self.room.cleanTileAtPosition(self.getRobotPosition())
        self.setRobotDirection(random.randint(lower, upper))

# runSimulation(1, 3.0, 10, 10, 0.7, 1, RandomWalkRobot, True)


# === Problem 6

def showPlot5():
    """
    Produces a plot comparing the two robot strategies.
    """
    # TODO: Your code goes here
    roomArea = [w*w for w in range(5, 26)]
    robot_type = [Robot, RandomWalkRobot]
    pylab.figure()
    pylab.ylabel('Timesteps')
    pylab.xlabel('Room area')
    pylab.title('Time to clean 75% of a square room with 1 base robot or random walk robot, for various room sizes')
    for r in robot_type:
        meanTime = []
        for width in range(5, 26):
            meanTime.append(meanTimeCalc(1, 1.0, width, width, 0.75, 100, r, False))
        if r is Robot:
            tag = 'Basic robot'
        else: tag = 'Random walk robot'
        pylab.plot(roomArea, meanTime, label= tag)
    pylab.legend(loc='upper left')
    pylab.show()

# showPlot5()