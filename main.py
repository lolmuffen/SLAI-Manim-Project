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

        self.output_line = Line(RIGHT + [0.5, 0, 0], RIGHT + [1.5, 0, 0])

        self.add(
            self.back_line,
            self.front_line,
            self.bottom_line,
            self.top_line,
            self.input_line_top,
            self.input_line_bottom,
            self.output_line,
        )
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

        self.back_line_inner = Line(UP, DOWN, path_arc=-0.2 * PI)
        self.back_line_outer = Line(UP * 0.75, DOWN * 0.75, path_arc=-0.2 * PI).shift(
            [-0.25, 0, 0]
        )

        self.front_line_top = Line(
            self.back_line_inner.get_end(), RIGHT * 2, path_arc=0.25 * PI
        )
        self.front_line_bottom = Line(
            self.back_line_inner.get_start(), RIGHT * 2, path_arc=-0.25 * PI
        )

        self.input_line_top = Line(LEFT + [-0.2, 0.5, 0], ORIGIN + [-0.2, 0.5, 0])
        self.input_line_bottom = Line(LEFT + [-0.2, -0.5, 0], ORIGIN + [-0.2, -0.5, 0])

        self.output_line = Line(RIGHT + [1, 0, 0], RIGHT + [2, 0, 0])

        self.add(
            self.back_line_inner,
            self.back_line_outer,
            self.front_line_top,
            self.front_line_bottom,
            self.input_line_top,
            self.input_line_bottom,
            self.output_line,
        )
        self.shift(shift_offset).rotate(rotation).scale(scale_factor)


class OrGateSymbol(VMobject):
    def __init__(self, shift_offset=0, rotation=0, scale_factor=1, **kwargs):
        super().__init__(**kwargs)

        self.back_line_inner = Line(UP, DOWN, path_arc=-0.2 * PI)

        self.front_line_top = Line(
            self.back_line_inner.get_end(), RIGHT * 2, path_arc=0.25 * PI
        )
        self.front_line_bottom = Line(
            self.back_line_inner.get_start(), RIGHT * 2, path_arc=-0.25 * PI
        )

        self.input_line_top = Line(LEFT + [0.1, 0.5, 0], ORIGIN + [0.1, 0.5, 0])
        self.input_line_bottom = Line(LEFT + [0.1, -0.5, 0], ORIGIN + [0.1, -0.5, 0])

        self.output_line = Line(RIGHT + [1, 0, 0], RIGHT + [2, 0, 0])

        self.add(
            self.back_line_inner,
            self.front_line_top,
            self.front_line_bottom,
            self.input_line_top,
            self.input_line_bottom,
            self.output_line,
        )
        self.shift(shift_offset).rotate(rotation).scale(scale_factor)


class HalfAdder(VMobject):
    def __init__(self, shift_offset=0, rotation=0, scale_factor=1, **kwargs):
        super().__init__(**kwargs)
        self.ha_xor_gate = XorGateSymbol(shift_offset=[0, -0.75, 0], scale_factor=0.5)
        self.ha_and_gate = AndGateSymbol(shift_offset=[0, -2, 0], scale_factor=0.5)

        self.vert_input_line_A = Line(
            self.ha_and_gate.input_line_top.get_start(),
            self.ha_and_gate.input_line_top.get_start() + [0, 0.75, 0],
        )
        self.vert_input_line_B = Line(
            self.ha_and_gate.input_line_bottom.get_start() + [-0.25, 0, 0],
            self.ha_and_gate.input_line_bottom.get_start() + [-0.25, 1.75, 0],
        )
        self.horz_input_line_A_bottom = Line(
            self.ha_and_gate.input_line_bottom.get_start() + [-0.25, 0, 0],
            self.ha_and_gate.input_line_bottom.get_start(),
        )

        self.horz_input_line_A = Line(
            self.vert_input_line_A.get_end(),
            self.vert_input_line_A.get_end() + [-1, 0, 0],
        )
        self.horz_input_line_B = Line(
            self.ha_xor_gate.input_line_top.get_start(),
            self.ha_xor_gate.input_line_top.get_end() + [-1.5, 0, 0],
        )

        self.add(
            self.ha_xor_gate,
            self.ha_and_gate,
            self.vert_input_line_A,
            self.vert_input_line_B,
            self.horz_input_line_A,
            self.horz_input_line_B,
            self.horz_input_line_A_bottom,
        )
        self.shift(shift_offset).rotate(rotation).scale(scale_factor)


