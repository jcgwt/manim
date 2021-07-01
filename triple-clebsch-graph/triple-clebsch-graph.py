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

        # the following values are parameters for defining the Clebsch graph; they are the base on which the graph bases its symmetries
        
        # for outer pentagon
        pts_out_out = [1]
        pts_out_mid = [0]
        pts_out_in = [11,14]
        # for middle pentagon
        pts_mid_mid = [2,3]
        pts_mid_in = [7,8]
        # no transformation for edges within the inner hexagon

        wdth = 1.8 # width for edges
        # edges between outer pentagon and relevant vertices
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
        
        def transformation(permutation,colour):

            # copy vertices
            vtx_cp = [v.copy() for v in vtx]
            self.add_foreground_mobjects(*vtx_cp)
            # vertex targets
            vtx_targ = [centre.copy()] + [vtx_cp[p] for p in permutation]
            for v in vtx_cp:
                v.generate_target()
                v.target.move_to(vtx_targ[vtx_cp.index(v)])
                
            # edges for copy
            edges_cp = [e.copy().set_opacity(0) for e in edges]
            # create target for copies using
            edge_targ = []
            for e in edges_cp:
                start = e.get_start()
                end = e.get_end()
                # this is a little messy because manim seems to struggle with keeping floats consistent passed a certain number of decimal places
                # hence rounding to 4 dp to allow an accurate check for whether vertices are in the same spot (there is probably a nicer way of dealing with this)
                s_target = [v.target for v in vtx_cp if [round(x,4) for x in list(start)] == [round(y,4) for y in list(v.get_center())]]
                e_target = [v.target for v in vtx_cp if [round(x,4) for x in list(end)] == [round(y,4) for y in list(v.get_center())]]
                line_target = Line(s_target[0],e_target[0],stroke_width = wdth).set_color(colour)
                edge_targ.append(line_target)

            # package animations
            move_edges = AnimationGroup(*[ReplacementTransform(edges_cp[k],edge_targ[k]) for k in range(len(edges))])
            move_pts = AnimationGroup(*[MoveToTarget(v) for v in vtx_cp])

            # PLAY: transformation
            self.play(move_edges,move_pts,run_time=1.5)

        # first transformation
        first_perm = [x for x in range(11,16)]+[x for x in range(1,6)]+[x for x in range(6,11)]
        transformation(first_perm,RED_D)
        
        # second transformation
        scnd_perm = [x for x in range(6,11)]+[x for x in range(11,16)]+[x for x in range(1,6)]
        transformation(scnd_perm,'#E1E332')

        self.play(*[FadeOut(o) for o in self.mobjects])
