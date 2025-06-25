# Manim Community v0.19.0
# 文件名: 01_opening_scene.py
# 场景: 【开场：谜题的提出】 (时长约45秒)

from manim import *

# --- 全局设定 ---
# 为了模拟角色对话，我们创建一个辅助函数
# 这个函数可以在后续所有场景脚本中复用
def create_dialogue(character_name, text, character_color, scene, wait_time=3):
    # 角色名字
    name = Text(character_name, font_size=28, color=character_color, weight=BOLD)
    # 对话内容
    dialogue_text = Text(text, font_size=32, weight=NORMAL)
    
    # 将名字和对话组合，并创建对话框背景
    content = VGroup(name, dialogue_text).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
    dialogue_box = SurroundingRectangle(content, corner_radius=0.2, buff=0.4, fill_opacity=0.9, fill_color="#0c1445", stroke_color=character_color, stroke_width=2)
    
    # 完整的对话组合
    dialogue_group = VGroup(dialogue_box, content).to_corner(UL, buff=0.5)
    
    scene.play(Write(dialogue_group))
    scene.wait(wait_time) # 根据旁白长度调整等待时间
    scene.play(FadeOut(dialogue_group))

class OpeningScene(Scene):
    def construct(self):
        # 设定场景的深空背景色
        self.camera.background_color = "#0c1445"
        
        # --- 视觉: 星空背景和古老星图 (00:00 - 00:15) ---
        
        # 1. 创建一个缓慢移动的星空背景，增加纵深感
        stars = VGroup(*[Dot(radius=0.03, color=WHITE).move_to(np.random.uniform(-9, 9, 3)) for _ in range(200)])
        self.play(Create(stars), run_time=3)
        self.play(stars.animate.shift(LEFT*0.5), run_time=10) # 让星空缓慢移动

        # 2. 渐入古老的星图 (使用我们之前下载好的本地图片)
        star_map = ImageMobject("assets/ep01/star_map_background.png")
        star_map.set_opacity(0.4)
        self.play(FadeIn(star_map, scale=1.2))

        # 3. 动画：星图上的神秘符号发光
        symbol1 = MathTex("2^5", color=YELLOW_C).scale(1.8).move_to(LEFT*2.5 + UP*1.5)
        symbol2 = MathTex("3^4", color=YELLOW_C).scale(1.8).move_to(RIGHT*2.5 + DOWN*1.5)
        self.play(FadeIn(symbol1), FadeIn(symbol2))
        self.play(Flash(symbol1, color=WHITE, flash_radius=1, line_length=0.5), 
                  Flash(symbol2, color=WHITE, flash_radius=1, line_length=0.5), 
                  run_time=3)
        
        # --- 对白与叙事 (00:16 - 00:45) ---
        
        create_dialogue(
            character_name="Kai (凯)", 
            text="大师，这张古老的星图真的沉睡了千年吗？\n我们...真的能唤醒它，找到那个传说中的失落星系？", 
            character_color=ORANGE, 
            scene=self,
            wait_time=5
        )
        
        create_dialogue(
            character_name="Elara (大师)", 
            text="它一直在等待，凯。等待能读懂它语言的人。\n这语言，就是数学...", 
            character_color=BLUE_B, 
            scene=self,
            wait_time=5
        )

        # 最终聚焦，为下一场景做铺垫
        self.play(
            self.camera.frame.animate.scale(0.5).move_to(symbol1),
            FadeOut(symbol2)
        )
        self.wait(2)

