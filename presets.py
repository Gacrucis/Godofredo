import os
import math
from itertools import cycle
from manim import *


class TimeLine(VGroup):
    def __init__(
        self, times: list, length: float = None, direction: "ndarray" = None, time_buff: float = None,
        time_scale: float = None, dot_scale: float = None, dot_colors: list = None, arrow_buff: float = None,
        arrow_scale: float = None, line_config: dict = {}, arrow_config: dict = {}, time_config: dict = {},
        dot_config: dict = {}, *args, **kwargs
    ):
        super().__init__(*args, **kwargs)

        self.length = length or Camera(None).frame_width / 2
        self.size = len(times)

        # control next time index and next dot index
        self.index_reference = {
            'times': 0,
            'dots': 0
        }

        if direction is RIGHT:
            height_buff = 1.3

            frame_height = Camera(None).frame_height


            left_x_coord = LEFT * self.length / 2
            left_y_coord = UP * (frame_height / 2 - height_buff)

            # horizontally centered
            self.end_point = -left_x_coord + left_y_coord

            self.directions = {
                'times': DOWN,
                'arrow': UP,
                'arrow_direction': DOWN,
                'scroll': LEFT
            }
        
        elif direction is DOWN:
            left_buff = 1.3

            frame_width = Camera(None).frame_width


            left_x_coord = LEFT * (frame_width / 2 - left_buff)
            left_y_coord = UP * self.length / 2

            # vertically centered
            self.end_point = left_x_coord - left_y_coord

            self.directions = {
                'times': RIGHT,
                'arrow': LEFT,
                'arrow_direction': RIGHT,
                'scroll': UP
            }
        
        else:
            raise Exception("Expecting RIGHT or DOWN vectors only")


        self.initial_point = left_x_coord + left_y_coord

        # create main line

        self.line = Line(
            start=self.initial_point,
            end=self.end_point,
            z_index=0,
            **line_config
        )

        self.dots = VGroup()
        self.times = VGroup()

        dot_scale = dot_scale or 1
        time_scale = time_scale or 0.6
        arrow_scale = arrow_scale or 1

        self.time_buff = time_buff or 0.5
        self.arrow_buff = arrow_buff = arrow_buff or 0.3

        # default colors

        default_dots_color = BLUE
        default_arrow_color = WHITE

        if not dot_colors:
            dot_colors = [default_dots_color]
        
        dot_colors = cycle(dot_colors)

        point_distance = 1 / (self.size - 1)

        # create dots and times

        for n, time in enumerate(times):
            position = self.line.point_from_proportion(point_distance * n)

            dot = Dot(z_index=1, **dot_config).scale(dot_scale).move_to(position)
            dot.set_color(next(dot_colors))

            self.dots.add(dot)

            time_mob = Tex(time, z_index=1, **time_config).scale(time_scale)
            time_mob.next_to(position, self.directions['times'], self.time_buff)

            self.times.add(time_mob)

        # create arrow

        self.arrow = Arrow(
            start=ORIGIN,
            end=self.directions['arrow_direction'],
            **arrow_config
        ).scale(arrow_scale)

        # predefine buff for next_time method works properly
        self.arrow.next_to(self.dots[0], self.directions['arrow'], buff=self.arrow_buff)

        if not "color" in arrow_config:
            self.arrow.set_color(default_arrow_color)

        self.add(
            self.line,
            *self.dots,
            *self.times,
            self.arrow
        )

    def shift(self, direction: "ndarray") -> "TimeLine":
        self.line.shift(direction)
        current_dot = self.get_current_dot()
        self.arrow.next_to(current_dot, self.directions['arrow'], self.arrow_buff)
    
    def next_to(self, *args, **kwargs) -> "TimeLine":
        line = self.get_line()

        line.next_to(*args, **kwargs)

        self.position_elements()
        
        return self
    
    def position_dots(self) -> None:
        point_distance = 1 / (self.size - 1)
        line = self.get_line()
        dots = self.get_dots()

        for n, dot in enumerate(dots):
            dot.move_to(
                line.point_from_proportion(point_distance * n)
            )
        
    def position_times(self) -> None:
        point_distance = 1 / (self.size - 1)
        line = self.get_line()
        times = self.get_times()

        for n, time in enumerate(times):
            time.move_to(
                line.point_from_proportion(point_distance * n)
            )

    def position_elements(self) -> None:
        """
            Position dots, times and arrow
        """
        point_distance = 1 / (self.size - 1)

        line = self.get_line()
        times = self.get_times()
        dots = self.get_dots()
        arrow = self.get_arrow()

        for n in range(self.size):
            position = line.point_from_proportion(point_distance * n)

            times[n].next_to(position, self.directions['times'], buff=self.time_buff)
            dots[n].move_to(position)
        
        current_dot = self.get_current_dot()

        arrow.next_to(current_dot, self.directions['arrow'], self.arrow_buff)

    def get_dots(self) -> VGroup:
        return self.dots

    def get_times(self) -> VGroup:
        return self.times

    def get_line(self) -> Line:
        return self.line

    def get_arrow(self) -> Arrow:
        return self.arrow

    def get_next_time(self, increment: bool=True) -> Tex:
        if self.index_reference['times'] > self.size:
            raise Exception("Next time exceeds size")
        
        index = self.index_reference['times']

        next_time = self.times[index]
        if not increment:
            return next_time
            
        self.index_reference['times'] += 1

        return next_time

    def get_current_time(self) -> Tex:
        current_time_index = self.index_reference['times'] - 1
        if current_time_index < 0:
            current_time_index = 0
        
        return self.times[current_time_index]

    def get_next_dot(self) -> Dot:
        if self.index_reference['dots'] > self.size:
            raise Exception("Next dot exceeds size")

        index = self.index_reference['dots']

        next_dot = self.dots[index]
        self.index_reference['dots'] += 1

        return next_dot

    def get_current_dot(self) -> Dot:
        current_dot_index = self.index_reference['dots'] - 1
        if current_dot_index < 0:
            current_dot_index = 0
        
        return self.dots[current_dot_index]

    def create(self, with_arrow: bool = False, with_time: bool = False) -> AnimationGroup:
        animations = [
            DrawBorderThenFill(self.line),
            DrawBorderThenFill(self.dots)
        ]
        if with_arrow:
            animations.append(
                DrawBorderThenFill(self.arrow)
            )

        if with_time:
            self.index_reference['times'] += 1  # increased next time index
            animations.append(
                Write(self.times[0])
            )

        self.index_reference['dots'] += 1  # increases next dot index
        return AnimationGroup(*animations)

    def next_time(self) -> AnimationGroup:
        """
            animate both arrow shift and time write
        """
        target_time = self.get_next_time()
        next_dot = self.get_next_dot()

        animations = [
            self.arrow.animate.next_to(next_dot, self.directions['arrow'], buff=self.arrow_buff),
            Write(target_time)
        ]

        return AnimationGroup(*animations)
    
    def next_time_scroll(self) -> AnimationGroup:
        """
            make scroll effect by shifting
            self.line up or right
        """
        current_dot = self.get_current_dot()
        next_dot = self.get_next_dot()

        dots_distance = abs(current_dot.get_center() - next_dot.get_center())


        first_time = self.get_times()[0]
        current_time = self.get_current_time()
        target_time = self.get_next_time()

        target_time.add_updater(
            lambda mob: mob.next_to(next_dot, self.directions['times'], self.time_buff)
        )

        if current_time is first_time:

            first_dot = self.get_dots()[0]

            current_time.add_updater(
                lambda mob: mob.next_to(first_dot, self.directions['times'], self.time_buff)
            )

        animations = [
            self.line.animate.shift(self.directions['scroll'] * dots_distance),
            self.dots.animate.shift(self.directions['scroll'] * dots_distance),
            Write(target_time)
        ]

        return AnimationGroup(*animations)

    def fade(self) -> AnimationGroup:
        animations = [
            FadeOut(self.dots),
            FadeOut(self.line),
            FadeOut(self.arrow),
            FadeOut(self.times)
        ]
        return AnimationGroup(*animations)

    def _load_from(self, target_time: str, scene_class: "Scene"=None) -> VGroup:
        """
            - get times that should have been shown
            before 'time' including 'target_time'
            - shift arrow to 'time'
        """
        times_string = [mob_time.get_tex_string() for mob_time in self.times]

        if not target_time in set(times_string):
            raise Exception(f'{target_time} is not a valid time')
        
        self.times[0].get_tex_string()

        target_index = [
            index 
            for index, time_str in enumerate(times_string) 
            if time_str == target_time
        ][0]

        return self.times[:target_index + 1]

    def _attach_to_dot(self, target_time: Tex, dot: Dot) -> Tex:
        target_time.add_updater(
            lambda mob: mob.next_to(dot, self.directions['times'], self.time_buff)
        )
        return target_time

    def preload_for_scene(self, target_time: str, scene: "Scene", with_arrow: bool=True) -> None:
        """
            load times previous to 'target_time' (including target_time) and 
            add them directly to the scene_class
        """
        previous_times = self._load_from(target_time)
        new_index = len(previous_times)

        dots = self.get_dots()
        first_dot = dots[0]

        self.index_reference['dots'] = new_index
        self.index_reference['times'] = new_index

        # once index_reference is updated current_dot is right
        current_dot = self.get_current_dot()

        # calculates the corresponding shift based on number of previous times
        shift_size = abs(first_dot.get_center() - current_dot.get_center())
        line = self.get_line()

        line.shift(self.directions['scroll'] * shift_size)
        dots.shift(self.directions['scroll'] * shift_size)

        # add updaters to the times

        [
            self._attach_to_dot(time, dot) 
            for time, dot in zip(previous_times, dots)
        ]

        scene.add(
            line,
            dots,
            *previous_times
        )

        if with_arrow:
            scene.add(self.arrow)


