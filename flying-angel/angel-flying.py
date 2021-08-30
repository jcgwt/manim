from manim import *
import angel

class FlyingAngel(Scene):

    def construct(self):

        back_color =  "#CFB88B"
        self.camera.background_color = back_color
        for i in range(-7, 8):
            self.add(Line([i+1/2, -5, 0], [i+1/2, 5, 0],
                     stroke_width=2,
                     color=WHITE))
        for j in range(-5, 6):
            self.add(Line([-8, j+1/2, 0], [8, j+1/2, 0],
                     stroke_width=2,
                     color=WHITE))

        closed_wings = [angel.closed() for _ in range(3)]
        open_wings = [angel.open() for _ in range(4)]
        # this sets the speed for each wing flap and can be customised
        close_speeds = [0.2, 0.08, 0.05]
        open_speeds = [0.1, 0.05, 0.09]

        open_wings[0].move_to([-8, 2, 0])
        self.add(open_wings[0])

        open_wings[0].generate_target()
        open_wings[0].target.move_to(ORIGIN)
        self.play(MoveToTarget(open_wings[0]))
        self.wait(1/2)

        for t in range(3):
            self.play(ReplacementTransform(open_wings[t], closed_wings[t]), run_time=close_speeds[t])
            self.play(ReplacementTransform(closed_wings[t], open_wings[t+1]), run_time=open_speeds[t])

        open_wings[-1].generate_target()
        open_wings[-1].target.move_to([9, 3, 0])
        self.play(MoveToTarget(open_wings[-1]))
        self.wait()


