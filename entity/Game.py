import pygame
from entity.Fighter import Fighter
from entity.Tournament import Tournament

class Game:

    def __init__(self, screen_height: int = 640, screen_width: int = 480,  fighters: dict = {}):
        pygame.init()
        pygame.display.set_caption("Sparking!")
            
        self.tournament = Tournament(fighters)
        self.screen = pygame.display.set_mode((screen_height, screen_width))
        self.screen_center = (screen_height//2, screen_width//2)
        self.font = pygame.font.Font(None, 20)
    
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    def start_game(self):
        self.init_screen()
    
    def end_game(self):
        pygame.quit()

    def init_screen(self):
        blink_rate = 500  # text blinking time
        last_blink_time = pygame.time.get_ticks()
        visible = True

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        running = False
                        
            self.screen.fill(self.BLACK)
            current_time = pygame.time.get_ticks()

            #update visibility state
            if current_time - last_blink_time > blink_rate:
                visible = not visible
                last_blink_time = current_time

            # show message only if visible
            if visible:
                text = self.font.render("Press enter to generate rounds...", True, self.WHITE)
                text_rect = text.get_rect(center=self.screen_center) #centers the text
                self.screen.blit(text, text_rect) #draw text

            # update screen
            pygame.display.flip()

        
        self.matches_screen()

    def matches_screen(self):
        #by default tournament class set the matches when created
        #but you can shuffle as many times you want
        self.tournament.gen_matches()
        self.tournament.draw_base_bracket()
        
        self.screen.fill(self.BLACK)
        
        pygame.display.flip()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        running = False

    
    