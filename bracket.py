import matplotlib.pyplot as plt
import math

# ask for the stages in tournament, the height to operate y positions
# and initial right and left position at base stage
# this is needed to draw lines propertly 
def draw_stages(stages, height, right_pos, left_pos):
    num_matches = len(stages[0])
    
    n_stages = math.ceil(math.log(num_matches,2))+1 #return n stages (including base stage)
    print(f"num matches -> {num_matches}")
    print(f'stages -> {n_stages}')

    for i in range(1,n_stages+1):
        pass

def draw_base_bracket(stages):
    matches = stages[0]
    # Determine the number of matches and the height of the bracket
    num_matches = len(matches)
    height = num_matches * 2  # Two levels for each match
            
    # Set up the figure
    plt.figure(figsize=(10, height))
    
    line_style = "k--"
    left_line_x_position = 0.5
    right_line_x_position = 1.5
    line_gap = 0.4

    for i in range(0, num_matches, 2):
        f1_y_position = height - (i * 2) - 1
        f2_y_position = height - ((i+1) * 2) - 1
        delta_y = (f2_y_position + f1_y_position)//2+0.1
        #this loop draw two match at time one at the right and one at the left
        #since tournament participants are always a power of 2 this is possible

        # fighters 1 names
        plt.text(0, f1_y_position-0.1, matches[i][0], horizontalalignment='right', fontsize=12)
        plt.text(2, f1_y_position-0.1, matches[i+1][0], horizontalalignment='left', fontsize=12)

        # fighters 1 lines
        plt.plot([left_line_x_position, left_line_x_position-line_gap], [f1_y_position, f1_y_position], line_style)  # Left line
        plt.plot([right_line_x_position, right_line_x_position+line_gap], [f1_y_position, f1_y_position], line_style)  # Right line
        
        #vertical lines
        plt.plot([left_line_x_position, left_line_x_position], [f1_y_position, f2_y_position], line_style)  # Left line
        plt.plot([right_line_x_position, right_line_x_position], [f1_y_position, f2_y_position], line_style)  # Right line

        # match connection lines
        plt.plot([left_line_x_position, 0.8], [delta_y, delta_y], line_style)  # Left line
        plt.plot([right_line_x_position, 1.3], [delta_y, delta_y], line_style)  # Right line

        # fighters 2 names
        plt.text(0, f2_y_position-0.1, matches[i][1], horizontalalignment='right', fontsize=12)
        plt.text(2, f2_y_position-0.1, matches[i+1][1], horizontalalignment='left', fontsize=12)

        # fighters 2 lines
        plt.plot([left_line_x_position, left_line_x_position-line_gap], [f2_y_position, f2_y_position], line_style)  # Left line
        plt.plot([right_line_x_position, right_line_x_position+line_gap], [f2_y_position, f2_y_position], line_style)  # Right line
    

    draw_stages(stages, height, right_line_x_position, left_line_x_position)

    # Set the limits and remove axes
    plt.xlim(-0.5, 2.5)
    plt.ylim(-1, height)
    plt.axis('off')
    plt.title('Tournament Bracket', fontsize=16)
    
    plt.show()

# Example usage
matches = [("Player A", "Player C"), ("Player B", "Player D"),("Player A", "Player C"), ("Player B", "Player D")]
stages = [matches]  # stages refers to the number of steps to reach the victory 
                    # for example: top 16, top 8, semifinals, finals means 4 stages
                    # stages[0] will always be base match (when all fighters are on tournament)
draw_base_bracket(stages)