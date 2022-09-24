from kivy.uix.relativelayout import RelativeLayout
# from main import reset_game
def keyboard_closed(self):
    self._keyboard.unbind(on_key_down=self.on_keyboard_down)
    self._keyboard.unbind(on_key_up=self.on_keyboard_up)
    self._keyboard.unbind(on_key_space=self.on_keyboard_space)

    self._keyboard = None

def reset_game(self):
        self.current_offset_y = 0
        self.current_y_loop=0        
        self.current_speed_x = 0
        self.current_offset_x = 0
        
        self.tiles_coordinates=[]
        self.score_txt="SCORE:0 " #+str(self.current_y_loop)
        self.pre_fill_tiles_coordinates()
        self.generate_tiles_coordinates()        
        
        
        self.state_game_over=False

def on_keyboard_down(self, keyboard, keycode, text, modifiers):
    
    if keycode[1] == 'left':
        self.current_speed_x = self.SPEED_X
    elif keycode[1] == 'right':
        self.current_speed_x = -self.SPEED_X
    elif keycode[1] == 'spacebar':
        self.reset_game()
        state_game_over=True
        state_game_has_started=True
        self.menu_widget.opacity=0
        
        

    return True

def on_keyboard_space(self, keyboard, keycode, text, modifiers):
    
    if keycode[1] == 32:
        self.reset_game()
    
    return True



def on_keyboard_up(self, keyboard, keycode):

    self.current_speed_x = 0
    return True


def on_touch_down(self, touch):
    
    if not self.state_game_over and self.state_game_has_started:
    
        if touch.x < self.width/2:
            # print("<-")
            self.current_speed_x = self.SPEED_X
        else:
            # print("->")
            self.current_speed_x = -self.SPEED_X
    
    return super(RelativeLayout,self).on_touch_down(touch)


def on_touch_up(self, touch):
    #print("UP")
    self.current_speed_x = 0
