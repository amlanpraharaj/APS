import pandas as pd
#create a pd DataFrame for all users to pull ratio details using user name.
class Users():
    def __init__(self):
        self.user_name = None
        self.pickups = 0.1
        self.orders = 0.1
        self.rank = None
        self.shadow_points = {}
        self.contacts = []#list of user names.
        
    def get_rank(self, df):
        """
        Function to access database and retrieve the rank of the user based on their ratio.
        """
        
        
    def cut_off(self, df):
        """
        Function to check if the user is to be cut off after the order is placed.
        Args:
            None
        Returns:
            Boolean
        """
        if(self.rank) < 0.8 * len(df):
            return(True)
        return(False)
    
    def add_contact(self, phone_num):
        """
        Function to add a user with a particular phone number.
        """
    
class APS():
    def __init__(self):
        self.order_people = []
        self.pickup_person = []
        self.order_point = 1
        self.pickup_point = self.order_point/len(self.pickup_person)
        self.df = pd.read_csv('users_data.csv')
        
    def place_order(self, orders_people, pickup_people, auto_pick = True):
        for user in order_people:
            #check if user is eligible for pickup for all but the people picking up
            if(user.)
        #once successful, the order can be placed, update the values on to the dataframe, and save the data frame.
        #else warn the user that a particular user needs to pickup
        
    def auto_pick(self, orders_people, pickup_people):
        #return the person with the lowest pickup ratio from the list.
        