class PTex(Tex):
    def __init__(
        self, 
        text: str, 
        alignment: str = "center", 
        line_length: int = 40, 
        interline_space: float = MED_LARGE_BUFF,
        tex_environment: str = None, 
        **kwargs
    ):
        """
            alignment: can take 'center', 'left' or 'right', default is 'left'
            
        """
        line_separated = [
            line + r"\\"
            for line in self.text_to_lines(text, line_length=line_length)
        ]
        super().__init__(
            *line_separated,
            tex_environment=tex_environment,
            **kwargs)

        self.arrange(
            **{
                "direction": DOWN,
                "aligned_edge": RIGHT if alignment == "right" else LEFT,
                "center": True if alignment == "center" else False,
                "buff": interline_space
            }
        )
    
    def text_to_lines(self, text: str, line_length: int = 40) -> list:
        text = text.strip()
        text_length = len(text)
        line_amount = text_length // line_length
        text_lines = []

        text_words = text.split(' ')
        current_word_index = 0
        min_length = 9999
        min_line = 0

        for i in range(line_amount):
            current_line = []
            current_length = 0

            while current_length < line_length and current_word_index < len(text_words):
                current_word = text_words[current_word_index]

                current_line.append(current_word)
                current_length += len(current_word) + 1
                current_word_index += 1
            
            text_lines.append(current_line)

            if current_length < min_length:
                min_length = current_length
                min_line = i
        
        if current_word_index <= (len(text_words)-1):
            text_lines.append(
                text_words[current_word_index:]
            )

        processed_lines = [' '.join(line) for line in text_lines]
        processed_lines = [line.strip() for line in processed_lines]

        return processed_lines

