import matplotlib.pyplot as plt
import math
import random

class Tournament():
    def __init__(self, fighters: dict):
        self.fighters = fighters
        self.stages = [[None]]    # stages refers to the number of steps to reach the victory 
                            # for example: top 16, top 8, semifinals, finals means 4 stages
                            # stages[0] will always be base match (when all fighters are on tournament)
        
        self.gen_matches()
        # Determine the number of matches and the height of the bracket   
        self.num_matches = len(self.stages[0])
        self.height = self.num_matches * 3  # Three levels for each match

        #style for tournament diagram
        self.line_style = "k--"
        self.left_line_x_position = 0.3
        self.right_line_x_position = 1.7
        self.line_gap = 0.25
        

    def gen_matches(self):
        fighters_list = list(self.fighters.keys())
        random.shuffle(fighters_list)
        base_stage = []

        for i in range(0, len(fighters_list), 2):
            base_stage.append(fighters_list[i: i+2])

        self.stages[0] = base_stage
        return base_stage
    
    def draw_base_bracket(self):
        matches = self.stages[0]
                
        # Set up the figure
        plt.figure(figsize=(10, self.height))
        for i in range(0, self.num_matches, 2):
            f1_y_position = self.height - (i * 2) - 1
            f2_y_position = self.height - ((i+1) * 2) - 1
            delta_y = (f2_y_position + f1_y_position)//2
            #this loop draw two match at time one at the right and one at the left
            #since tournament participants are always a power of 2 this is possible

            (fighter_a, fighter_b) = (self.fighters[matches[i][j]].fighter for j in range(2))
            (fighter_c, fighter_d) = (self.fighters[matches[i+1][j]].fighter for j in range(2))

            # fighters 1 names
            plt.text(0, f1_y_position-0.05, fighter_a, horizontalalignment='right', fontsize=12)
            plt.text(2, f1_y_position-0.05, fighter_c, horizontalalignment='left', fontsize=12)

            left_x_f = self.left_line_x_position-self.line_gap
            right_x_f = self.right_line_x_position+self.line_gap

            # fighters 1 lines
            plt.plot([self.left_line_x_position, left_x_f], [f1_y_position, f1_y_position], self.line_style)  # Left line
            plt.plot([self.right_line_x_position, right_x_f], [f1_y_position, f1_y_position], self.line_style)  # Right line
            
            #vertical lines
            plt.plot([self.left_line_x_position, self.left_line_x_position], [f1_y_position, f2_y_position], self.line_style)  # Left line
            plt.plot([self.right_line_x_position, self.right_line_x_position], [f1_y_position, f2_y_position], self.line_style)  # Right line

            # match connection lines
            plt.plot([self.left_line_x_position, self.left_line_x_position + self.line_gap], [delta_y, delta_y], self.line_style)  # Left line
            plt.plot([self.right_line_x_position, self.right_line_x_position - self.line_gap], [delta_y, delta_y], self.line_style)  # Right line

            # fighters 2 names
            plt.text(0, f2_y_position-0.05, fighter_b, horizontalalignment='right', fontsize=12)
            plt.text(2, f2_y_position-0.05, fighter_d, horizontalalignment='left', fontsize=12)

            # fighters 2 lines
            plt.plot([self.left_line_x_position, left_x_f], [f2_y_position, f2_y_position], self.line_style)  # Left line
            plt.plot([self.right_line_x_position, right_x_f], [f2_y_position, f2_y_position], self.line_style)  # Right line
        

        self.draw_stages()

        # Set the limits and remove axes
        plt.xlim(-0.5, 2.5)
        plt.ylim(-1, self.height)
        plt.axis('off')
        plt.title('Tournament Bracket', fontsize=16)
        plt.show()

    # ask for the stages in tournament, the height to operate y positions
    # and initial right and left position at base stage
    # this is needed to draw lines propertly 
    def draw_stages(self):
        n_stages = math.ceil(math.log(self.num_matches,2))+1 #return n stages (including base stage)
        print(f"n stages -> {n_stages}")
        for i in range(2, n_stages):
            skip = int(math.pow(2,i))
            #print(f"i -> {i}")
            for j in range(0, self.num_matches, skip):
                #positions (x,y)
                left_x_position = self.left_line_x_position + self.line_gap*(i-1)
                right_x_position = self.right_line_x_position - self.line_gap*(i-1)

                ##### upper match #####
                left_l1_y_position = self.height - (j * i) - 1
                left_l2_y_position = self.height - ((j+1) * i) - 1
                
                #f1_y_position = self.height - (i * 2) - 1
               # f2_y_position = self.height - ((i+1) * 2) - 1

                delta_y0 = (left_l2_y_position + left_l1_y_position)//2

                ##### lower match #####
                left_l1_y_position = self.height - ((j+skip-2) * 2) - 1
                left_l2_y_position = self.height - ((j+skip-1) * 2) - 1

                #f1_y_position = self.height - (i * 2) - 1
               # f2_y_position = self.height - ((i+1) * 2) - 1

                delta_y1 = (left_l2_y_position + left_l1_y_position)//2

                #vertical lines
                plt.plot([left_x_position, left_x_position], [delta_y0, delta_y1], self.line_style)  # Left line
                plt.plot([right_x_position, right_x_position], [delta_y0, delta_y1], self.line_style)  # Right line

                delta_y = (delta_y1 + delta_y0)//2

                # match connection lines
                plt.plot([left_x_position, left_x_position + self.line_gap], [delta_y, delta_y], self.line_style)  # Left line
                plt.plot([right_x_position, right_x_position - self.line_gap], [delta_y, delta_y], self.line_style)  # Right line
                


            