# ========================================
# 《解题的艺术》动画系列 - The Art of Problem Solving Animation Series
# 第一集：指数的诞生 - Episode 01: The Birth of Exponents  
# 场景01：开场谜题的提出 - Scene 01: Opening Mystery
# 版本：V1.4 (无外部资源依赖版)
# ========================================

from manim import *
import numpy as np
from typing import List, Tuple

# --- 全局配置 ---
BACKGROUND_COLOR = "#0c1445"
DIALOGUE_CONFIG = {
    "font_size_name": 28,
    "font_size_text": 32,
    "box_corner_radius": 0.2,
    "box_buff": 0.4,
    "box_opacity": 0.9,
    "position_buff": 0.5
}

STAR_CONFIG = {
    "count": 120,
    "twinkle_count": 15,
    "radius_range": (0.01, 0.04),
    "area_range": (-8, 8)
}

# --- 工具函数 ---
def create_dialogue(character_name: str, text: str, character_color: str, scene: Scene) -> None:
    """创建角色对话动画"""
    base_time = 2.5
    text_length_factor = len(text.replace("\n", "")) * 0.12
    wait_time = max(base_time, text_length_factor)
    
    # 尝试使用中文字体，回退到默认字体
    fonts_to_try = ["Noto Sans CJK SC", "SimHei", "PingFang SC", "Microsoft YaHei"]
    name_text = None
    dialogue_text = None
    
    for font in fonts_to_try:
        try:
            name_text = Text(character_name, font_size=DIALOGUE_CONFIG["font_size_name"], 
                           color=character_color, weight=BOLD, font=font)
            dialogue_text = Text(text, font_size=DIALOGUE_CONFIG["font_size_text"], 
                               weight=NORMAL, font=font)
            break
        except Exception:
            continue
    
    if name_text is None:
        name_text = Text(character_name, font_size=DIALOGUE_CONFIG["font_size_name"], 
                        color=character_color, weight=BOLD)
        dialogue_text = Text(text, font_size=DIALOGUE_CONFIG["font_size_text"], weight=NORMAL)
    
    content = VGroup(name_text, dialogue_text).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
    dialogue_box = SurroundingRectangle(
        content, corner_radius=DIALOGUE_CONFIG["box_corner_radius"],
        buff=DIALOGUE_CONFIG["box_buff"], fill_opacity=DIALOGUE_CONFIG["box_opacity"],
        fill_color=BACKGROUND_COLOR, stroke_color=character_color, stroke_width=2
    )
    dialogue_group = VGroup(dialogue_box, content).to_corner(UL, buff=DIALOGUE_CONFIG["position_buff"])
    
    # {Audio Cue: character_name dialogue start}
    scene.play(Write(dialogue_group), run_time=1.5)
    scene.wait(wait_time)
    scene.play(FadeOut(dialogue_group), run_time=1.0)
    # {Audio Cue: character_name dialogue end}

def create_starfield(scene: Scene) -> VGroup:
    """创建星空背景"""
    positions = [
        np.array([
            np.random.uniform(-STAR_CONFIG["area_range"][0], STAR_CONFIG["area_range"][1]),
            np.random.uniform(-STAR_CONFIG["area_range"][0], STAR_CONFIG["area_range"][1]),
            0
        ]) for _ in range(STAR_CONFIG["count"])
    ]
    
    stars = VGroup(*[
        Dot(pos, radius=np.random.uniform(*STAR_CONFIG["radius_range"]), 
            color=WHITE, fill_opacity=np.random.uniform(0.3, 1.0))
        for pos in positions
    ])
    
    return stars

