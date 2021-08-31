from manim import *
import numpy as np


class Clock(VGroup):
    def __init__(self, circle_config={}, hands_config={}, ticks_config={}, **kwargs):
        circle = Circle(**circle_config)
        ticks = []
        for x in range(12):
            alpha = x / 12.0
            point = complex_to_R3(np.exp(2 * np.pi * alpha * complex(0, 1)))
            length = 0.2 if x % 3 == 0 else 0.1
            ticks.append(Line(point, (1 - length) * point, **ticks_config))

        self.hour_hand = Line(ORIGIN, 0.3 * UP, **hands_config)
        self.minute_hand = Line(ORIGIN, 0.6 * UP, **hands_config)
        # for hand in self.hour_hand, self.minute_hand:
        #     #Balance out where the center is
        #     hand.add(VectorizedPoint(-hand.get_end()))

        super().__init__(circle, self.hour_hand, self.minute_hand, *ticks)


class ClockPassesTime(Animation):
    def __init__(self, clock, hours_passed=12, rate_func=linear, **kwargs):
        assert isinstance(clock, Clock)
        self.hours_passed = hours_passed
        rot_kwargs = {"axis": OUT, "about_point": clock.get_center()}
        hour_radians = self.hours_passed * 2 * np.pi / 12
        self.hour_rotation = Rotating(
            clock.hour_hand, radians=hour_radians, **rot_kwargs
        )
        self.hour_rotation.begin()
        self.minute_rotation = Rotating(
            clock.minute_hand, radians=12 * hour_radians, **rot_kwargs
        )
        self.minute_rotation.begin()
        Animation.__init__(self, clock, **kwargs)

    def interpolate_mobject(self, alpha):
        for rotation in self.hour_rotation, self.minute_rotation:
            rotation.interpolate_mobject(alpha)
