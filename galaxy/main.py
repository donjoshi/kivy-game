from kivy.config import Config
Config.set('graphics', 'width', '900')
Config.set('graphics', 'height', '400')

from kivy import platform
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.metrics import dp
from kivy.properties import StringProperty
from kivy.properties import StringProperty, BooleanProperty
from kivy.graphics.vertex_instructions import Line
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle, Ellipse
from kivy.properties import Clock
from kivy.properties import NumericProperty



class MainWidget(Widget):

    from transforms import transform, transform_2D, transform_perspective
    from user_actions import keyboard_closed, on_keyboard_down, on_keyboard_up, on_touch_down, on_touch_up
    perspective_point_x = NumericProperty(0)
    perspective_point_y = NumericProperty(0)

    V_NB_LINES = 10
    V_LINES_SPACING = .25  # % in screen width

    vertical_lines = []

    H_NB_LINES = 15
    H_LINES_SPACING = .1  # % in screen height

    horizontal_lines = []

    SPEED = 4
    current_offset_y = 0

    SPEED_X = 12
    current_speed_x = 0
    current_offset_x = 0

    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        # print("INIT W: " + str(self.width) +" H: "+str(self.height))
        self.init_vertical_lines()
        self.init_horizontal_lines()

        if self.is_desktop():
            self._keyboard = Window.request_keyboard(
                self.keyboard_closed, self)
            self._keyboard.bind(on_key_down=self.on_keyboard_down)
            self._keyboard.bind(on_key_up=self.on_keyboard_up)

        Clock.schedule_interval(self.update, 1.0 / 60.0)

    def is_desktop(self):
        if platform == 'win' or platform == 'linux' or platform == 'macosx':
            return True

        return False

    def init_vertical_lines(self):
        with self.canvas:
            Color(1, 1, 1)
            #self.line = Line(points=[100, 0, 100, 100])
            for i in range(0, self.V_NB_LINES):
                self.vertical_lines.append(Line())

    def get_line_from_index(self):
        pass

    def update_vertical_lines(self):
        central_line_x = int(self.width/2)
        #spacing = int(self.width*self.V_LINES_SPACING)
        spacing = self.width*self.V_LINES_SPACING
        #self.line.points = [center_x, 0, center_x, 100]
        offset = -int(self.V_NB_LINES/2)+.5

        for i in range(0, self.V_NB_LINES):
            line_x = central_line_x + offset * spacing+self.current_offset_x

            x1, y1 = self.transform(line_x, 0)
            x2, y2 = self.transform(line_x, self.height)
            self.vertical_lines[i].points = [x1, y1, x2, y2]
            offset += 1

    def init_horizontal_lines(self):
        with self.canvas:
            Color(1, 1, 1)
            #self.line = Line(points=[100, 0, 100, 100])
            for i in range(0, self.H_NB_LINES):
                self.horizontal_lines.append(Line())

    def update_horizontal_lines(self):

        central_line_x = int(self.width/2)
        spacing = self.width*self.V_LINES_SPACING
        offset = int(self.V_NB_LINES/2)-.5

        xmin = central_line_x-offset*spacing+self.current_offset_x
        xmax = central_line_x+offset*spacing+self.current_offset_x
        spacing_y = self.height*self.H_LINES_SPACING

        for i in range(0, self.H_NB_LINES):
            line_y = i*spacing_y-self.current_offset_y

            x1, y1 = self.transform(xmin, line_y)
            x2, y2 = self.transform(xmax, line_y)
            self.horizontal_lines[i].points = [x1, y1, x2, y2]

    def update(self, dt):
        #print("dt : " + str(dt*60))
        time_factor = dt*60
        self.update_vertical_lines()
        self.update_horizontal_lines()
        self.current_offset_y += self.SPEED*time_factor

        spacing_y = self.height*self.H_LINES_SPACING
        if self.current_offset_y >= spacing_y:
            self.current_offset_y -= spacing_y

        self.current_offset_x += self.current_speed_x*time_factor


class GalaxyApp(App):
    pass


GalaxyApp().run()