def create_procedural_star_map(scene: Scene) -> VGroup:
    """
    创建程序生成的星图，替代外部图片资源
    """
    star_map_group = VGroup()
    
    # 1. 创建主要的星座连线
    constellation_lines = VGroup()
    
    # 大熊座样式
    ursa_major_points = [
        LEFT*3 + UP*2, LEFT*1.5 + UP*2.2, LEFT*0.5 + UP*1.8, 
        RIGHT*0.5 + UP*2.5, RIGHT*1.8 + UP*2, RIGHT*3 + UP*1.5, RIGHT*2.5 + UP*0.8
    ]
    for i in range(len(ursa_major_points) - 1):
        line = Line(ursa_major_points[i], ursa_major_points[i+1], 
                   color=BLUE_C, stroke_width=2, stroke_opacity=0.6)
        constellation_lines.add(line)
    
    # 猎户座样式
    orion_points = [
        LEFT*2 + DOWN*1, LEFT*1 + DOWN*0.5, RIGHT*0 + DOWN*0.8,
        RIGHT*1 + DOWN*1.2, LEFT*0.5 + DOWN*2, RIGHT*0.5 + DOWN*2.5
    ]
    for i in range(len(orion_points) - 1):
        line = Line(orion_points[i], orion_points[i+1], 
                   color=PURPLE_C, stroke_width=2, stroke_opacity=0.5)
        constellation_lines.add(line)
    
    # 2. 在连线的端点和交叉点创建亮星
    bright_stars = VGroup()
    all_points = ursa_major_points + orion_points
    for point in all_points:
        star = Dot(point, radius=0.08, color=YELLOW, fill_opacity=0.9)
        bright_stars.add(star)
    
    # 3. 创建神秘的几何图案
    mystical_shapes = VGroup()
    
    # 中心的神秘圆环
    center_circle = Circle(radius=1.5, color=TEAL_C, stroke_width=3, stroke_opacity=0.4)
    inner_circle = Circle(radius=0.8, color=TEAL_C, stroke_width=2, stroke_opacity=0.6)
    
    # 十字准线
    cross_h = Line(LEFT*1.2, RIGHT*1.2, color=TEAL_C, stroke_width=2, stroke_opacity=0.5)
    cross_v = Line(DOWN*1.2, UP*1.2, color=TEAL_C, stroke_width=2, stroke_opacity=0.5)
    
    mystical_shapes.add(center_circle, inner_circle, cross_h, cross_v)
    
    # 4. 添加装饰性的符文符号
    runic_symbols = VGroup()
    rune_positions = [LEFT*4 + UP*3, RIGHT*4 + UP*3, LEFT*4 + DOWN*2.5, RIGHT*4 + DOWN*2.5]
    rune_texts = ["✦", "✧", "✩", "✪"]
    
    for pos, rune in zip(rune_positions, rune_texts):
        symbol = Text(rune, font_size=36, color=GOLD_C, fill_opacity=0.7).move_to(pos)
        runic_symbols.add(symbol)
    
    # 5. 组装完整的星图
    star_map_group.add(constellation_lines, bright_stars, mystical_shapes, runic_symbols)
    star_map_group.set_opacity(0.4)  # 设置整体透明度，模拟古老的感觉
    
    return star_map_group

def animate_star_twinkle(stars: VGroup, scene: Scene) -> None:
    """创建星星闪烁动画"""
    selected_stars = np.random.choice(
        stars.submobjects, 
        min(STAR_CONFIG["twinkle_count"], len(stars.submobjects)), 
        replace=False
    )
    
    twinkle_animations = AnimationGroup(*[
        Flash(star, color=WHITE, flash_radius=0.15, line_length=0.08, num_lines=8)
        for star in selected_stars
    ], lag_ratio=0.15)
    
    scene.play(twinkle_animations, run_time=2.5)

