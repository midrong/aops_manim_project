
# Manim Community v0.18.0
# 场景2：零指数之谜 (双屏对比)

from manim import *

class ZeroExponentMystery(Scene):
    def construct(self):
        # --- 场景设置与旁白引入 ---
        # Kai: （困惑地）大师，这个...能量等级为`0`？这是什么意思？
        # Elara: ...让我们用逻辑来找到答案...

        # 创建标题
        title = Text("零指数之谜：a⁰ = ?").to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # 创建分割线，实现双屏效果
        line = DashedLine(UP * 3, DOWN * 3.5, color=GRAY)
        self.play(Create(line))

        # --- 左屏: 实体逻辑 (一个数除以它自己) ---
        left_title = Text("实体世界").to_edge(UP, buff=1.5).shift(LEFT * 3.5)
        self.play(Write(left_title))

        # 创建分数并展开
        fraction = MathTex(r"\frac{2^3}{2^3}", r"=", r"\frac{2 \times 2 \times 2}{2 \times 2 \times 2}").shift(LEFT * 3.5)
        self.play(Write(fraction[0]))
        self.wait(0.5)
        # 用ReplacementTransform让展开更自然
        self.play(ReplacementTransform(fraction[0].copy(), fraction[2]))
        self.play(Write(fraction[1]))
        self.wait(1)
        
        # 动画化约分过程
        numerator_parts = fraction[2].get_parts_by_tex("2")
        denominator_parts = fraction[2].get_parts_by_tex("2", submobject_mode="bottom_up")
        
        cancel_lines = VGroup()
        for i in range(3):
            # 获取分子和分母的'2'
            num_2 = numerator_parts[i]
            den_2 = denominator_parts[i]
            
            # 画线抵消
            cancel_line = Line(num_2.get_center()+UL*0.1, den_2.get_center()+DR*0.1, color=YELLOW, stroke_width=4)
            cancel_lines.add(cancel_line)
            self.play(Create(cancel_line), run_time=0.3)
            self.play(Indicate(num_2, color=BLUE), Indicate(den_2, color=RED), run_time=0.3)


        # 变换为1
        result_1 = MathTex("= 1", font_size=72).next_to(fraction[1], RIGHT)
        self.play(ReplacementTransform(VGroup(fraction, cancel_lines), result_1))
        self.wait(1)


        # --- 右屏: 法则逻辑 (指数相减) ---
        right_title = Text("符号世界").to_edge(UP, buff=1.5).shift(RIGHT * 3.5)
        self.play(Write(right_title))
        
        expression = MathTex(r"\frac{2^3}{2^3}", r"=", r"2^{3-3}").shift(RIGHT * 3.5)
        self.play(Write(expression[0]))
        self.wait(0.5)
        self.play(ReplacementTransform(expression[0].copy(), expression[2]))
        self.play(Write(expression[1]))
        self.wait(1)

        # 指数相减动画
        result_0 = MathTex("= 2^0", font_size=72).next_to(expression[1], RIGHT)
        self.play(ReplacementTransform(expression, result_0))
        self.wait(1)

        # --- Aha! 时刻: 连接左右两边 ---
        # Elara: 你看，凯。从两个完全不同的角度出发...
        
        # 绘制连接光束
        connection_arrow = DoubleArrow(result_1.get_right(), result_0.get_left(), buff=0.2, color=ORANGE)
        self.play(GrowArrow(connection_arrow))

        final_law = MathTex("a^0 = 1", r"~~(a \neq 0)", font_size=96)
        final_law.move_to(DOWN*2)
        
        # 最终结论
        self.play(
            ReplacementTransform(VGroup(result_1, result_0, connection_arrow), final_law[0]),
            FadeOut(title, left_title, right_title, line)
        )
        self.play(Write(final_law[1]))
        self.wait(3)
        self.play(FadeOut(final_law))

