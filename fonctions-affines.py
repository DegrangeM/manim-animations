from manim import *

def niceFloat(n) :
    return str(round(n)) if round(n) == round(n, 1) else str(round(n,1))

class fonctions_affines(Scene):
    def construct(self):
        ax = Axes(
            x_range=[-6, 6, 1],
            y_range=[-6, 6, 1],
            x_length=7,
            y_length=7,
            tips=True,
            axis_config={"include_numbers": True},
        ).shift(LEFT*3)
        plane = NumberPlane(
            x_range=[-6, 6, 1],
            y_range=[-6, 6, 1],
            x_length=7,
            y_length=7,
            background_line_style={
                "stroke_color": WHITE,
                "stroke_opacity": 0.25
            },
            faded_line_style = {
                "stroke_color": RED,
            }
        ).shift(LEFT*3)
        plot = ax.plot(lambda x: 2*x-3, color=RED)
        plane.get_x_axis().set_opacity(0)
        plane.get_y_axis().set_opacity(0)
        self.play(FadeIn(plane), FadeIn(ax))
        self.play(Create(plot))
        self.wait()
        dot = Dot(ax.coords_to_point(0, -3))
        pText = MathTex("p = ", "-3")
        pTitre = Text("Ordonnée à l'origine").scale(0.5).next_to(pText, UP)
        pGroup = VGroup(pTitre, pText).move_to(RIGHT * 4)
        self.play(Write(pTitre))
        self.play(Create(dot))
        self.play(FocusOn(dot))
        self.play(Write(pText))
        self.wait()
        p = ValueTracker(-3)
        dot.add_updater(lambda d: d.move_to(ax.coords_to_point(0, p.get_value())))
        plot.add_updater(lambda plot: plot.become(ax.plot(lambda x: 2*x+p.get_value(), color=RED)))
        self.play(p.animate.set_value(2), Transform(pText[1], MathTex("2").move_to(pText[1])))
        self.wait()
        self.play(p.animate.set_value(-5), Transform(pText[1], MathTex("-5").move_to(pText[1])))
        self.wait()
        self.play(p.animate.set_value(-3), Transform(pText[1], MathTex("-3").move_to(pText[1])))
        self.wait()
        self.play(FadeOut(dot))
        plot.clear_updaters()
        self.play(pGroup.animate.shift(DOWN*2.5))
        self.wait()
        mText = MathTex("m = ", "2")
        mTitre = Text("Coefficient directeur").scale(0.5).next_to(mText, UP)
        mGroup = VGroup(mTitre, mText).move_to(RIGHT * 4)
        v1 = Arrow(
            ax.coords_to_point(0, -3),
            ax.coords_to_point(1, -3),
            color=GREEN,
            buff=0.1,
            max_stroke_width_to_length_ratio=50,
            max_tip_length_to_length_ratio=0.5
        )
        v2 = Arrow(
            ax.coords_to_point(1, -3),
            ax.coords_to_point(1, 2-3),
            color=GREEN,
            buff=0.1,
            max_stroke_width_to_length_ratio=50,
        )
        b1 = Brace(v2, direction = RIGHT)
        b1text = b1.get_text("2")
        self.play(Write(mTitre))
        self.play(GrowArrow(v1))
        self.play(GrowArrow(v2))
        self.play(FadeIn(b1), FadeIn(b1text))
        self.play(Indicate(b1), Indicate(b1text))
        self.play(Write(mText))
        self.wait()
        m = ValueTracker(2)
        v2.add_updater(lambda v: v.become(Arrow(
            ax.coords_to_point(1, -3),
            ax.coords_to_point(1, m.get_value()-3),
            color=GREEN,
            buff=0.1,
            max_stroke_width_to_length_ratio=50,
        )))
        b1.add_updater(lambda b: b.become(Brace(v2, direction = RIGHT)))
        b1text.add_updater(lambda t: t.become(
            b1.get_text(niceFloat(m.get_value()))
        ))
        plot.add_updater(lambda plot: plot.become(ax.plot(lambda x: m.get_value()*x-3, color=RED)))
        # Ne pas retirer le run_time sinon cela provoque un bug (affichage de 4.0 au lieu de 4)
        self.play(m.animate.set_value(4), Transform(mText[1], MathTex("4").move_to(mText[1])), run_time=1)
        self.wait()
        self.play(m.animate.set_value(7), Transform(mText[1], MathTex("7").move_to(mText[1])), run_time=1)
        self.wait()
        self.play(m.animate.set_value(-2), Transform(mText[1], MathTex("-2").move_to(mText[1]).shift(RIGHT*0.1)), run_time=1)
        self.wait()
        self.play(m.animate.set_value(2), Transform(mText[1], MathTex("2").move_to(mText[1])), run_time=1)
        self.wait()
        b1.clear_updaters()
        b1text.clear_updaters()
        plot.clear_updaters()
        v2.clear_updaters()
        mGroup2 = VGroup(v1, v2, b1, b1text)
        self.play(mGroup2.animate.shift(ax.coords_to_point(1, 2)-ax.coords_to_point(0,0)))
        self.play(mGroup2.animate.shift(ax.coords_to_point(1, 2)-ax.coords_to_point(0,0)))
        self.play(mGroup2.animate.shift(ax.coords_to_point(1, 2)-ax.coords_to_point(0,0)))
        self.play(FadeOut(mGroup2))
        self.play(mGroup.animate.shift(UP*2.5))
        formula = MathTex("f(x) = mx + p").shift(RIGHT*4)
        self.play(Write(formula))
        self.wait()
        self.play(Transform(formula, MathTex("f(x) = 2x - 3").move_to(formula)))
        self.wait()
        self.play(ApplyWave(formula))
        self.play(FadeOut(pGroup), FadeOut(mGroup))
        plot.add_updater(lambda plot: plot.become(ax.plot(lambda x: m.get_value()*x+p.get_value(), color=RED)))
        self.play(
            m.animate.set_value(2),
            p.animate.set_value(1),
            Transform(formula, MathTex("f(x) = 2x + 1").move_to(formula)),
            run_time = 2
        )
        self.wait()
        self.play(ApplyWave(formula))
        self.wait()
        self.play(
            m.animate.set_value(3),
            p.animate.set_value(1),
            Transform(formula, MathTex("f(x) = 3x + 1").move_to(formula)),
            run_time = 2
        )
        self.wait()
        self.play(ApplyWave(formula))
        self.wait()
        self.play(
            m.animate.set_value(-4),
            p.animate.set_value(1),
            Transform(formula, MathTex("f(x) = -4x + 1").move_to(formula)),
            run_time = 2
        )
        self.wait()
        self.play(ApplyWave(formula))
        self.wait()
        self.play(
            m.animate.set_value(-4),
            p.animate.set_value(5),
            Transform(formula, MathTex("f(x) = -4x + 5").move_to(formula)),
            run_time = 2
        )
        self.wait()
        self.play(ApplyWave(formula))
        self.wait()