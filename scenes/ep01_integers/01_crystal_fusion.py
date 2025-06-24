# Manim Community v0.18.0
# 场景1：晶石融合 (指数乘法)

from manim import *

class CrystalFusion(Scene):
    def construct(self):
        # --- 开场旁白 ---
        # Elara: 凯，仔细观察，当你把它们的能量融合在一起时，它们的指数发生了什么变化？
        
        # 1. 创建初始晶石和它们的标签
        # 创建代表 2^3 的晶石 (一个蓝色的圆形)
        crystal1_obj = Circle(radius=0.5, color=BLUE, fill_opacity=0.5).set_stroke(color=BLUE_A, width=10)
        crystal1_label = MathTex("2^3").next_to(crystal1_obj, DOWN)
        crystal1 = VGroup(crystal1_obj, crystal1_label).shift(LEFT * 3)

        # 创建代表 2^2 的晶石
        crystal2_obj = Circle(radius=0.4, color=BLUE, fill_opacity=0.5).set_stroke(color=BLUE_A, width=10)
        crystal2_label = MathTex("2^2").next_to(crystal2_obj, DOWN)
        crystal2 = VGroup(crystal2_obj, crystal2_label).shift(RIGHT * 3)

        self.play(FadeIn(crystal1, scale=0.5), FadeIn(crystal2, scale=0.5))
        self.wait(1)

        # 2. 动画：晶石靠近与融合
        # 创建融合后的目标晶石
        fusion_crystal_obj = Circle(radius=0.7, color=PURPLE, fill_opacity=0.7).set_stroke(color=PURPLE_A, width=15)
        fusion_crystal = VGroup(fusion_crystal_obj).move_to(ORIGIN)

        # 播放融合动画，同时淡出旧标签
        self.play(
            ReplacementTransform(crystal1_obj, fusion_crystal_obj.copy()),
            ReplacementTransform(crystal2_obj, fusion_crystal_obj.copy()),
            FadeOut(crystal1_label),
            FadeOut(crystal2_label)
        )
        self.remove(crystal1_obj, crystal2_obj)
        self.add(fusion_crystal_obj)
        self.play(Indicate(fusion_crystal_obj, color=YELLOW))
        self.wait(1)

        # 3. 动画：指数的飞出与相加
        # 从原始位置创建指数
        exponent3 = MathTex("3").move_to(crystal1.get_center() + UP * 0.7)
        exponent2 = MathTex("2").move_to(crystal2.get_center() + UP * 0.7)
        
        plus_sign = MathTex("+").move_to(UP * 1.5)
        
        # 指数飞出并准备相加
        self.play(
            exponent3.animate.move_to(UP * 1.5 + LEFT * 0.5),
            exponent2.animate.move_to(UP * 1.5 + RIGHT * 0.5)
        )
        self.play(Write(plus_sign))
        
        # 指数合并计算
        sum_group = VGroup(exponent3, plus_sign, exponent2)
        target_exponent = MathTex("5").move_to(UP * 1.5)
        
        self.play(Transform(sum_group, target_exponent))
        self.wait(1)

        # 4. 动画：新指数落下，形成最终晶石
        final_label = MathTex("2^5")
        final_label.next_to(fusion_crystal_obj, DOWN)

        # 将计算结果的'5'移动到最终标签中'5'的位置
        self.play(sum_group.animate.move_to(final_label.get_part_by_tex("5").get_center()))
        # 同时写出底数'2'和指数的'^'符号部分
        self.play(Write(final_label.get_part_by_tex("2^")))
        
        final_crystal_group = VGroup(fusion_crystal_obj, final_label)
        self.wait(1)
        
        # 5. 屏幕中央出现法则
        law = MathTex("a^m \\cdot a^n = a^{m+n}", font_size=60).to_edge(UP)
        self.play(ReplacementTransform(final_crystal_group, law))
        self.wait(2)
        self.play(FadeOut(law))

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

