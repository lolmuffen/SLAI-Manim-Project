from manim import *

class AndGateSymbol(VMobject):

    def __init__(self, shift_offset=0, rotation=0, scale_factor=1, **kwargs):
        super().__init__(**kwargs)
        self.back_line = Line(UP, DOWN)
        self.front_line = Line(UP + [0.5, 0, 0], DOWN + [0.5, 0, 0], path_arc=-PI)

        self.top_line = Line(self.back_line.get_start(), self.front_line.get_start())
        self.bottom_line = Line(self.back_line.get_end(), self.front_line.get_end())

        self.input_line_top = Line(LEFT + [0, 0.5, 0], ORIGIN + [0, 0.5, 0])
        self.input_line_bottom = Line(LEFT + [0, -0.5, 0], ORIGIN + [0, -0.5, 0])

        self.output_line = Line(RIGHT + [0.5, 0, 0], RIGHT + [1.5, 0, 0] )
        
        self.add(self.back_line, self.front_line, self.bottom_line, self.top_line, self.input_line_top, self.input_line_bottom, self.output_line)
        self.shift(shift_offset).rotate(rotation).scale(scale_factor)


class NotGateSymbol(VMobject):

    def __init__(self, shift_offset=0, rotation=0, scale_factor=1, **kwargs):
        super().__init__(**kwargs)
        self.triangle = Polygon([0, 0.5, 0], [0, -0.5, 0], [1, 0, 0], color=WHITE)
        
        self.bubble = Circle(radius=0.1, color=WHITE).move_to([1.1, 0, 0])
        
        self.input_line = Line(LEFT, ORIGIN)
        self.output_line = Line([1.2, 0, 0], RIGHT + [1, 0, 0])
        
        self.add(self.triangle, self.bubble, self.input_line, self.output_line)
        self.shift(shift_offset).rotate(rotation).scale(scale_factor)


class XorGateSymbol(VMobject):

    def __init__(self, shift_offset=0, rotation=0, scale_factor=1, **kwargs):
        super().__init__(**kwargs)

        self.back_line_inner = Line(UP, DOWN, path_arc=-0.2*PI)
        self.back_line_outer = Line(UP * 0.75, DOWN * 0.75, path_arc=-0.2*PI).shift([-0.25, 0, 0])
        
        self.front_line_top = Line(self.back_line_inner.get_end(), RIGHT * 2, path_arc=0.25*PI)
        self.front_line_bottom = Line(self.back_line_inner.get_start(), RIGHT * 2, path_arc=-0.25*PI)
        
        self.input_line_top = Line(LEFT + [-0.2, 0.5, 0], ORIGIN + [-0.2, 0.5, 0])
        self.input_line_bottom = Line(LEFT + [-0.2, -0.5, 0], ORIGIN + [-0.2, -0.5, 0])

        self.output_line = Line(RIGHT + [1, 0, 0], RIGHT + [2, 0, 0] )

        self.add(self.back_line_inner, self.back_line_outer, self.front_line_top, self.front_line_bottom, self.input_line_top, self.input_line_bottom, self.output_line)
        self.shift(shift_offset).rotate(rotation).scale(scale_factor)


class OrGateSymbol(VMobject):

    def __init__(self, shift_offset=0, rotation=0, scale_factor=1, **kwargs):
        super().__init__(**kwargs)

        self.back_line_inner = Line(UP, DOWN, path_arc=-0.2*PI)
        
        self.front_line_top = Line(self.back_line_inner.get_end(), RIGHT * 2, path_arc=0.25*PI)
        self.front_line_bottom = Line(self.back_line_inner.get_start(), RIGHT * 2, path_arc=-0.25*PI)
        
        self.input_line_top = Line(LEFT + [0.1, 0.5, 0], ORIGIN + [0.1, 0.5, 0])
        self.input_line_bottom = Line(LEFT + [0.1, -0.5, 0], ORIGIN + [0.1, -0.5, 0])

        self.output_line = Line(RIGHT + [1, 0, 0], RIGHT + [2, 0, 0] )

        self.add(self.back_line_inner, self.front_line_top, self.front_line_bottom, self.input_line_top, self.input_line_bottom, self.output_line)
        self.shift(shift_offset).rotate(rotation).scale(scale_factor)


