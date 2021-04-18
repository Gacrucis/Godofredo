import math
from itertools import cycle
from manim import *

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

        timeline_line = Line(start=initial_point, end=initial_point.get_center()+RIGHT*lenght)

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

        text_bullet = create_bullet_point(text, text_color=next(text_colors), bullet_scale=bullet_scale, bullet_color=next(bullet_colors), bullet_buff=bullet_buff)
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