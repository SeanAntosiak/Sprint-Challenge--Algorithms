class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def sort(self):
        # breaking the rule
        sorting = 1
        self.swap_item()
        while sorting == 1:
            while self.light_is_on() is False:
                if self.compare_item() == -1:
                    self.swap_item()

                if self.can_move_right():
                    self.move_right()
                else:
                    self.set_light_on()

            while self.light_is_on():
                if self.compare_item() == 1:
                    self.swap_item()

                if self.can_move_left() and (self.compare_item() is not None):
                    self.move_left()
                elif self.compare_item() is None:
                    self.swap_item()
                    if self.can_move_right():
                        self.move_right()
                        self.swap_item()
                        self.set_light_off()
                    else:
                        sorting = 0  # list is now sorted
                        self.set_light_off()



if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)


# ### plan ###
# have the robot move right until check move right is false
# pick up the item when the robot can no longer move right
# move left and check if it is smaller, if yes swap
# continue moving left and check/swaping for lower values until the robot cant move left
# once the robot cant move left turn the light on
# while light is on check values and if the held object is smaller swap else move right
# once an item is swapped turn the light off
#  BAD PLAN NVM

# ### plan 2 ###
# while light is off check values, if -1 swap
# check if you can move right , if you can do so
# if cant move right AND check != -1  swap item and turn light on
# while light on check values if 1 swap
# check move left, if you can do it
# if cant move left AND check values = -1 swap and turn light off
#
# Problems !!
# when to stop
# how to deal with none object (maybe related on how to stop)
# how to alternate between while loops without another while loop ( which would require a variable) ( could use light for this but then cant use it for choosing direction)


# ### Running out of time plan ###
# ## aka playing with mahjong tiles till it works plan ##
# swap none imediatly so its the first item in the list
# while light off
# check swap
# if -1 swap
# check if move right and move if can
#   if not turn light on
# while light on
# check swap
# if 1 swap
# if cant move left or check is none swap
# move right once and swap. Turn light off and repeat

# if cant move right and swap is none return list

# this works if you can alternate while loops outside of creating a larger while loop
