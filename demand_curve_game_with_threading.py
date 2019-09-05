import time
import random
import math
import numpy as np
import threading
import matplotlib.pyplot as plt


class Game:
    """
    # when you edit code for taking input while processing

    def __init__(self, product_name,user_num):
       self.user_price = user_num  .. # you can do this or just import the user_from another side
       and le self.user price get it , from the global scope
    """

    def __init__(self, product_name):
        """
        it's the initializing func , that takes the game to play , and start the whole game
        :param product_name:
        :return who won , and each player money that he got
        """

        self.product_name = product_name
        self.revenue_agent_all = 0
        self.revenue_user_all = 0
        self.revenue_user_all_list = []
        self.share_user_list = []
        self.time_line = []
        self.user_price = None
        # self.user_price = 58
        self.choose_game(self.product_name)

        print("user_last_number", self.user_price)

        if self.revenue_user_all > self.revenue_agent_all:
            print(f"You won agent .. :\n    You got {round(self.revenue_user_all, 2)} ,"
                  f" agent got : {round(self.revenue_agent_all, 2)}")
            print(
                f"You won agent by"
                f" {round(100 - round(((self.revenue_agent_all / self.revenue_user_all) * 100), 2), 2)} %")
        else:
            print(f"Agent won .. :\n agent got {round(self.revenue_agent_all, 2)} , "
                  f"you got : {round(self.revenue_user_all, 2)}")
            print(
                f"Agent won You by "
                f"{round(100 - round(((self.revenue_user_all / self.revenue_agent_all) * 100), 2), 2)} %")

        self.plotting_func()

    def choose_game(self, product_name):
        """
        :param product_name: it take it from __init__ fun
        :return: play what's is choosen from the init func
        """

        if product_name == 'groceries':
            self.fruit_game()
        elif product_name == "service":
            self.service_game()
        elif product_name == 'refined':
            self.wine_game()
        elif product_name == 'luxury':
            self.luxury_game()

    def fruit_game(self):
        """
        it a function to start the fruit game , with it's basic properties
        """
        cost_range = list(range(10, 18))
        print("cost range :", cost_range)
        ag_prices = [15, 16, 18, 21, 25, 30]

        loops_fruits = [[math.floor(random.random() * 200 + 900), 14],  # Summer
                        [math.floor(random.random() * 100 + 450), 12],  # Fall
                        [math.floor(random.random() * 100 + 250), 13],  # Winter
                        [math.floor(random.random() * 200 + 600), 15]]  # Spring

        self.start_game(cost_range, ag_prices, loops_fruits)
        return

    def service_game(self):
        """
        it a function to start the service game , with it's basic properties
        """
        cost_range = list(range(4, 8))
        ag_prices = [6, 7, 8, 10, 13, 17]

        loops_service = [[math.floor(random.random() * 5000 + 5000), 5],  # Summer
                         [math.floor(random.random() * 2000 + 2000), 6],  # Fall
                         [math.floor(random.random() * 1000 + 1000), 8],  # Winter
                         [math.floor(random.random() * 2000 + 2000), 10]]  # Spring

        self.start_game(cost_range, ag_prices, loops_service)

    def wine_game(self):
        """
        it a function to start the wine game , with it's basic properties
        """
        cost_range = list(range(25, 51))
        print("cost range :", cost_range)
        ag_prices = [46, 47, 50, 55, 65, 80]

        loops_wine = [[math.floor(random.random() * 200 + 200), 8],  # Summer
                      [math.floor(random.random() * 100 + 100), 5],  # Fall
                      [math.floor(random.random() * 100 + 100), 6],  # Winter
                      [math.floor(random.random() * 200 + 200), 8]]  # Spring

        self.start_game(cost_range, ag_prices, loops_wine)

    def luxury_game(self):
        """
        it a function to start the luxury game , with it's basic properties
        """
        cost_range = list(range(1750, 2001))
        ag_prices = [1850, 1900, 2000, 2100, 2300, 2500]

        loops_luxury = [[math.floor(random.random() * 20 + 20), 4],  # Summer
                        [math.floor(random.random() * 10 + 10), 2],  # Fall
                        [math.floor(random.random() * 10 + 10), 2],  # Winter
                        [math.floor(random.random() * 20 + 20), 4]]  # Spring

        self.start_game(cost_range, ag_prices, loops_luxury)

    def start_game(self, cost_range, agent_prices, loops):
        item_cost_ = random.choice(cost_range)
        print("item cost :", item_cost_)

        self.user_price = agent_prices[-1]

        threading_ = threading.Thread(target=self.get_user_input_while_running, args=(agent_prices,))
        threading_.daemon = True
        threading_.start()

        print("Summer")
        end_time = 0
        summer_time_loop_time = 15 / loops[0][1]
        while end_time < 15:
            items_quantity = loops[0][0]

            end_time = self.session_loop(agent_prices, items_quantity, item_cost_,
                                         end_time, summer_time_loop_time)

        print("Fall")
        fall_time_loop_time = 15 / loops[1][1]
        item_cost_ = random.choice(cost_range)
        print("item cost :", item_cost_)

        while end_time < 30:
            items_quantity = loops[1][0]

            end_time = self.session_loop(agent_prices, items_quantity, item_cost_, end_time,
                                         fall_time_loop_time)

        print("Winter")
        winter_time_loop_time = 15 / loops[2][1]
        item_cost_ = random.choice(cost_range)
        print("item cost :", item_cost_)

        while end_time < 45:
            items_quantity = loops[2][0]

            end_time = self.session_loop(agent_prices, items_quantity, item_cost_, end_time,
                                         winter_time_loop_time)

        print("Spring")
        spring_time_loop_time = 15 / loops[3][1]
        item_cost_ = random.choice(cost_range)
        print("item cost :", item_cost_)

        while end_time < 60:
            items_quantity = loops[3][0]

            end_time = self.session_loop(agent_prices, items_quantity, item_cost_,
                                         end_time, spring_time_loop_time)

    def get_user_input_while_running(self, allowed_prices):
        while True:
            try:
                x = int(input())
                if x in allowed_prices:
                    print("cost placed")
                    self.user_price = x
                else:
                    print("invalid cost")
            except ValueError:
                print("invalid input")
                pass

    def session_loop(self, agent_prices_, items_quantity_, item_cost, end_time_, time_loop_time):
        """
        it's a function that responsible for how the game work every part on second in the session,
        it takes ...

        where those params are there , it append them into a cycle, of processing , to get :
        the price of agent , the revenue of both players , and the share of the player , to make the
        graph more detailed.

        :return: the end time , to continue the cycle of the game, depending on a time ,
                to avoid the infinite while loop , and make the game continue with a specific cycle ,
                not a random events of time !.

        """
        print(f"Please input your price from list {agent_prices_}")
        time.sleep(time_loop_time)
        items_quantity_ = self.shift_curve(items_quantity_)
        chosen_number, revenue_agent, \
            customer_revenue, user_share = self.get_agent_price(agent_prices_,
                                                                items_quantity_, item_cost, self.user_price)

        print("revenue_agent", revenue_agent)
        print("revenue_competitor", customer_revenue)
        self.revenue_agent_all += revenue_agent
        self.revenue_user_all += customer_revenue
        self.revenue_user_all_list.append(customer_revenue)
        print("agent price :", chosen_number)
        print("player cost : ", self.user_price)
        print("game time : ", end_time_)
        self.time_line.append(end_time_)

        end_time_ += time_loop_time
        self.share_user_list.append(user_share)

        return end_time_

    @staticmethod
    def shift_curve(items_quantity_):
        """function to deal with the different events in the market , that affects on tha sales """
        all_probabilities = np.arange(0.5, 1.6, 0.1)
        shifted_curve = round(np.random.choice(all_probabilities), 1)
        items_quantity_ = items_quantity_ * shifted_curve
        return items_quantity_

    @staticmethod
    def get_revenue(chosen_number, items_quantity, items_costs, user_price):
        """
        it the function to get the share of every player in the market and calculate it's profit
        :param chosen_number: agent player
        :param items_quantity: number of items in market
        :param items_costs: the cost of one item
        :param user_price:  the user player cost for the item
        :return: the profits for agent and the player
        """
        all_prices = chosen_number + user_price
        if user_price < chosen_number:
            user_share = round((chosen_number / all_prices) * items_quantity)

            agent_share_ = round((user_price / all_prices) * items_quantity)
            ratio_ = 1 - (user_price / chosen_number)

            agent_share = agent_share_ - agent_share_ * (1 - 2 * ratio_)
            user_share += (agent_share_ - agent_share)

            user_got = (user_share * user_price) - (user_share * items_costs)

            agent_got = (agent_share * chosen_number) - (agent_share * items_costs)

            return agent_got, user_got, user_share

        if user_price > chosen_number:
            user_share_ = round((chosen_number / all_prices) * items_quantity)
            ratio_ = 1 - (chosen_number / user_price)
            user_share = user_share_ - user_share_ * (1 - 2 * ratio_)

            agent_share = round((user_price / all_prices) * items_quantity)
            agent_share += (user_share_ - user_share)

            user_got = (user_share * user_price) - (user_share * items_costs)

            agent_got = (agent_share * chosen_number) - (agent_share * items_costs)

            return agent_got, user_got, user_share

        if user_price == chosen_number:
            user_share = 0.5 * items_quantity
            user_got = (user_share * user_price) - (user_share * items_costs)
            agent_got = user_got
            return agent_got, user_got, user_share

    def get_agent_price(self, list_prices, number_population, cost_of_item, competitor_price):
        """
        A function to make the agent choose it's best price , for best profit,
        from the calcuated revenue that happened in get_revenue function.

        # the function actually take every price and calculate if used , how many revenue for agent will get,
        # so , it make the agent choose always the best revenue for it.. so it also know the best price to use.

        :param list_prices: the list of prices that agent choose from it's best price
        :param number_population: number of items in the market
        :param cost_of_item: cost of the item
        :param competitor_price: the user choice for price
        :return: agent best choice for profit , it's profit , the profit of the user

        """

        revenue_agent_list = []
        agent_number = []
        revenues = []
        revenue_user_list = []
        revenues_user = []
        user_share_list_ag = []
        user_share_list_user = []
        for i in list_prices:
            if i > cost_of_item:
                agent_number.append(i)
        for i in agent_number:
            revenue_agent, revenue_competitor, user_share = self.get_revenue(i, number_population, cost_of_item,
                                                                             competitor_price)

            if revenue_agent > revenue_competitor:
                try:
                    revenue_agent_list.append((revenue_agent / revenue_competitor, i))
                    revenues.append([revenue_agent, revenue_competitor])
                    user_share_list_ag.append(user_share)

                except ZeroDivisionError:
                    revenue_agent_list.append((100, i))
                    revenues.append([revenue_agent, revenue_competitor])
                    user_share_list_ag.append(user_share)

            if revenue_competitor > revenue_agent:
                try:
                    revenue_user_list.append((revenue_competitor / revenue_agent, i))
                    revenues_user.append([revenue_competitor, revenue_agent])
                    user_share_list_user.append(user_share)

                except ZeroDivisionError:
                    revenue_user_list.append((100, i))
                    revenues_user.append([revenue_competitor, revenue_agent])
                    user_share_list_user.append(user_share)

        try:
            max_revenue = max(revenue_agent_list)
            for i in range(len(revenue_agent_list)):
                if revenue_agent_list[i] == max_revenue:
                    agent_choice = revenue_agent_list[i][1]
                    revenue_agent = revenues[i][0]
                    revenue_competitor = revenues[i][1]
                    user_share = user_share_list_ag[i]
                    return agent_choice, revenue_agent, revenue_competitor, user_share

        except ValueError:
            max_revenue = min(revenue_user_list)
            for i in range(len(revenue_user_list)):
                if revenue_user_list[i] == max_revenue:
                    agent_choice = revenue_user_list[i][1]
                    revenue_agent = revenues_user[i][1]
                    revenue_competitor = revenues_user[i][0]
                    user_share = user_share_list_user[i]

                    return agent_choice, revenue_agent, revenue_competitor, user_share

    def plotting_func(self):
        """
        it's a function to plot the game result in all the session,
        draw the revenue , and the share for the player
        :return:
        """
        plt.subplot(211)
        plt.title("Revenue")
        plt.plot(self.time_line, self.revenue_user_all_list)
        plt.subplot(212)
        plt.title("User Share")
        plt.plot(self.time_line, self.share_user_list)
        plt.show()
        return


# app = Game('groceries')
# app = Game('service')
# app = Game('refined')
app = Game('luxury')
