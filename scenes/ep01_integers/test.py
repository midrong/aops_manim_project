# Manim Community v0.19.0
# 《解题的艺术》第一集：《指数的诞生》
# 完整动画脚本 V1.0

from manim import *

# --- 全局设定 ---
# 为了模拟角色对话，我们创建一个辅助函数
def create_dialogue(character_name, text, character_color, scene):
    # 角色名字
    name = Text(character_name, font_size=24, color=character_color).to_corner(UL).shift(RIGHT*0.5)
    # 对话框
    dialogue_box = SurroundingRectangle(Text(text, font_size=28), corner_radius=0.1, buff=0.3, fill_opacity=0.8, fill_color=BLACK)
    # 完整的对话组合
    dialogue = VGroup(name, dialogue_box).to_corner(UL)
    
    scene.play(Write(dialogue))
    scene.wait(3) # 根据旁白长度调整等待时间
    scene.play(FadeOut(dialogue))

class BirthOfExponents(Scene):
    def construct(self):
        # 使用深蓝色作为背景，模拟天文台的神秘氛围
        self.camera.background_color = "#0c1445"
        
        # --- 【开场：谜题的提出】 (约 00:00 - 00:45) ---
        
        # 1. 视觉：星空背景和古老星图
        # 用很多小点来模拟星空
        stars = VGroup(*[Dot(radius=0.02, color=WHITE).move_to(np.random.uniform(-8, 8, 3)) for _ in range(150)])
        self.add(stars)
        
        # 一个示意性的星图
        star_map = ImageMobject("https://placehold.co/800x600/000033/FFFFFF?text=Ancient+Star+Map") # 使用占位图
        star_map.set_opacity(0.3)
        self.play(FadeIn(star_map))

        # 闪烁的数学符号
        symbol1 = MathTex("2^5", color=YELLOW).scale(1.5).move_to(LEFT*2 + UP*1)
        symbol2 = MathTex("3^4", color=YELLOW).scale(1.5).move_to(RIGHT*2 + DOWN*1)
        self.play(FadeIn(symbol1), FadeIn(symbol2))
        self.play(Flash(symbol1), Flash(symbol2), run_time=2)
        
        # 2. 旁白与对话
        create_dialogue("Kai (凯)", "大师，这张古老的星图真的沉睡了千年吗？", ORANGE, self)
        create_dialogue("Elara (大师)", "它一直在等待，凯。等待能读懂它语言的人...", BLUE, self)
        self.wait(2)

        # 清理开场
        self.play(FadeOut(stars), FadeOut(star_map), FadeOut(symbol1), FadeOut(symbol2))


        # --- 【第一部分：指数的诞生 - 为重复而生】 (约 00:46 - 01:50) ---

        # 1. 从加法到乘法
        create_dialogue("Elara (大师)", "凯，所有复杂的知识，都源于最简单的思想...", BLUE, self)
        
        addition = MathTex("2+2+2+2+2").scale(1.5)
        multiplication = MathTex("5 \\times 2").scale(1.5)
        self.play(Write(addition))
        self.wait(1)
        self.play(ReplacementTransform(addition, multiplication))
        self.wait(1)
        
        create_dialogue("Kai (凯)", "是乘法！用一个简单的符号，代表重复的加法。", ORANGE, self)
        self.play(FadeOut(multiplication))

        # 2. 从乘法到指数
        multiplication_long = MathTex("2\\times2\\times2\\times2\\times2").scale(1.5)
        exponent_form = MathTex("2^5").scale(2)
        
        self.play(Write(multiplication_long))
        self.wait(1)
        self.play(ReplacementTransform(multiplication_long, exponent_form))

        # 标注底数和指数
        base = exponent_form.get_part_by_tex("2")
        exponent = exponent_form.get_part_by_tex("5")
        base_label = Text("底数", font_size=24).next_to(base, DOWN, buff=0.5)
        exponent_label = Text("指数", font_size=24).next_to(exponent, UP, buff=0.5)
        self.play(Indicate(base, color=BLUE), Write(base_label))
        self.play(Indicate(exponent, color=YELLOW), Write(exponent_label))
        self.wait(2)

        self.play(FadeOut(exponent_form), FadeOut(base_label), FadeOut(exponent_label))

        # --- 【第二部分：乘除法则】 (约 01:51 - 03:30) ---
        
        # 乘法法则 (融合)
        eq_mul = MathTex("2^3", "\\cdot", "2^2", "=", "2^{3+2}", "=", "2^5").scale(1.2)
        self.play(Write(eq_mul[0:3]))
        self.wait(1)
        self.play(Transform(eq_mul[0:3].copy(), eq_mul[4]))
        self.play(Write(eq_mul[3]))
        self.wait(1)
        self.play(Transform(eq_mul[4], eq_mul[6]))
        self.play(Write(eq_mul[5]))
        self.wait(2)
        
        law_mul = MathTex("a^m \\cdot a^n = a^{m+n}").to_edge(UP)
        self.play(ReplacementTransform(VGroup(eq_mul), law_mul))
        self.wait(2)
        self.play(FadeOut(law_mul))

        # 除法法则 (分离)
        create_dialogue("Elara (大师)", "那如果是分离能量呢？", BLUE, self)
        eq_div = MathTex(r"\frac{2^5}{2^2}", "=", "2^{5-2}", "=", "2^3").scale(1.2)
        self.play(Write(eq_div[0]))
        self.wait(1)
        self.play(Transform(eq_div[0].copy(), eq_div[2]))
        self.play(Write(eq_div[1]))
        self.wait(1)
        self.play(Transform(eq_div[2], eq_div[4]))
        self.play(Write(eq_div[3]))
        self.wait(2)
        
        law_div = MathTex(r"\frac{a^m}{a^n} = a^{m-n}").to_edge(UP)
        self.play(ReplacementTransform(VGroup(eq_div), law_div))
        self.wait(2)
        self.play(FadeOut(law_div))
        
        # 后续场景的代码可以继续添加在这里...
        # 例如 ZeroExponentMystery, NegativeExponentMystery 等
        # 为了简洁，此处省略，但最终脚本应将所有场景类合并或按顺序调用