class Transistor(VMobject):
    def __init__(self, line_straight=True, shift_offset=0, rotation=0, scale_factor=1, invert_letters=False, **kwargs):
        super().__init__(**kwargs)
        self.left_rectangle = Rectangle(width=1,height=1,fill_opacity=.5,color=RED)
        self.right_rectangle = Rectangle(width=1,height=1,fill_opacity=.5,color=RED)
        self.middle_rectangle = Rectangle(width=3,height=1,color=BLUE_B,fill_opacity=0.2)
        if not invert_letters:
            self.left_text = Text("N")
            self.right_text = Text("N")
            self.middle_text = Text("P")
        else:
            self.left_text = Text("P")
            self.right_text = Text("P")
            self.middle_text = Text("N")
            self.middle_rectangle.set_color(color=RED)
            self.right_rectangle.set_color(color=BLUE_B)
            self.left_rectangle.set_color(color=BLUE_B)

        if line_straight:
            self.left_line = Line([-2,0.5,0],[-2,3,0])
            self.right_line = Line([2,0.5,0],[2,3,0])

        else: 
            self.left_line = Line([-2,0.5,0],[-2,0.75,0])
            self.right_line = Line([2,0.5,0],[2,0.75,0])
            self.left_horz_line = Line([-2,0.75,0],[-4, 0.75, 0])
            self.right_horz_line = Line([2,0.75,0], [4, 0.75, 0])
            self.add(self.left_horz_line,self.right_horz_line)


        self.gate_middle_line = Line([0,.75,0],[0,2,0])
        self.gate_bottom_line = Line([-1.5,.75,0],[1.5,.75,0])

        self.left_rectangle.move_to(LEFT*2)
        self.right_rectangle.move_to(RIGHT*2)
        self.left_text.move_to(self.left_rectangle.get_center())
        self.right_text.move_to(self.right_rectangle.get_center())
        self.middle_text.move_to(self.middle_rectangle.get_center())

        self.add(self.left_rectangle, self.right_rectangle, self.middle_rectangle, self.left_text, self.right_text, self.middle_text, self.left_line, self.right_line, self.gate_middle_line, self.gate_bottom_line)

        self.shift(shift_offset).rotate(rotation).scale(scale_factor)


