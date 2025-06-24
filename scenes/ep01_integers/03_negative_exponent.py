
# Manim Community v0.18.0
# 场景3：反能量之谜 (负指数)

from manim import *

class NegativeExponentMystery(Scene):
    def construct(self):
        # --- 场景设置与旁白引入 ---
        # Kai: 负数的能量等级？这难道是“反能量”吗？
        # Elara: 当一种能量和它的反能量相遇时，它们会相互中和...

        title = Text("反能量之谜：a⁻ⁿ = ?").to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # 1. 创建普通晶石和反能量晶石
        crystal_pos_label = MathTex("3^2")
        crystal_pos = SurroundingRectangle(crystal_pos_label, color=BLUE, buff=0.4, corner_radius=0.1)
        crystal_pos_group = VGroup(crystal_pos, crystal_pos_label).shift(LEFT * 3)
        
        crystal_neg_label = MathTex("3^{-2}")
        crystal_neg = SurroundingRectangle(crystal_neg_label, color=RED, buff=0.4, corner_radius=0.1)
        crystal_neg_group = VGroup(crystal_neg, crystal_neg_label).shift(RIGHT * 3)

        self.play(FadeIn(crystal_pos_group), FadeIn(crystal_neg_group))

        # 显示乘法符号
        multiply_sign = Tex(r"$\times$").scale(1.5)
        self.play(Write(multiply_sign))
        self.wait(1)

        # 2. 动画：能量融合，指数相加
        # Elara: 你看，$3^2$ 乘以 $3^{-2}$，根据我们的融合法则...
        
        # 将所有元素组合成一个等式
        full_equation = VGroup(crystal_pos_group, multiply_sign, crystal_neg_group).arrange(RIGHT, buff=0.5)
        self.play(full_equation.animate.move_to(ORIGIN))

        # 指数飞出并相加
        exponent_part = MathTex("3^{2+(-2)}").scale(1.2).shift(DOWN*2)
        self.play(Transform(full_equation.copy(), exponent_part))
        self.wait(1)
        
        # 指数变为0
        exponent_zero = MathTex("3^0").scale(1.2).move_to(exponent_part.get_center())
        self.play(Transform(exponent_part, exponent_zero))
        self.wait(1)

        # 结果变为1
        result_1_group = MathTex("= 1").scale(1.5).next_to(exponent_zero, RIGHT)
        self.play(ReplacementTransform(exponent_zero, result_1_group))
        
        self.wait(2)
        
        # 3. Aha! 时刻: 推导负指数的意义
        # Elara: 既然 $3^2$ 乘以 $3^{-2}$ 等于1，你能推断出，$3^{-2}$ 它本身，究竟代表着什么吗？
        
        self.play(FadeOut(title))
        self.play(full_equation.animate.to_edge(UP, buff=1.5), FadeOut(result_1_group))
        
        # 重新展示等式用于推导
        derivation_start = MathTex("3^2", r"\cdot", "3^{-2}", "=", "1").move_to(ORIGIN)
        self.play(ReplacementTransform(full_equation.copy(), derivation_start))
        self.wait(1)
        
        # 动画化代数变形过程
        # 创建目标公式
        target_form = MathTex("3^{-2}", "=", r"\frac{1}{3^2}").move_to(ORIGIN)
        
        # 使用TransformMatchingTex可以平滑地匹配和变换公式中的相同部分
        # 它会智能地将 derivation_start 中的对应部分移动到 target_form 的位置
        self.play(
            TransformMatchingTex(
                derivation_start.copy(), 
                target_form,
                transform_mismatches=True,
                key_map={"3^2": "3^2"}
            )
        )
        
        self.wait(2)

        # 4. 最终法则展示
        final_law = MathTex("a^{-n} = \\frac{1}{a^n}", font_size=96).move_to(DOWN*2)
        # 将屏幕上所有元素都变换成最终的法则，有强调效果
        self.play(ReplacementTransform(VGroup(derivation_start, target_form), final_law))
        self.wait(3)
        self.play(FadeOut(final_law))