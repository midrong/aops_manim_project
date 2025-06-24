# Manim Community v0.19.0
# 《解题的艺术》第一集：《指数的诞生》
# 完整动画脚本 V1.1 (修正版)

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

# 【注意】我们的主场景类名是 BirthOfExponents
class BirthOfExponents(Scene):
    def construct(self):
        # 使用深蓝色作为背景，模拟天文台的神秘氛围
        self.camera.background_color = "#0c1445"
        
        # --- 【开场：谜题的提出】 ---
        
        # 1. 视觉：星空背景和古老星图
        stars = VGroup(*[Dot(radius=0.02, color=WHITE).move_to(np.random.uniform(-8, 8, 3)) for _ in range(150)])
        self.add(stars)
        
        # 【代码修正】从本地的assets文件夹加载我们下载好的图片
        star_map = ImageMobject("assets/ep01/star_map_background.png") 
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


        # --- 【第一部分：指数的诞生 - 为重复而生】 ---

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

        self.play(FadeOut(VGroup(exponent_form, base_label, exponent_label)))

        # （后续场景代码省略，但应包含所有部分）
