from manim import *
import numpy as np
import random

class ShatterLine(Scene):
    def construct(self):

        # random permuation of integers between -500 and 499 to randomly allocate centres of rotations
        perm = np.random.permutation([n for n in range(-500,500)])
        perm1 = perm[:500]
        perm2 = perm[500:]
        # create centre coordinates
        cents = []
        for k in range(-500,500):
            cent = np.array([(perm[k] + k) / 80, 0,0])
            cents.append(cent) 
        
        # have rotations performed in the top half or bottom half randomly
        updown = [random.choice([-1,1]) for n in range(1000)]

        # the line is a sequence of dots; in the full video I add the dots then fade out an existing line
        # Note: sequence of dots (and positions of centres) should exceed the width of the screen so that some leave / some enter when the rotations are played
        dts = []
        for n in range(1000):
            dt = Dot(radius = 0.02) #matches standard line width, if required
            dt.move_to(np.array([(n-500) / 40,0,0]))
            dts.append(dt)
            
        # PLAY: fade in dots
        self.play(*[FadeIn(t) for t in dts])
        self.wait()

        # separate into a set of groups of rotations of varying radii and runtime
        rotate_group1 = AnimationGroup(*[Rotate(dts[n],
                                 PI * updown[n],
                                 about_point=cents[n]) for n in perm[:100]],
                                 run_time = 5)
        rotate_group2 = AnimationGroup(*[Rotate(dts[n],
                                 PI * updown[n],
                                 about_point=cents[n]) for n in perm[100:300]],
                                 run_time = 4.5)
        rotate_group3 = AnimationGroup(*[Rotate(dts[n],
                                 PI * updown[n],
                                 about_point=cents[n]) for n in perm[300:500]],
                                 run_time = 3.5)
        rotate_group4 = AnimationGroup(*[Rotate(dts[n], 
                                 PI * updown[n],
                                 about_point=cents[n]) for n in perm[500:700]],
                                 run_time = 3)
        rotate_group5 = AnimationGroup(*[Rotate(dts[n],
                                 PI * updown[n],
                                 about_point=cents[n]) for n in perm[700:900]],
                                 run_time = 3.5)
        rotate_group6 = AnimationGroup(*[Rotate(dts[n],
                                 PI * updown[n],
                                 about_point=cents[n]) for n in perm[900:]],
                                 run_time = 4)
        # PLAY: all rotations
        chaos = AnimationGroup(rotate_group1,
                                rotate_group2,
                                rotate_group3,
                                rotate_group4,
                                rotate_group5,
                                rotate_group6,
                                lag_ratio = 0.1)
        self.play(chaos)
        self.wait(1/4)
        self.play(*[FadeOut(o) for o in self.mobjects])