class OpeningScene(Scene):
    """开场场景：谜题的提出"""
    
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        
        # === 第一阶段：星空背景建立 ===
        print("🌟 创建星空背景...")
        stars = create_starfield(self)
        self.add(stars)
        
        # 星星闪烁效果
        animate_star_twinkle(stars, self)
        
        # === 第二阶段：程序生成的古老星图显现 ===
        print("🗺️  生成古老星图...")
        star_map = create_procedural_star_map(self)
        
        # 星图出现动画
        self.play(
            DrawBorderThenFill(star_map, run_time=4, lag_ratio=0.1),
            stars.animate.set_opacity(0.3)  # 让背景星星变暗，突出星图
        )
        self.wait(1)
        
        # === 第三阶段：神秘符号激活 ===
        print("✨ 激活神秘符号...")
        
        # 创建数学符号 - 这些将是我们解码的关键
        symbol1 = MathTex("2^5", color=YELLOW_C).scale(1.8).move_to(LEFT*2.5 + UP*1.5)
        symbol2 = MathTex("3^4", color=YELLOW_C).scale(1.8).move_to(RIGHT*2.5 + DOWN*1.5)
        
        # 符号出现动画
        self.play(
            FadeIn(symbol1, shift=UP*0.5, scale=1.2),
            FadeIn(symbol2, shift=DOWN*0.5, scale=1.2),
            run_time=2
        )
        
        # 符号发光效果
        self.play(
            Flash(symbol1, color=WHITE, flash_radius=1.2, line_length=0.7),
            Flash(symbol2, color=WHITE, flash_radius=1.2, line_length=0.7),
            # 同时让星图的几何图案也发光
            Flash(star_map[2][0], color=TEAL_C, flash_radius=0.5),  # 外圆
            Flash(star_map[2][1], color=TEAL_C, flash_radius=0.3),  # 内圆
            run_time=2.5
        )
        
        self.wait(1)
        
        # === 第四阶段：师徒对话 ===
        print("💬 开始师徒对话...")
        
        # Kai的疑问
        create_dialogue(
            character_name="Kai (凯)",
            text="大师，这张古老的星图真的沉睡了千年吗？\n我们...真的能唤醒它，找到那个传说中的失落星系？",
            character_color=ORANGE,
            scene=self
        )
        
        # Elara的回应
        create_dialogue(
            character_name="Elara (大师)",
            text="它一直在等待，凯。等待能读懂它语言的人。\n这语言，就是数学...",
            character_color=BLUE_B,
            scene=self
        )
        
        # === 第五阶段：符号的神秘联系揭示 ===
        print("🔗 揭示符号之间的联系...")
        
        # 在两个符号之间画一条神秘的连线
        connection_line = Line(symbol1.get_center(), symbol2.get_center(), 
                             color=PURPLE_C, stroke_width=3)
        connection_line.add_updater(lambda m: m.put_start_and_end_on(
            symbol1.get_center(), symbol2.get_center()))
        
        # 连线出现动画
        self.play(Create(connection_line), run_time=2)
        
        # 显示它们的计算结果
        result1 = MathTex("= 32", color=GREEN_C).scale(1.2).next_to(symbol1, RIGHT)
        result2 = MathTex("= 81", color=GREEN_C).scale(1.2).next_to(symbol2, LEFT)
        
        self.play(
            Write(result1),
            Write(result2),
            run_time=2
        )
        
        self.wait(2)
        
        # === 第六阶段：镜头聚焦，场景转换 ===
        print("🎬 准备场景转换...")
        
        # 聚焦到symbol1，为下一场景做准备
        self.play(
            self.camera.frame.animate.scale(0.6).move_to(symbol1),
            FadeOut(symbol2),
            FadeOut(result2), 
            FadeOut(connection_line),
            FadeOut(star_map, run_time=2),
            stars.animate.set_opacity(0.1),
            run_time=3
        )
        
        # 最后特写symbol1和它的结果
        self.play(
            symbol1.animate.set_color(WHITE),
            result1.animate.set_color(WHITE),
            run_time=1
        )
        
        self.wait(2)
        print("✅ 开场场景完成")

# === 场景测试运行 ===
if __name__ == "__main__":
    print("《解题的艺术》- 第一集开场场景 (无外部资源版)")