def get_vmobjects_from_scene(scene):

    mobjects = scene.mobjects
    vmobjects = VGroup()

    for m in mobjects:
        if isinstance(m, VMobject) and isinstance(m, Mobject):
            vmobjects.add(m)

    return vmobjects


def create_timeline(dot_amount=5, dot_scale=1, lenght=Camera(None).frame_width-4, height_buff=1.3, dot_colors=None, timeline_color=WHITE):

    initial_point = Point()
    initial_point.align_on_border(UP, buff=height_buff)
    initial_point.shift(LEFT*lenght/2)

    timeline_line = Line(start=initial_point,
                         end=initial_point.get_center()+RIGHT*lenght)

    point_distance = 1/(dot_amount-1)

    dots = VGroup()

    for n in range(dot_amount):

        current_dot = Dot()
        current_dot.scale(dot_scale)
        if dot_colors:
            current_dot.set_color(dot_colors[n])

        dot_position = timeline_line.point_from_proportion(point_distance*n)
        current_dot.move_to(dot_position)

        dots.add(current_dot)

    return VGroup(timeline_line, dots)


def create_bullet_point(text, text_color=WHITE, bullet_scale=0.8, bullet_color=None, bullet_buff=0.2):

    if bullet_color is None:
        bullet_color = text_color

    bullet = Dot(color=bullet_color)
    bullet.scale(bullet_scale)

    text_mobject = Tex(text, color=text_color, alignment=r'\raggedright')
    text_mobject.next_to(bullet, RIGHT, bullet_buff)

    def text_updater(m):
        m.next_to(bullet, direction=RIGHT, buff=bullet_buff)

    text_mobject.add_updater(text_updater)

    bullet_point = VGroup(bullet, text_mobject)
    return bullet_point


def create_bullet_list(text_list, start_point=ORIGIN, text_colors=None, bullet_scale=1, bullet_colors=None, bullet_buff=0.3, text_buff=0.6, text_scale=0.7):

    bullet_list = VGroup()

    if text_colors is None:
        text_colors = [WHITE, WHITE]

    if bullet_colors is None:
        bullet_colors = text_colors

    text_colors = cycle(text_colors)
    bullet_colors = cycle(bullet_colors)

    for i, text in enumerate(text_list):
        text_bullet = create_bullet_point(
            text, 
            text_color=next(
            text_colors), 
            bullet_scale=bullet_scale, 
            bullet_color=next(bullet_colors), 
            bullet_buff=bullet_buff
        )
        text_bullet.scale(text_scale)
        text_bullet[0].move_to(start_point)
        text_bullet[0].align_to(start_point, UP)

        bullet_list.add(text_bullet)

    for i, text_bullet in enumerate(bullet_list):

        if i:
            text_bullet[0].next_to(bullet_list[i-1][0], DOWN, buff=text_buff)
            text_bullet[0].align_to(bullet_list[i-1][0], LEFT)

    return bullet_list