class Play(Scene):
    def construct(self):
        transistor = Transistor(line_straight=True)
        self.play(Create(transistor))
        transistorText = Text("MOSFET TRANSISTOR")
        transistorText.move_to(DOWN)
        self.play(FadeIn(transistorText))

        #END SCENE 1
        #############################################################

        self.wait(1)#14

        TCT = Text("Silicon to Software", font_size=72,).shift([1.25,-.5,0])

        self.play(transistor.animate().scale(.5).move_to([-4.5,0,0]), FadeOut(transistorText), FadeIn(TCT), lag_ratio=0.25)

        self.wait(1)

        self.play(FadeOut(TCT), lag_ratio=0.25)

        not_gate_text = Text("NOT").shift([-5,3,0])
        or_gate_text = Text("OR").shift([-2,3,0])
        and_gate_text = Text("AND").shift([2,3,0])
        xor_gate_text = Text("XOR").shift([5,3,0])

        gate_text_anims = [FadeIn(not_gate_text), FadeIn(or_gate_text), FadeIn(and_gate_text),FadeIn(xor_gate_text)]
       
        not_gate = VGroup()
        not_gate_transistor = Transistor(line_straight=False, shift_offset=[-5,-1,0], scale_factor=0.25, rotation=PI/2, invert_letters=True)
        not_gate.add(not_gate_transistor)

        not_gate_io_text = [Text("A", font_size=16).shift(not_gate_transistor.gate_middle_line.get_end() + [0, 0.2, 0]), 
                            Text("Out", font_size=16).shift(not_gate_transistor.right_horz_line.get_end() + [-0.25, -0.1, 0])]
        
        self.play(*gate_text_anims)

        self.play(FadeOut(transistor), FadeIn(not_gate_transistor), *[Create(anim) for anim in not_gate_io_text])

        self.play(AnimationGroup(
            AnimationGroup(
                Indicate(not_gate_transistor.gate_middle_line, color=YELLOW, run_time=5), 
                Indicate(not_gate_transistor.gate_bottom_line, color=YELLOW, run_time=5),
                ),
            AnimationGroup( 
                Indicate(not_gate_transistor.left_horz_line),
                Indicate(not_gate_transistor.left_line),
                Indicate(not_gate_transistor.left_text), 
                Indicate(not_gate_transistor.left_rectangle),
                Indicate(not_gate_transistor.middle_text, color=RED), 
                Indicate(not_gate_transistor.middle_rectangle, color=RED),
                lag_ratio=.2,
                run_time=3
                ),
            lag_ratio = .25,
            run_time=6
            )
            )
        

        or_gate = VGroup()
        or_gate_transistor = Transistor(line_straight=False, shift_offset=[-2,-1.5,0], scale_factor=0.25, rotation=PI/2)         
        or_gate_transistor1 = Transistor(line_straight=False, shift_offset=[-2,0.5,0], scale_factor=0.25, rotation=PI/2)  
        or_gate_around_line1 = Line(or_gate_transistor.left_horz_line.get_end() + [0, 0, 0], or_gate_transistor.left_horz_line.get_end() + [1, 0, 0])
        or_gate_around_line2 = Line(or_gate_transistor.right_horz_line.get_end() + [-1, 0, 0], or_gate_transistor.right_horz_line.get_end() + [0, 0, 0])
        or_gate_around_line3 = Line(or_gate_transistor1.right_horz_line.get_end() + [0, -0.25, 0], or_gate_transistor1.right_horz_line.get_end() + [1, -0.25, 0])
        or_gate_around_line4 = Line(or_gate_transistor.left_horz_line.get_end() + [1, 0, 0], or_gate_transistor1.right_horz_line.get_end() + [1, -0.25, 0])
        or_gate_io_text = [Text("A", font_size=16).shift(or_gate_transistor.gate_middle_line.get_end() + [0, 0.2, 0]), 
                           Text("B", font_size=16).shift(or_gate_transistor1.gate_middle_line.get_end() + [0, 0.2, 0]), 
                           Text("Out", font_size=16).shift(or_gate_transistor1.right_horz_line.get_end() + [0.25, 0, 0])]   

        or_gate.add(or_gate_transistor, or_gate_transistor1, or_gate_around_line1, or_gate_around_line2, or_gate_around_line3, or_gate_around_line4, *or_gate_io_text)

        self.play(FadeIn(or_gate_transistor1), FadeIn(or_gate_transistor), FadeIn(or_gate_around_line1), FadeIn(or_gate_around_line2), FadeIn(or_gate_around_line3), FadeIn(or_gate_around_line4), *[Create(anim) for anim in or_gate_io_text])

        self.play(AnimationGroup(
            AnimationGroup(
                Indicate(or_gate_transistor.gate_bottom_line, run_time = 5),
                Indicate(or_gate_transistor.gate_middle_line, run_time = 5),
                Indicate(or_gate_transistor1.gate_bottom_line, run_time = 5),
                Indicate(or_gate_transistor1.gate_middle_line, run_time = 5),
            ),
            AnimationGroup(
                Indicate(or_gate_around_line2),
                AnimationGroup(
                    Indicate(or_gate_transistor.right_horz_line),
                    Indicate(or_gate_transistor.right_line),
                    Indicate(or_gate_transistor.right_rectangle),
                    Indicate(or_gate_transistor.middle_rectangle),
                    Indicate(or_gate_transistor.left_rectangle),
                    Indicate(or_gate_transistor.left_line),
                    Indicate(or_gate_transistor.left_horz_line),
                    Indicate(or_gate_around_line1),
                    Indicate(or_gate_around_line4),
                    Indicate(or_gate_around_line3),
                lag_ratio=.2,
                run_time=3
                ),
               AnimationGroup(
                    Indicate(or_gate_transistor1.left_horz_line),
                    Indicate(or_gate_transistor1.left_line),
                    Indicate(or_gate_transistor1.left_rectangle),
                    Indicate(or_gate_transistor1.middle_rectangle),
                    Indicate(or_gate_transistor1.right_rectangle),
                    Indicate(or_gate_transistor1.right_line),
                    Indicate(or_gate_transistor1.right_horz_line),

                lag_ratio=.2,
                run_time=3
                ),
            ),
        lag_ratio=.25,
        run_time=5
        )
        )
        and_gate = VGroup()
        and_gate_transistor = Transistor(line_straight=False, shift_offset=[2,-1.5,0], scale_factor=0.25, rotation=PI/2)         
        and_gate_transistor1 = Transistor(line_straight=False, shift_offset=[2,0.5,0], scale_factor=0.25, rotation=PI/2)
        and_gate_io_text = [Text("A", font_size=16).shift(and_gate_transistor.gate_middle_line.get_end() + [0, 0.2, 0]), 
                           Text("B", font_size=16).shift(and_gate_transistor1.gate_middle_line.get_end() + [0, 0.2, 0]), 
                           Text("Out", font_size=16).shift(and_gate_transistor1.right_horz_line.get_end() + [0.25, 0.25, 0])]

        and_gate.add(and_gate_io_text, and_gate_transistor, and_gate_transistor1)

        self.play(FadeIn(and_gate_transistor1), FadeIn(and_gate_transistor), *[Create(anim) for anim in and_gate_io_text])
        self.play(AnimationGroup(
            AnimationGroup(
                Indicate(and_gate_transistor.gate_bottom_line, run_time=5),
                Indicate(and_gate_transistor.gate_middle_line, run_time=5),
                Indicate(and_gate_transistor1.gate_bottom_line, run_time=5),
                Indicate(and_gate_transistor1.gate_middle_line, run_time=5),
                           ),
            AnimationGroup(
                Indicate(and_gate_transistor.left_horz_line),
                Indicate(and_gate_transistor.left_line),
                Indicate(and_gate_transistor.left_rectangle),
                Indicate(and_gate_transistor.middle_rectangle),
                Indicate(and_gate_transistor.right_rectangle),
                Indicate(and_gate_transistor.right_line),
                Indicate(and_gate_transistor.right_horz_line),
                Indicate(and_gate_transistor1.left_horz_line),
                Indicate(and_gate_transistor1.left_line),
                Indicate(and_gate_transistor1.left_rectangle),
                Indicate(and_gate_transistor1.middle_rectangle),
                Indicate(and_gate_transistor1.right_rectangle),
                Indicate(and_gate_transistor1.right_line),
                Indicate(and_gate_transistor1.right_horz_line),
                run_time=3,
                lag_ratio=.2,
            ),
        lag_ratio = .25,
        run_time=6
        ), 
        )
        xor_gate = VGroup()
        or_xor = VGroup()

        xor_gate_transistor = Transistor(line_straight=False, shift_offset=[5,-1.5,0], scale_factor=0.25, rotation=PI/2)         
        xor_gate_transistor1 = Transistor(line_straight=False, shift_offset=[5,0.5,0], scale_factor=0.25, rotation=PI/2)

        or_xor.add(xor_gate_transistor, xor_gate_transistor1)
        or_xor.scale(0.75).shift([-.5, 0.5, 0])

        and_xor = VGroup()
        xor_gate.add(and_xor, or_xor)
        xor_gate_transistor2 = Transistor(line_straight=False, shift_offset=[5,-1.5,0], scale_factor=0.25, rotation=PI/2)         
        xor_gate_transistor3 = Transistor(line_straight=False, shift_offset=[5,0.5,0], scale_factor=0.25, rotation=PI/2)  
        xor_gate_around_line1 = Line(xor_gate_transistor2.left_horz_line.get_end() + [0, 0.25, 0], xor_gate_transistor2.left_horz_line.get_end() + [1, 0.25, 0])
        xor_gate_around_line2 = Line(xor_gate_transistor2.right_horz_line.get_end() + [-0.6, 0, 0], xor_gate_transistor2.right_horz_line.get_end() + [0, 0, 0])
        xor_gate_around_line3 = Line(xor_gate_transistor3.right_horz_line.get_end() + [0, 0, 0], xor_gate_transistor3.right_horz_line.get_end() + [1, 0, 0])
        xor_gate_around_line4 = Line(xor_gate_transistor2.left_horz_line.get_end() + [1, 0.25, 0], xor_gate_transistor3.right_horz_line.get_end() + [1, 0, 0])
        and_to_or = Line(xor_gate_transistor1.right_horz_line.get_end() + [-0.04, 0, 0], xor_gate_transistor1.right_horz_line.get_end() + [-0.04, -2, 0])

        a_inputs_horz_line = Line(xor_gate_transistor2.gate_middle_line.get_end(), xor_gate_transistor2.gate_middle_line.get_end() + [-1.5, 0, 0])
        b_inputs_horz_line = Line(xor_gate_transistor3.gate_middle_line.get_end(), xor_gate_transistor3.gate_middle_line.get_end() + [-1, 0, 0])

        a_inputs_vert_line = Line(a_inputs_horz_line.get_end(), a_inputs_horz_line.get_end() + [0, 3.57, 0])
        b_inputs_vert_line = Line(b_inputs_horz_line.get_end(), b_inputs_horz_line.get_end() + [0, 3.57, 0])

        a_inputs_horz_line_top = Line(a_inputs_vert_line.get_end(), a_inputs_vert_line.get_end() + [1, 0, 0])
        b_inputs_horz_line_top = Line(b_inputs_vert_line.get_end(), b_inputs_vert_line.get_end() + [0.5, 0, 0])
        
        xor_gate_io_text = [Text("A", font_size=16).shift(xor_gate_transistor.gate_middle_line.get_end() + [0, 0.2, 0]), 
                           Text("B", font_size=16).shift(xor_gate_transistor1.gate_middle_line.get_end() + [0, 0.2, 0]), 
                           Text("Out", font_size=16).shift([5.25, -3.4, 0])]

        and_xor.add(xor_gate_transistor2, 
                    xor_gate_transistor3, 
                    xor_gate_around_line1, 
                    xor_gate_around_line2, 
                    xor_gate_around_line3, 
                    xor_gate_around_line4, 
                    and_to_or, 
                    a_inputs_horz_line, 
                    b_inputs_horz_line, 
                    a_inputs_vert_line, 
                    b_inputs_vert_line, 
                    a_inputs_horz_line_top, 
                    b_inputs_horz_line_top)

        
        
        and_xor.scale(0.75).shift([0, -2.5, 0])

        self.play(FadeIn(or_xor), FadeIn(and_xor), *[Create(anim) for anim in xor_gate_io_text])

        #add more animation here

        self.play(*[FadeOut(anim) for anim in xor_gate_io_text], 
                  *[FadeOut(anim) for anim in not_gate_io_text]
                  )

