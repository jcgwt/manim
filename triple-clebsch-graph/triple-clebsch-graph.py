from manim import *
import numpy as np

# this produces an attractive 3-colouring of 3 copies of the Clebsch graph, producing a 3-coloring of the complete graph on 16 vertices
# in particular, coupled with the standard argument that R(3,3,3) ≤ 17, this shows R(3,3,3) = 17

class TripleClebschGraph(Scene):
    def construct(self):
        
        # create vertices
        centre = Dot([0,0,0])
        inner = [Dot([np.cos(2.05*PI/10+k*2*PI/5),np.sin(2.05*PI/10+k*2*PI/5),0]) for k in range(5)]
        middle = [Dot([1.8*np.cos(8.1*PI/20+k*2*PI/5),1.8*np.sin(8.1*PI/20+k*2*PI/5),0]) for k in range(5)]
        outer = [Dot([2.8*np.cos(PI/10+k*2*PI/5),2.8*np.sin(PI/10+k*2*PI/5),0]) for k in range(5)]

        vtx = [centre]
        for ls in [outer,middle,inner]:
            vtx.extend(ls)
        self.add_foreground_mobjects(*vtx)

        # these values essentially guide the transformation between copies of the original graph by setting target vertices
        # for outer pentagon
        pts_out_out = [1]
        pts_out_mid = [0]
        pts_out_in = [11,14]
        # for middle pentagon
        pts_mid_mid = [2,3]
        pts_mid_in = [7,8]
        # no transformation for edges within the inner hexagon

        wdth = 1.8 # width for edges
        # edges between outer pentagon and relevant vertices (BLUE)
        edges = []
        for n in range(1,6):
            for crd in pts_out_out:
                end = n%5+crd
                e = Line(vtx[n].get_center(),vtx[end].get_center(),stroke_width = wdth)
                edges.append(e)
            for crd in pts_out_mid:
                end = (n+crd-1)%5+6
                e = Line(vtx[n].get_center(),vtx[end].get_center(),stroke_width = wdth)
                edges.append(e)
            for crd in pts_out_in:
                end = (n+crd-1)%5+11
                e = Line(vtx[n].get_center(),vtx[end].get_center(),stroke_width = wdth)
                edges.append(e)

        # edges between middle pentagon and vertices excluding outer pentagon
        for n in range(6,11):               
            for crd in pts_mid_mid:
                end = (n+crd-1)%5+6
                e = Line(vtx[n].get_center(),vtx[end].get_center(),stroke_width = wdth)
                edges.append(e)
            for crd in pts_mid_in:
                end = (n+crd-1)%5+11
                e = Line(vtx[n].get_center(),vtx[end].get_center(),stroke_width = wdth)
                edges.append(e)

        # edges between inner hexagon and relevant vertices exluding middle and outer pentagons
        for n in range(11,16):
            e = Line(vtx[n].get_center(),vtx[0].get_center(),stroke_width = wdth)
            edges.append(e)

        edges = [e.set_color(BLUE_D) for e in edges]

        # PLAY: fade in vertices, then edges
        self.play(*[FadeIn(v) for v in vtx])
        self.add_foreground_mobjects(*vtx)
        self.play(*[FadeIn(e,run_time=1.5) for e in edges])
        self.wait(1/2)

        # material for first transformation
        # copy of original vertices
        vtx2 = [v.copy() for v in vtx]
        self.add_foreground_mobjects(*vtx2)

        # create targets for copies; note the permutation of the order       
        vtx_targ = [centre.copy()]        
        for ls_of_vtx in [vtx2[11:16],vtx2[1:6],vtx2[6:11]]:
            vtx_targ.extend(ls_of_vtx)
        for v in vtx2:
            v.generate_target()
            v.target.move_to(vtx_targ[vtx2.index(v)])
            
        # edges for first copy (RED)
        edges2 = [e.copy().set_opacity(0) for e in edges]
        # create target for copies using
        edge_targ = []
        for e in edges2:
            start = e.get_start()
            end = e.get_end()
            # this is a little messy because manim seems to struggle with keeping floats consistent passed a certain number of decimal places
            # hence rounding to 4 dp to allow an accurate check for whether vertices are in the same spot (there is probably a nicer way of dealing with this)
            s_target = [v.target for v in vtx2 if [round(x,4) for x in list(start)] == [round(y,4) for y in list(v.get_center())]]
            e_target = [v.target for v in vtx2 if [round(x,4) for x in list(end)] == [round(y,4) for y in list(v.get_center())]]
            line_target = Line(s_target[0],e_target[0],stroke_width = wdth).set_color(RED_D)
            edge_targ.append(line_target)

        # animation for first transformtion
        move_edges = AnimationGroup(*[ReplacementTransform(edges2[k],edge_targ[k]) for k in range(len(edges))])
        move_pts = AnimationGroup(*[MoveToTarget(v) for v in vtx2])

        # PLAY: first transformation
        self.play(move_edges,move_pts,run_time=1.5)

        # material for second transformation; identical to previous other than the permutation
        vtx3 = [v.copy() for v in vtx]
        self.add_foreground_mobjects(*vtx3)
        
        vtx_targ2 = [centre.copy()]        
        for ls in [vtx3[6:11],vtx3[11:16],vtx3[1:6]]:
            vtx_targ2.extend(ls)
        for v in vtx3:
            v.generate_target()
            v.target.move_to(vtx_targ2[vtx3.index(v)])

        edges3 = [e.copy().set_opacity(0) for e in edges]
        edge_targ2 = []
        for e in edges3:
            start = e.get_start()
            end = e.get_end()
            s_target = [v.target for v in vtx3 if [round(x,4) for x in list(start)] == [round(y,4) for y in list(v.get_center())]]
            e_target = [v.target for v in vtx3 if [round(x,4) for x in list(end)] == [round(y,4) for y in list(v.get_center())]]
            line_target = Line(s_target[0],e_target[0],stroke_width = wdth).set_color('#E1E332')
            edge_targ2.append(line_target)

        move_edges2 = AnimationGroup(*[ReplacementTransform(edges3[k],edge_targ2[k]) for k in range(len(edges))])
        move_pts2 = AnimationGroup(*[MoveToTarget(v) for v in vtx3])

        # PLAY: second transformation
        self.play(move_edges2,move_pts2,run_time =1.5)
        self.play(*[FadeOut(o) for o in self.mobjects])
