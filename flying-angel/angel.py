from manim import *

def open():

    right_wing = Sector().rotate(angle = -PI/4).move_to(ORIGIN).align_to(ORIGIN, LEFT)
    left_wing = Sector().rotate(angle = 3*PI/4).move_to(ORIGIN).align_to(ORIGIN, RIGHT)
    body = Polygon([0, 0.26, 0], [-0.2, -1, 0], [0.2, -1, 0],
                   color=WHITE,
                   fill_color=WHITE,
                   fill_opacity=1)
    head = Circle(radius=0.2,
                  center=[0, 1, 0],
                  color=WHITE,
                  fill_color=WHITE,
                  fill_opacity=1).shift(UP * 0.4)
    crown = Ellipse(width=0.6,
                    height=0.2,
                    arc_center=[0, 0.9, 0],
                    stroke_width=2,
                    color=YELLOW_B)

    return VGroup(right_wing, left_wing, body, head, crown).scale(0.355)


def closed():

    right_wing = Sector().rotate(angle = -PI/4)
    left_wing = Sector().rotate(angle = 3*PI/4)
    right_wing.stretch(1.25, 1).stretch(0.6, 0).move_to(ORIGIN).align_to(ORIGIN, LEFT)
    left_wing.stretch(1.25, 1).stretch(0.6, 0).move_to(ORIGIN).align_to(ORIGIN, RIGHT)
    body = Polygon([0, 0.26, 0], [-0.2, -1, 0], [0.2, -1, 0],
                   color=WHITE,
                   fill_color=WHITE,
                   fill_opacity=1)
    head = Circle(radius=0.2,
                  center=[0, 1, 0],
                  color=WHITE,
                  fill_color=WHITE,
                  fill_opacity=1).shift(UP * 0.4)
    crown = Ellipse(width=0.6,
                    height=0.2,
                    arc_center=[0, 0.9, 0],
                    stroke_width=2,
                    color=YELLOW_B)

    return VGroup(right_wing, left_wing, body, head, crown).scale(0.355)