##################################################################
#END ACT 3

        orGate = OrGateSymbol(scale_factor=0.5, shift_offset=[-3, 0, 0])
        andGate = AndGateSymbol(scale_factor=.5, shift_offset=[1.5, 0, 0])
        notGate = NotGateSymbol(shift_offset=[-5.5, 0, 0], scale_factor=.75)
        xorGate = XorGateSymbol(shift_offset=[4.25, 0, 0], scale_factor=.5)

        self.play(ReplacementTransform(and_gate, andGate), 
                  ReplacementTransform(or_gate, orGate), 
                  ReplacementTransform(not_gate, notGate), 
                  ReplacementTransform(xor_gate, xorGate))
        self.wait(1)
        self.play(orGate.animate().scale(.75).shift([0, 1, 0]), 
                  andGate.animate().scale(.75).shift([0, 1, 0]), 
                  notGate.animate().scale(.75).shift([0, 1, 0]), 
                  xorGate.animate().scale(.75).shift([0, 1, 0]))
        
        not_table = Table(
            [["0", "1"],
             ["1", "0"]],
            col_labels=[Text("A"), Text("Out")],
            include_outer_lines=True,
        ).scale(0.3).shift([-5, -.7, 0])

        or_table = Table(
            [["0", "0", "0"],
             ["0", "1", "1"],
             ["1", "0", "1"],
             ["1", "1", "1"]],
            col_labels=[Text("A"), Text("B"), Text("Out")],
            include_outer_lines=True,
        ).scale(0.3).shift([-2, -1, 0])

        and_table = Table(
                    [["0", "0", "0"],
                    ["0", "1", "0"],
                    ["1", "0", "0"],
                    ["1", "1", "1"]],
                    col_labels=[Text("A"), Text("B"), Text("Out")],
                    include_outer_lines=True,
                ).scale(0.3).shift([2.25, -1, 0])

        xor_table = Table(
            [["0", "0", "0"],
             ["0", "1", "1"],
             ["1", "0", "1"],
             ["1", "1", "0"]],
            col_labels=[Text("A"), Text("B"), Text("Out")],
            include_outer_lines=True,
        ).scale(0.3).shift([5, -1, 0])


        self.play(FadeIn(or_table), FadeIn(and_table), FadeIn(xor_table), FadeIn(not_table))

        self.wait(2)

        self.play(FadeOut(or_table), FadeOut(and_table), FadeOut(xor_table), FadeOut(not_table), 
                  FadeOut(orGate), FadeOut(andGate), FadeOut(notGate), FadeOut(xorGate),
                  FadeOut(not_gate_text), FadeOut(or_gate_text), FadeOut(and_gate_text), FadeOut(xor_gate_text))