class Transistor(VMobject):
    def __init__(
        self,
        line_straight=True,
        shift_offset=0,
        rotation=0,
        scale_factor=1,
        invert_letters=False,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.left_rectangle = Rectangle(width=1, height=1, fill_opacity=0.5, color=RED)
        self.right_rectangle = Rectangle(width=1, height=1, fill_opacity=0.5, color=RED)
        self.middle_rectangle = Rectangle(
            width=3, height=1, color=BLUE_B, fill_opacity=0.2
        )
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
            self.left_line = Line([-2, 0.5, 0], [-2, 3, 0])
            self.right_line = Line([2, 0.5, 0], [2, 3, 0])

        else:
            self.left_line = Line([-2, 0.5, 0], [-2, 0.75, 0])
            self.right_line = Line([2, 0.5, 0], [2, 0.75, 0])
            self.left_horz_line = Line([-2, 0.75, 0], [-4, 0.75, 0])
            self.right_horz_line = Line([2, 0.75, 0], [4, 0.75, 0])
            self.add(self.left_horz_line, self.right_horz_line)

        self.gate_middle_line = Line([0, 0.75, 0], [0, 2, 0])
        self.gate_bottom_line = Line([-1.5, 0.75, 0], [1.5, 0.75, 0])

        self.left_rectangle.move_to(LEFT * 2)
        self.right_rectangle.move_to(RIGHT * 2)
        self.left_text.move_to(self.left_rectangle.get_center())
        self.right_text.move_to(self.right_rectangle.get_center())
        self.middle_text.move_to(self.middle_rectangle.get_center())

        self.add(
            self.left_rectangle,
            self.right_rectangle,
            self.middle_rectangle,
            self.left_text,
            self.right_text,
            self.middle_text,
            self.left_line,
            self.right_line,
            self.gate_middle_line,
            self.gate_bottom_line,
        )

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
        sceneVGroup = VGroup()
        self.wait(1)
        sequential_text = Text("Combintational vs Sequential", font_size=60).shift(
            [0, 1, 0]
        )
        self.play(FadeIn(sequential_text))

        half_adder = HalfAdder(shift_offset=[-3, 0, 0], scale_factor=0.75)
        self.play(FadeIn(half_adder))

        seq_or_gate_group = VGroup()
        seq_or_gate = OrGateSymbol(shift_offset=[2, -1, 0], scale_factor=0.5)
        seq_or_extention = Line(
            seq_or_gate.output_line.get_end(),
            seq_or_gate.output_line.get_end() + [1, 0, 0],
        )
        seq_vertical_line_front = Line(
            seq_or_gate.output_line.get_end(),
            seq_or_gate.output_line.get_end() + [0, -1, 0],
        )
        seq_back_line = Line(
            seq_vertical_line_front.get_end(),
            seq_vertical_line_front.get_end() + [-1.95, 0, 0],
        )
        seq_vertical_line_back = Line(
            seq_back_line.get_end(), seq_back_line.get_end() + [0, 0.75, 0]
        )
        seq_or_gate_group.add(
            seq_or_gate,
            seq_or_extention,
            seq_vertical_line_front,
            seq_back_line,
            seq_vertical_line_back,
        )

        self.play(FadeIn(seq_or_gate_group))

        self.wait(1)

        self.play(
            FadeOut(sequential_text), FadeOut(half_adder), FadeOut(seq_or_gate_group)
        )

        sceneVGroup.add(half_adder, seq_or_gate_group, sequential_text)

        #################################################################################################################
        # END ACT 6
        decimal_text = Text("Decimal", font_size=54).shift([-2, 2, 0])
        binary_text = Text("Binary", font_size=54).shift([2, 2, 0])

        decimal_table = VGroup(Square(1).shift([-1.5, 0, 0]), Square(1).shift([-2.5, 0, 0]))
        binary_table = VGroup(Square(1).shift([1.5, 0, 0]), Square(1).shift([2.5, 0, 0]))

        binary_number = Text("1").move_to([2.5, 0, 0])
        decimal_number = Text("9").move_to([-1.5, 0, 0])

        decimal_value = Text(f"Value: nine").move_to([-2, -2, 0])
        binary_value = Text(f"Value: one").move_to([2, -2, 0])

        self.play(FadeIn(decimal_text),
                    FadeIn(binary_text),
                    FadeIn(decimal_table),
                    FadeIn(binary_table),
                    FadeIn(binary_number),
                    FadeIn(decimal_number),
                    FadeIn(decimal_value),
                    FadeIn(binary_value))

        self.wait(2)

        plus_one_text_binary = Text("+1", font_size=54).shift([2.5, -1, 0])
        plus_one_text_decimal = Text("+1", font_size=54).shift([-1.5, -1, 0])

        self.play(FadeIn(plus_one_text_binary),
                    plus_one_text_binary.animate().shift([0, 1, 0]),
                    binary_number.animate().shift([-1, 0, 0]),
                    ReplacementTransform(binary_value, Text("Value: two").move_to([2, -2, 0])),
                    FadeIn(Text("0").shift([2.5, 0, 0])),

                    run_time = 0.75
                    )

        self.play(FadeOut(plus_one_text_binary), run_time=0.25)
        self.play(Indicate(binary_value))

        self.wait(1)

        self.play(FadeIn(plus_one_text_decimal),
                    plus_one_text_decimal.animate().shift([0, 1, 0]),
                    decimal_number.animate().shift([-1, 0, 0]),
                    Transform(decimal_number, Text("1").move_to([-2.5, 0, 0])),
                    ReplacementTransform(decimal_value, Text("Value: ten").move_to([-2, -2, 0])),
                    FadeIn(Text("0").shift([-1.5, 0, 0])),
                    run_time = 0.75

                )

        self.play(FadeOut(plus_one_text_decimal), run_time=0.25)
        self.play(Indicate(decimal_value))

        self.wait(1)

        self.play(FadeOut(*self.mobjects))

##############################################################################################
# END ACT 7
        IntroAdderVGroup = VGroup()
        Introadder_4_bitRect = Rectangle(width=3, height=3)
        Introadder_4_bitText = Text("4 Bit Adder", font_size=36)
        Introadder_4_bitInLine1 = Line([-1.5, 0, 0], [-3, 0, 0])
        Introadder_4_bitInLine2 = Line([-1.5, 0.25, 0], [-3, 0.25, 0])
        Introadder_4_bitInLine3 = Line([-1.5, 0.5, 0], [-3, 0.5, 0])
        Introadder_4_bitInLine4 = Line([-1.5, 0.75, 0], [-3, 0.75, 0])
        Introadder_4_bitInLine5 = Line([-1.5, 1, 0], [-3, 1, 0])
        Introadder_4_bitInLine6 = Line([-1.5, -0.25, 0], [-3, -0.25, 0])
        Introadder_4_bitInLine7 = Line([-1.5, -0.5, 0], [-3, -0.5, 0])
        Introadder_4_bitInLine8 = Line([-1.5, -0.75, 0], [-3, -0.75, 0])
        Introadder_4_bitInLine9 = Line([-1.5, -1.25, 0], [-3, -1.25, 0])
        IntroAddedLines = [
            Introadder_4_bitInLine1,
            Introadder_4_bitInLine2,
            Introadder_4_bitInLine3,
            Introadder_4_bitInLine4,
            Introadder_4_bitInLine5,
            Introadder_4_bitInLine6,
            Introadder_4_bitInLine7,
            Introadder_4_bitInLine8,
            Introadder_4_bitInLine9,
        ]
        IntroAdder4BitOutLine1 = Line([1.5, -1, 0], [3, -1, 0])
        IntroAdder4BitOutLine2 = Line([1.5, -0.75, 0], [3, -0.75, 0])
        IntroAdder4BitOutLine3 = Line([1.5, -0.5, 0], [3, -0.5, 0])
        IntroAdder4BitOutLine4 = Line([1.5, -0.25, 0], [3, -0.25, 0])

        IntroAdder4BitCarry = Line([1.5, 1, 0], [3, 1, 0])

        half_add_table = (
            Table(
                [
                    ["0", "0", "0", "0"],
                    ["0", "1", "1", "0"],
                    ["1", "0", "1", "0"],
                    ["1", "1", "0", "1"],
                ],
                col_labels=[Text("A"), Text("B"), Text("Sum"), Text("Carry")],
                include_outer_lines=True,
            )
            .scale(0.5)
            .shift([-3, 0, 0])
        )

        IntroAdder4BitOutLines = [
            IntroAdder4BitOutLine1,
            IntroAdder4BitOutLine2,
            IntroAdder4BitOutLine3,
            IntroAdder4BitOutLine4,
            IntroAdder4BitCarry,
        ]

        IntroAdderVGroup.add(
            *IntroAddedLines,
            Introadder_4_bitRect,
            Introadder_4_bitText,
            *IntroAdder4BitOutLines,
        )
        self.play(Create(IntroAdderVGroup), run_time=3)

        self.wait(0.5)

        self.play(
            IntroAdderVGroup.animate.scale(250).shift([-5, -5, 0]),
            rate_func=rush_into,
            run_time=1.5,
        )
        self.play(FadeOut(IntroAdderVGroup))

        HAVGroup = VGroup()

        halfAdderTitle = Text("Half Adder", font_size=52).shift([0, 3, 0])

        half_adder = HalfAdder(shift_offset=[2, 1, 0])
        HAVGroup.add(halfAdderTitle, half_add_table)
        self.play(Create(half_adder), FadeIn(half_add_table), Create(halfAdderTitle))
        self.wait(3)

        self.play(FadeOut(HAVGroup), half_adder.animate().move_to([-2.625, 0.625, 0]))

        ###############################################################################################
        # END ACT 8

        FAVGroup = VGroup()

        half_adder_left = half_adder
        half_adder_right = HalfAdder(shift_offset=[7, 1, 0])
        carry_or_gate = OrGateSymbol(shift_offset=[3, 2, 0], scale_factor=0.5)

        self.play(
            FadeIn(half_adder_right),
            half_adder_right.animate().shift([-6, 0, 0]),
            FadeIn(carry_or_gate),
        )

        sum_to_A_vert = Line(
            half_adder_right.horz_input_line_B.get_end() + [0, 0, 0],
            half_adder_right.horz_input_line_B.get_end() + [0, 0.75, 0],
        )

        sum_to_A_horz = Line(
            sum_to_A_vert.get_end(), sum_to_A_vert.get_end() + [-1, 0, 0]
        )

        carry_from_left_vert = Line(
            half_adder_left.ha_and_gate.output_line.get_end() + [0, 0, 0],
            half_adder_left.ha_and_gate.output_line.get_end() + [0, 2.25, 0],
        )

        carry_from_left_horz = Line(
            carry_from_left_vert.get_end(), carry_from_left_vert.get_end() + [4.5, 0, 0]
        )

        carry_in_horz = Line([-4, -1, 0], [-0.1, -1, 0])
        carry_in_vert = Line(
            carry_in_horz.get_end(), carry_in_horz.get_end() + [0, 1, 0]
        )

        sum_out_line = Line(
            half_adder_right.ha_xor_gate.output_line.get_end() + [0, 0, 0],
            half_adder_right.ha_xor_gate.output_line.get_end() + [2, 0, 0],
        )

        carry_from_right_horz = Line(
            half_adder_right.ha_and_gate.output_line.get_end() + [0, 0, 0],
            half_adder_right.ha_and_gate.output_line.get_end() + [0.5, 0, 0],
        )

        carry_from_right_vert = Line(
            carry_from_right_horz.get_end(),
            carry_from_right_horz.get_end() + [0, 2.75, 0],
        )

        self.play(
            FadeIn(sum_to_A_vert),
            FadeIn(sum_to_A_horz),
            FadeIn(carry_from_left_vert),
            FadeIn(carry_from_left_horz),
            FadeIn(carry_in_horz),
            FadeIn(carry_in_vert),
            FadeIn(sum_out_line),
            FadeIn(carry_from_right_horz),
            FadeIn(carry_from_right_vert),
        )

        self.wait(1)

        FAVGroup.add(
            half_adder_left,
            half_adder_right,
            carry_or_gate,
            sum_to_A_vert,
            sum_to_A_horz,
            carry_from_left_vert,
            carry_from_left_horz,
            carry_in_horz,
            carry_in_vert,
            sum_out_line,
            carry_from_right_horz,
            carry_from_right_vert,
        )

        self.play(
            FAVGroup.animate.scale(0.004),
            FadeIn(IntroAdderVGroup),
            FadeOut(FAVGroup),
            IntroAdderVGroup.animate.scale(0.004).shift([5, 5, 0]),
            run_time=1.5,
            rate_func=linear,
        )
        self.wait(1)

        # ########################################################################################
        # #end act 10

        sceneVGroup.move_to([11, 0, 0])

        self.play(
            IntroAdderVGroup.animate().shift([-11, 0, 0]),
            FadeIn(sceneVGroup),
            sceneVGroup.animate().move_to([0, 0, 0]),
            run_time=1.5,
            rate_func=linear,
        )

        self.play(FadeOut(IntroAdderVGroup), FadeOut(sceneVGroup))
        seq_text = Text("Sequential", font_size=72).shift([0.5, 2, 0])

        self.play(FadeIn(seq_text), FadeIn(seq_or_gate_group.move_to([1, 0, 0])))
        self.wait(2)
        self.play(
            FadeOut(seq_text),
            FadeOut(seq_or_gate_group),
        )

        ##############################################################################
        # END ACT 11

        SrLatchVGroup = VGroup()

        sr_latch_and_gate = AndGateSymbol(scale_factor=0.5, shift_offset=[2, 0, 0])
        sr_latch_or_gate = OrGateSymbol(scale_factor=0.5, shift_offset=[-2, 1, 0])
        sr_latch_not_gate = NotGateSymbol(shift_offset=[-1.5, -1, 0], scale_factor=0.5)

        sr_latch_set_line_input = Line(sr_latch_or_gate.input_line_bottom.get_end() + [-2, 0, 0], sr_latch_or_gate.input_line_bottom.get_start() + [0, 0, 0])
        sr_latch_or_and_horz = Line(sr_latch_or_gate.output_line.get_end() + [0, 0, 0], sr_latch_or_gate.output_line.get_end() + [1.85, 0, 0])
        sr_latch_or_and_vert = Line(sr_latch_or_and_horz.get_end(), sr_latch_or_and_horz.get_end() + [0, -.75, 0])

        sr_latch_loop_line_vert = Line(sr_latch_and_gate.output_line.get_end() + [0, 0, 0], sr_latch_and_gate.output_line.get_end() + [0, 2, 0])
        sr_latch_loop_line_horz = Line(sr_latch_loop_line_vert.get_end(), sr_latch_loop_line_vert.get_end() + [-5.55, 0, 0])
        sr_latch_loop_line = Line(sr_latch_loop_line_horz.get_end(), sr_latch_loop_line_horz.get_end() + [0, -0.75, 0])

        sr_latch_reset_line_input = Line(sr_latch_not_gate.input_line.get_end() + [-2, 0, 0], sr_latch_not_gate.input_line.get_end() + [0, 0, 0])
        sr_latch_not_and_horz = Line(sr_latch_not_gate.output_line.get_end() + [0, 0, 0], sr_latch_not_gate.output_line.get_end() + [2.15, 0, 0])
        sr_latch_reset_line_vert = Line(sr_latch_not_and_horz.get_end(), sr_latch_not_and_horz.get_end() + [0, 0.75, 0])

        sr_latch_output_line = Line(sr_latch_and_gate.output_line.get_end() + [0, 0, 0], sr_latch_and_gate.output_line.get_end() + [2.5, 0, 0])

        SrLatchSetText = Text("set", font_size=18).shift(sr_latch_set_line_input.get_start() + [0.2, .2, 0])
        SrLatchResetText = Text("reset", font_size=18).shift(sr_latch_reset_line_input.get_start() + [0.2, .2, 0])
        SrLatchOutputText = Text("output", font_size=18).shift(sr_latch_output_line.get_end() + [-0.3, .2, 0])

        SrTitleText = Text("SR Latch", font_size=72).shift([0,3,0])

        SrLatchVGroup.add(sr_latch_and_gate, 
                            sr_latch_or_gate, 
                            sr_latch_not_gate, 
                            sr_latch_set_line_input, 
                            sr_latch_or_and_horz,
                            sr_latch_or_and_vert,
                            sr_latch_loop_line_vert,
                            sr_latch_loop_line_horz,
                            sr_latch_loop_line,
                            sr_latch_reset_line_input,
                            SrLatchResetText,
                            SrLatchSetText,
                            sr_latch_not_and_horz,
                            sr_latch_reset_line_vert,
                            sr_latch_output_line,
                            SrLatchOutputText,
                            )

        self.play(Create(SrLatchVGroup), Create(SrTitleText))

        self.wait(1)

        ###############################################################################
        DLTitleText = Text("Data Latch", font_size=72).shift([0,3,0])

        self.play(FadeOut(SrLatchOutputText), FadeOut(SrLatchResetText), FadeOut(SrLatchSetText), SrLatchVGroup.animate.scale(.5).shift([1, 0, 0]), ReplacementTransform(SrTitleText, DLTitleText))

        d_latch_and_top = AndGateSymbol(scale_factor=0.5, shift_offset=[-3, 1, 0])
        d_latch_and_bottom = AndGateSymbol(scale_factor=0.5, shift_offset=[-3, -1, 0])

        d_latch_top_and_out_vert = Line(d_latch_and_top.output_line.get_end() + [0, 0, 0], d_latch_and_top.output_line.get_end() + [0, -0.44, 0])
        d_latch_top_and_out_horz = Line(d_latch_top_and_out_vert.get_end(), d_latch_top_and_out_vert.get_end() + [1.5, 0, 0])

        d_latch_bottom_and_out_vert = Line(d_latch_and_bottom.output_line.get_end() + [0, 0, 0], d_latch_and_bottom.output_line.get_end() + [0, 0.69, 0])
        d_latch_bottom_and_out_horz = Line(d_latch_bottom_and_out_vert.get_end(), d_latch_bottom_and_out_vert.get_end() + [1.5, 0, 0])

        d_latch_mux_not_gate = NotGateSymbol(shift_offset= d_latch_and_bottom.input_line_top.get_start() + [-1, 0, 0], scale_factor=0.5)
        d_latch_data_and_connector_vert = Line(d_latch_mux_not_gate.input_line.get_start() + [0, 0, 0], d_latch_mux_not_gate.input_line.get_start() + [0, 1.5, 0])
        d_latch_data_and_connector_horz = Line(d_latch_data_and_connector_vert.get_end() + [-1.5, 0, 0], d_latch_data_and_connector_vert.get_end() + [1.5, 0, 0])

        d_latch_mux_connector = Line(d_latch_and_top.input_line_top.get_start(), d_latch_and_bottom.input_line_bottom.get_start())
        d_latch_mux_output = Line(d_latch_and_bottom.input_line_bottom.get_start() + [0, 0, 0], d_latch_and_bottom.input_line_bottom.get_start() + [-2.75, 0, 0])


        self.play(  FadeIn(d_latch_and_top),
                    FadeIn(d_latch_and_bottom),
                    FadeIn(d_latch_top_and_out_vert),
                    FadeIn(d_latch_top_and_out_horz),
                    FadeIn(d_latch_bottom_and_out_vert),
                    FadeIn(d_latch_bottom_and_out_horz),
                    FadeIn(d_latch_mux_not_gate),
                    FadeIn(d_latch_data_and_connector_vert),
                    FadeIn(d_latch_data_and_connector_horz),
                    FadeIn(d_latch_mux_connector),
                    FadeIn(d_latch_mux_output),
                    )