def create_chapter(title, subtitle, color=MAROON_C, subtitle_buff=-0.5, scale_factor=0.7):

    anims = []

    lc_title = Tex(title)
    lc_title.scale(2 * scale_factor)

    anims.append(Write(lc_title))
    anims.append(Wait())
    # anims.append(ApplyMethod(lc_title.move_to, UP))
    anims.append(lc_title.animate.move_to(UP))

    subtitle = Tex(subtitle)
    subtitle.scale(scale_factor)
    subtitle.set_color(color)
    subtitle.next_to(lc_title, DOWN, buff=subtitle_buff)

    anims.append(Write(subtitle))
    anims.append(Wait())

    title = VGroup(lc_title, subtitle)

    anims.append(FadeOutAndShift(title, direction=DOWN))
    anims.append(Wait())

    return [anims, VGroup(title, subtitle)]

    # title = Tex(text, color=color)
    # title.scale(scale_factor)

    # bar = Line()
    # bar.set_opacity(0)

    # bar_radius = Camera().frame_width/2 - bar_buff

    # if bar:

    #     bar = Line(start=LEFT*bar_radius, end=RIGHT*bar_radius, color=bar_color)
    #     bar.next_to(title, DOWN, buff=0.2)

    # return VGroup(title, bar)


def create_paragraph(text, color=WHITE, scale_factor=0.5):

    paragraph = Tex(text, color=color, alignment=r'\justifying')
    paragraph.scale(scale_factor)

    return paragraph


def create_ripple(center=ORIGIN, max_radius=3, color=WHITE, current_radius=0):

    if current_radius <= 0:
        return Dot(point=center, color=color)

    current_radius = current_radius % max_radius

    decay_func = get_decay_func(treshold=max_radius)
    current_opacity = 1 - decay_func(current_radius)

    ripple = Circle(radius=current_radius)
    ripple.set_stroke(color=color, opacity=current_opacity)

    ripple.move_to(center)

    return ripple


def get_decay_func(treshold):

    # Creates a logaritmic function that equals 0 when x = 0
    # and equals 1 when x = treshold
    # f(x) = ln((decay_rate)x + 1)

    decay_rate = (math.e - 1)/treshold

    def decay_func(x):
        return math.log(decay_rate * x + 1)

    return decay_func


def create_interference_pattern(amount=5, width=0.5, height=1.5):

    pattern = VGroup()
    pattern_color = YELLOW_B

    for n in range(amount):

        light = Rectangle(height=height, width=width)
        light.set_fill(color=pattern_color, opacity=0.8)
        light.set_stroke(color=YELLOW_A, width=4)

        light.shift(RIGHT*width*n*2)

        pattern.add(light)

    return pattern

def text_to_lines(text, line_length=40):

    text = text.strip()
    text_length = len(text)
    line_amount = text_length // line_length
    text_lines = []

    text_words = text.split(' ')
    current_word_index = 0
    min_length = 9999
    min_line = 0

    for i in range(line_amount):
        current_line = []
        current_length = 0

        while current_length < line_length and current_word_index < len(text_words):
            current_word = text_words[current_word_index]

            current_line.append(current_word)
            current_length += len(current_word) + 1
            current_word_index += 1
        
        text_lines.append(current_line)

        if current_length < min_length:
            min_length = current_length
            min_line = i
    
    if current_word_index <= (len(text_words)-1):
        text_lines.append(
            text_words[current_word_index:]
        )
        # for line in text_lines[min_line:-1]:
            # line.append(text_lines[current_word_index+1].pop(0))

            # current_word_index += 1
        
        # text_lines[-1].append(text_words[-1])

    processed_lines = [' '.join(line) for line in text_lines]
    processed_lines = [line.strip() for line in processed_lines]

    return processed_lines


def text_to_paragraph(text, line_length=40, **kwargs):

    lines = text_to_lines(text, line_length=line_length)

    return Paragraph(*lines, **kwargs)

def image_path(name: str, folder_path=['assets', 'images']) -> str:
    path = os.path.join(*folder_path, name)
    if not os.path.exists(path):
        raise Exception(f"{path} does not exist.")
    return path

def get_coords(x: float, y: float) -> "ndarray":
    return RIGHT * x + UP * y