import pygame.font

class Button():
    def __init__(self, ai_settings, screen, msg):
        """Initialise button attributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Button size and features
        self.width, self.height = 200, 50
        self.button_color = (10, 110, 10)
        self.button_text_color = (250, 250, 250)
        self.font_style = "Helvetica"
        self.font = pygame.font.SysFont(self.font_style, 38, True)

        # Object creation and center button position
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        # Show button message
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """Transform msg to rectangle and center it """
        self.msg_img = self.font.render(msg,
                                        True,
                                        self.button_text_color,
                                        self.button_color)
        self.msg_img_rect = self.msg_img.get_rect()
        self.msg_img_rect.center = self.rect.center

    def draw_button(self):
        # Display button at the screen
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_img, self.msg_img_rect)

