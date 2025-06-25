# ========================================
# 《解题的艺术》动画系列 - The Art of Problem Solving Animation Series
# 第一集：指数的诞生 - Episode 01: The Birth of Exponents
# 场景01：开场谜题的提出 - Scene 01: Opening Mystery
# 版本：V1.3 (专业制作版)
# 基于《第一集创意设计定稿》严格实现
# ========================================

from manim import *
import numpy as np
import os
import json
from typing import List, Tuple, Optional

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
    "count": 120,  # 进一步优化性能
    "twinkle_count": 15,
    "radius_range": (0.01, 0.04),
    "area_range": (-8, 8)  # 稍微收缩范围
}

# --- 工具函数 ---
def check_assets(required_files: List[str]) -> Tuple[bool, List[str]]:
    """
    检查必需的资源文件是否存在
    
    Args:
        required_files: 必需文件路径列表
        
    Returns:
        (是否全部存在, 缺失文件列表)
    """
    missing = [f for f in required_files if not os.path.exists(f)]
    if missing:
        print("❌ 错误：缺失以下必要的资源文件：")
        for f in missing:
            print(f"   - {f}")
        return False, missing
    print("✅ 资源文件检查通过")
    return True, []

def load_dialogue_config(config_path: str) -> Optional[dict]:
    """
    从JSON文件加载对话配置（为未来扩展预留）
    
    Args:
        config_path: 配置文件路径
        
    Returns:
        对话配置字典或None
    """
    try:
        if os.path.exists(config_path):
            with open(config_path, 'r', encoding='utf-8') as f:
                return json.load(f)
    except Exception as e:
        print(f"⚠️  警告：无法加载对话配置文件 {config_path}: {e}")
    return None

def create_dialogue(character_name: str, text: str, character_color: str, scene: Scene) -> None:
    """
    创建角色对话动画
    
    Args:
        character_name: 角色名称
        text: 对话内容
        character_color: 角色颜色
        scene: 场景对象
    """
    # 动态计算等待时间：基础时间 + 文本长度调整
    base_time = 2.5
    text_length_factor = len(text.replace("\n", "")) * 0.12
    wait_time = max(base_time, text_length_factor)
    
    # 尝试使用中文字体，回退到默认字体
    fonts_to_try = ["Noto Sans CJK SC", "SimHei", "PingFang SC", "Microsoft YaHei"]
    name_text = None
    dialogue_text = None
    
    for font in fonts_to_try:
        try:
            name_text = Text(
                character_name, 
                font_size=DIALOGUE_CONFIG["font_size_name"], 
                color=character_color, 
                weight=BOLD, 
                font=font
            )
            dialogue_text = Text(
                text, 
                font_size=DIALOGUE_CONFIG["font_size_text"], 
                weight=NORMAL, 
                font=font
            )
            break
        except Exception:
            continue
    
    # 如果所有字体都失败，使用默认字体
    if name_text is None:
        name_text = Text(character_name, font_size=DIALOGUE_CONFIG["font_size_name"], color=character_color, weight=BOLD)
        dialogue_text = Text(text, font_size=DIALOGUE_CONFIG["font_size_text"], weight=NORMAL)
    
    # 组装对话框
    content = VGroup(name_text, dialogue_text).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
    dialogue_box = SurroundingRectangle(
        content,
        corner_radius=DIALOGUE_CONFIG["box_corner_radius"],
        buff=DIALOGUE_CONFIG["box_buff"],
        fill_opacity=DIALOGUE_CONFIG["box_opacity"],
        fill_color=BACKGROUND_COLOR,
        stroke_color=character_color,
        stroke_width=2
    )
    dialogue_group = VGroup(dialogue_box, content).to_corner(UL, buff=DIALOGUE_CONFIG["position_buff"])
    
    # 动画序列
    # {Audio Cue: character_name dialogue start}
    scene.play(Write(dialogue_group), run_time=1.5)
    scene.wait(wait_time)
    scene.play(FadeOut(dialogue_group), run_time=1.0)
    # {Audio Cue: character_name dialogue end}