#######################################################################
#END ACT 5

        self.wait(1)
        sequential_text = Text("Combintational vs Sequential", font_size=60).shift([0, 1, 0])
        self.play(FadeIn(sequential_text))
        
        ha_xor_gate = XorGateSymbol(shift_offset=[-3, -.75, 0], scale_factor=0.5)
        ha_and_gate = AndGateSymbol(shift_offset=[-3, -2, 0], scale_factor=0.5)

        vert_input_line_A = Line(ha_and_gate.input_line_top.get_start(), ha_and_gate.input_line_top.get_start() + [0, .75, 0])
        vert_input_line_B = Line(ha_and_gate.input_line_bottom.get_start() + [-0.25, 0, 0], ha_and_gate.input_line_bottom.get_start() + [-0.25, 1.75, 0])
        horz_input_line_A_bottom = Line(ha_and_gate.input_line_bottom.get_start() + [-0.25, 0, 0], ha_and_gate.input_line_bottom.get_start())

        horz_input_line_A = Line(vert_input_line_A.get_end(), vert_input_line_A.get_end() + [-1, 0, 0])
        horz_input_line_B = Line(ha_xor_gate.input_line_top.get_start(), ha_xor_gate.input_line_top.get_end() + [-1.5, 0, 0])

        self.play(FadeIn(ha_xor_gate), 
                  FadeIn(ha_and_gate), 
                  FadeIn(vert_input_line_A), 
                  FadeIn(vert_input_line_B), 
                  FadeIn(horz_input_line_A), 
                  FadeIn(horz_input_line_B), 
                  FadeIn(horz_input_line_A_bottom))

        seq_or_gate = OrGateSymbol(shift_offset=[3, -1.5, 0], scale_factor=0.5)
        seq_or_extention = Line(seq_or_gate.output_line.get_end(), seq_or_gate.output_line.get_end() + [1, 0, 0])