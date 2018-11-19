import pandas as pd
from aps_core import *


# create a pd DataFrame for all users to pull ratio details using user name.
class User:
    def __init__(self):
        self.user_name = None
        self.phone_number = None
        self.info = {}
        self.points = {'owed': 0,
                       'given': 0}

        self.shadow_points = {}

        self.shadow_owed = []

        self.contacts = []  # list of user names.
        self.groups = []

    def get_owed_given(self, with_shadow=False):

        owed = self.points['owed']

        if with_shadow:
            given = self.points['given'] + sum(self.shadow_points.values())
        else:
            given = self.points['given']

        return owed, given

    def get_ratio(self, with_shadow):

        owed, given = self.get_owed_given(with_shadow)
        if owed == 0:
            return 0
        else:
            return given / owed

    def is_shadow(self, new_points, ratio_threshold):
        """
        Function to check if the user is to be cut off after the order is placed.

        :param ratio_threshold:
        :param new_points: dictionary containing keys 'owed' and 'given'
        :return:
        """

        if self.points['owed'] < NEW_USER_SHADOW_THRESHOLD: return False

        owed, given = self.get_owed_given(with_shadow=False)

        new_owed, new_given = owed + new_points['owed'], given + new_points['given']


        if new_given / new_owed < ratio_threshold:
            return True
        else:
            return False

    # def remove_othe

    def remove_cast_shadows(self, aps):
        for user in self.shadow_owed:
            aps.remove_shadow(by=self, on=user)


class APS():
    def __init__(self):
        self.order_people = []
        self.pickup_person = []
        self.order_point = 1
        self.pickup_point = self.order_point / len(self.pickup_person)
        self.df = pd.read_csv('users_data.csv')

    def place_order(self, orders_people, pickup_people, auto_pick=True):
        for user in order_people:
            # check if user is eligible for pickup for all but the people picking up
            if (user.)
        # once successful, the order can be placed, update the values on to the dataframe, and save the data frame.
        # else warn the user that a particular user needs to pickup

    def auto_pick(self, orders_people, pickup_people):
# return the person with the lowest pickup ratio from the list.