def create_starfield(scene: Scene) -> VGroup:
    """
    创建星空背景
    
    Args:
        scene: 场景对象
        
    Returns:
        星星群组
    """
    # 生成随机星点位置
    positions = [
        np.array([
            np.random.uniform(-STAR_CONFIG["area_range"][0], STAR_CONFIG["area_range"][1]),
            np.random.uniform(-STAR_CONFIG["area_range"][0], STAR_CONFIG["area_range"][1]),
            0
        ]) for _ in range(STAR_CONFIG["count"])
    ]
    
    # 创建星星
    stars = VGroup(*[
        Dot(
            pos, 
            radius=np.random.uniform(*STAR_CONFIG["radius_range"]), 
            color=WHITE,
            fill_opacity=np.random.uniform(0.3, 1.0)  # 随机透明度增加层次
        ) for pos in positions
    ])
    
    return stars

def animate_star_twinkle(stars: VGroup, scene: Scene) -> None:
    """
    创建星星闪烁动画
    
    Args:
        stars: 星星群组
        scene: 场景对象
    """
    # 随机选择要闪烁的星星
    selected_stars = np.random.choice(
        stars.submobjects, 
        min(STAR_CONFIG["twinkle_count"], len(stars.submobjects)), 
        replace=False
    )
    
    # 创建闪烁动画组
    twinkle_animations = AnimationGroup(*[
        Flash(
            star, 
            color=WHITE, 
            flash_radius=0.15, 
            line_length=0.08,
            num_lines=8
        ) for star in selected_stars
    ], lag_ratio=0.15)
    
    scene.play(twinkle_animations, run_time=2.5)

class OpeningScene(Scene):
    """
    开场场景：谜题的提出
    
    故事背景：师徒二人在古老的星图前，准备开始解码之旅
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = BACKGROUND_COLOR
        
        # === 第一阶段：资源检查 ===
        required_assets = ["assets/ep01/star_map_background.png"]
        assets_ok, missing_files = check_assets(required_assets)
        
        if not assets_ok:
            # 显示错误信息
            error_text = Text(
                f"❌ 资源文件缺失\n请检查以下文件：\n" + "\n".join(f"• {f}" for f in missing_files),
                color=RED,
                font_size=32
            )
            self.add(error_text)
            self.wait(5)
            return
        
        # === 第二阶段：星空背景建立 ===
        print("🌟 创建星空背景...")
        stars = create_starfield(self)
        self.add(stars)
        
        # 星星闪烁效果
        animate_star_twinkle(stars, self)
        
        # === 第三阶段：古老星图显现 ===
        print("🗺️  加载古老星图...")
        star_map = ImageMobject("assets/ep01/star_map_background.png")
        star_map.set_opacity(0.4)
        star_map.scale(1.1)  # 稍微放大以增强视觉冲击力
        
        self.play(FadeIn(star_map, scale=1.2), run_time=3)
        self.wait(1)
        
        # === 第四阶段：神秘符号激活 ===
        print("✨ 激活神秘符号...")
        
        # 创建数学符号
        symbol1 = MathTex("2^5", color=YELLOW_C).scale(1.8).move_to(LEFT*2.5 + UP*1.5)
        symbol2 = MathTex("3^4", color=YELLOW_C).scale(1.8).move_to(RIGHT*2.5 + DOWN*1.5)
        
        # 符号出现动画
        self.play(
            FadeIn(symbol1, shift=UP*0.5),
            FadeIn(symbol2, shift=DOWN*0.5),
            run_time=2
        )
        
        # 符号发光效果
        self.play(
            Flash(symbol1, color=WHITE, flash_radius=1.2, line_length=0.7),
            Flash(symbol2, color=WHITE, flash_radius=1.2, line_length=0.7),
            run_time=2.5
        )
        
        self.wait(1)
        
        # === 第五阶段：师徒对话 ===
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
        
        # === 第六阶段：镜头聚焦，场景转换 ===
        print("🎬 准备场景转换...")
        
        # 聚焦到symbol1，为下一场景做准备
        self.play(
            self.camera.frame.animate.scale(0.5).move_to(symbol1),
            FadeOut(symbol2, shift=DOWN),
            FadeOut(star_map, run_time=2),
            run_time=3
        )
        
        self.wait(2)
        print("✅ 开场场景完成")

# === 场景测试和调试辅助 ===
if __name__ == "__main__":
    # 本地测试时可以运行的代码
    print("《解题的艺术》- 第一集开场场景")
    print("准备渲染...")
    # 这里可以添加一些测试代码

