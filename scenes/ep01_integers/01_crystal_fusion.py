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


