from manim import *

UIS_GREEN = "#67b93e"
PURPLE = '#673c4f'
LIGHT_PURPLE = '#7f557d'
VIOLET = '#726e97'
DARK_SKY_BLUE = '#7698b3'
SKY_BLUE = '#83b5d1'
BEIGE = '#7c795d'

TIMELINE_TIMES = [
    "Epoca antigua",
    "3000 A.C.",
    "Biblia",
    "762 A.C.",
    "594 A.C.",
    "1066",
    "Siglo XVI", # General y Colombia
    "1800", # Colombia
    "Siglo XX", # General y Colombia
    "2000", # Colombia
    "2020" # Colombia
]

TIMELINE_LENGTH = 20

timeline_config = {
    "times" : TIMELINE_TIMES,
    "direction": DOWN,
    "length": TIMELINE_LENGTH,
    "arrow_scale": 1,
    "time_buff": 0.25,
    "time_scale": 0.4,
    "dot_colors": [
        PURPLE,
        LIGHT_PURPLE,
        VIOLET,
        DARK_SKY_BLUE,
        SKY_BLUE
    ]
}