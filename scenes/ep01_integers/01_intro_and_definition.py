from manim import *
import numpy as np

class AtlantisExponentStory(Scene):
    def construct(self):
        # Scene 1: Opening - The Mysterious Star Map (00:00 - 00:45)
        self.opening_scene()
        self.wait(1)
        self.clear()
        
        # Scene 2: Birth of Exponents (00:46 - 01:50)
        self.birth_of_exponents()
        self.wait(1)
        self.clear()
        
        # Scene 3: Multiplication and Division Rules (01:51 - 03:30)
        self.multiplication_division_rules()
        self.wait(1)
        self.clear()
        
        # Scene 4: Zero Exponent (03:31 - 05:30)
        self.zero_exponent_mystery()
        self.wait(1)
        self.clear()
        
        # Scene 5: Negative Exponent (05:31 - 07:00)
        self.negative_exponent_secret()
        self.wait(1)
        self.clear()
        
        # Scene 6: Final Revelation (07:01 - 08:00)
        self.final_revelation()

    def opening_scene(self):
        # Create underwater observatory atmosphere
        background = Rectangle(width=14, height=8, fill_color=DARK_BLUE, fill_opacity=0.8)
        self.add(background)
        
        # Create crystal dome effect
        dome = Arc(radius=6, angle=PI, color=BLUE, stroke_width=3)
        dome.shift(UP * 2)
        
        # Starlight effects
        stars = VGroup()
        for _ in range(20):
            star = Dot(radius=0.05, color=WHITE)
            star.move_to([
                np.random.uniform(-6, 6),
                np.random.uniform(2, 6),
                0
            ])
            stars.add(star)
        
        # Ancient star map
        star_map = Rectangle(width=8, height=4, color=GOLD, stroke_width=2)
        star_map.shift(DOWN * 0.5)
        
        # Mysterious symbols on the map
        symbol_25 = MathTex("2^5", color=YELLOW, font_size=48)
        symbol_25.move_to(star_map.get_center() + LEFT * 2 + UP * 0.5)
        
        symbol_34 = MathTex("3^4", color=YELLOW, font_size=48)
        symbol_34.move_to(star_map.get_center() + RIGHT * 2 + DOWN * 0.5)
        
        # Dim other areas of the map
        dim_areas = VGroup()
        for i in range(8):
            dim_dot = Dot(radius=0.1, color=GRAY, fill_opacity=0.3)
            dim_dot.move_to([
                np.random.uniform(-3.5, 3.5),
                np.random.uniform(-1.5, 1.5),
                0
            ])
            dim_areas.add(dim_dot)
        
        # Animation sequence
        self.play(FadeIn(background), FadeIn(dome), FadeIn(stars))
        self.wait(0.5)
        self.play(FadeIn(star_map))
        self.wait(0.5)
        self.play(FadeIn(dim_areas))
        self.wait(0.5)
        self.play(
            Write(symbol_25),
            Write(symbol_34),
            run_time=2
        )
        
        # Glowing effect for active symbols
        self.play(
            symbol_25.animate.set_color(BRIGHT_YELLOW),
            symbol_34.animate.set_color(BRIGHT_YELLOW),
            run_time=1
        )
        
        # Title text
        title = Text("The Atlantis Observatory", font_size=36, color=GOLD)
        title.to_edge(UP)
        self.play(Write(title))
        
        self.wait(2)

    def birth_of_exponents(self):
        # Create ancient teaching stone tablet
        tablet = Rectangle(width=10, height=6, color=GRAY, fill_color=DARK_GRAY, fill_opacity=0.7)
        
        # Show repeated addition
        addition_expr = MathTex("2", "+", "2", "+", "2", "+", "2", "+", "2", color=WHITE, font_size=40)
        self.play(FadeIn(tablet), Write(addition_expr))
        self.wait(1)
        
        # Transform to multiplication
        multiplication_expr = MathTex("5", "\\times", "2", color=YELLOW, font_size=40)
        self.play(Transform(addition_expr, multiplication_expr))
        self.wait(1)
        
        # Show repeated multiplication
        mult_repeated = MathTex("2", "\\times", "2", "\\times", "2", "\\times", "2", "\\times", "2", 
                               color=WHITE, font_size=40)
        mult_repeated.shift(DOWN * 1)
        self.play(Write(mult_repeated))
        self.wait(1)
        
        # Transform to exponent notation
        exponent_expr = MathTex("2^5", color=BRIGHT_YELLOW, font_size=60)
        
        # Create transformation animation
        self.play(
            Transform(mult_repeated, exponent_expr),
            run_time=2
        )
        
        # Add labels
        base_label = Text("Base (底数)", font_size=24, color=GREEN)
        base_label.next_to(exponent_expr, DOWN + LEFT)
        
        exponent_label = Text("Exponent (指数)", font_size=24, color=BLUE)
        exponent_label.next_to(exponent_expr, UP + RIGHT)
        
        # Draw arrows
        base_arrow = Arrow(base_label.get_top(), exponent_expr.get_bottom() + LEFT * 0.3, color=GREEN)
        exp_arrow = Arrow(exponent_label.get_bottom(), exponent_expr.get_top() + RIGHT * 0.3, color=BLUE)
        
        self.play(
            Write(base_label),
            Write(exponent_label),
            Create(base_arrow),
            Create(exp_arrow)
        )
        
        # Add meaning text
        meaning_text = VGroup(
            Text("力量的基石", font_size=20, color=GREEN),
            Text("重复的次数", font_size=20, color=BLUE)
        )
        meaning_text[0].next_to(base_label, DOWN)
        meaning_text[1].next_to(exponent_label, DOWN)
        
        self.play(Write(meaning_text))
        self.wait(2)

    def multiplication_division_rules(self):
        # Create crystal fragments
        crystal1 = self.create_crystal("2^3", LEFT * 3)
        crystal2 = self.create_crystal("2^2", RIGHT * 3)
        
        self.play(FadeIn(crystal1), FadeIn(crystal2))
        self.wait(1)
        
        # Show expansion
        expansion1 = MathTex("(2 \\times 2 \\times 2)", color=YELLOW, font_size=32)
        expansion1.next_to(crystal1, DOWN)
        
        expansion2 = MathTex("(2 \\times 2)", color=YELLOW, font_size=32)
        expansion2.next_to(crystal2, DOWN)
        
        self.play(Write(expansion1), Write(expansion2))
        self.wait(1)
        
        # Bring crystals together
        self.play(
            crystal1.animate.move_to(LEFT * 1),
            crystal2.animate.move_to(RIGHT * 1),
            expansion1.animate.move_to(LEFT * 1 + DOWN * 1),
            expansion2.animate.move_to(RIGHT * 1 + DOWN * 1)
        )
        
        # Show multiplication symbol
        mult_symbol = MathTex("\\times", color=WHITE, font_size=48)
        mult_symbol.move_to(ORIGIN)
        self.play(Write(mult_symbol))
        
        # Show fusion
        combined_expansion = MathTex("2 \\times 2 \\times 2 \\times 2 \\times 2", color=YELLOW, font_size=32)
        combined_expansion.shift(DOWN * 2)
        self.play(Write(combined_expansion))
        
        # Show exponent addition
        exponent_addition = MathTex("3 + 2 = 5", color=GREEN, font_size=36)
        exponent_addition.shift(UP * 2)
        self.play(Write(exponent_addition))
        
        # Final result
        result_crystal = self.create_crystal("2^5", ORIGIN + UP * 0.5)
        self.play(
            FadeOut(crystal1),
            FadeOut(crystal2),
            FadeOut(mult_symbol),
            FadeIn(result_crystal)
        )
        
        # Show the rule
        rule = MathTex("a^m \\cdot a^n = a^{m+n}", color=BRIGHT_YELLOW, font_size=48)
        rule.shift(DOWN * 3)
        self.play(Write(rule))
        self.wait(2)
        
        # Division rule demonstration
        self.play(FadeOut(VGroup(*self.mobjects)))
        
        division_demo = MathTex("\\frac{2^5}{2^2} = 2^{5-2} = 2^3", color=YELLOW, font_size=48)
        self.play(Write(division_demo))
        
        division_rule = MathTex("\\frac{a^m}{a^n} = a^{m-n}", color=BRIGHT_YELLOW, font_size=48)
        division_rule.shift(DOWN * 2)
        self.play(Write(division_rule))
        self.wait(2)

    def zero_exponent_mystery(self):
        # Mysterious symbol appears
        mystery_symbol = MathTex("3^0", color=PURPLE, font_size=72)
        mystery_symbol.shift(UP * 2)
        
        question_mark = Text("?", font_size=96, color=RED)
        question_mark.next_to(mystery_symbol, RIGHT)
        
        self.play(Write(mystery_symbol), Write(question_mark))
        self.wait(1)
        
        # Show the logical deduction
        logic_text = Text("Let's use logic to find the answer:", font_size=32, color=WHITE)
        logic_text.shift(UP * 0.5)
        self.play(Write(logic_text))
        
        # Two-screen comparison
        left_screen = Rectangle(width=5, height=4, color=BLUE)
        left_screen.shift(LEFT * 3.5 + DOWN * 1)
        left_title = Text("Real World", font_size=24, color=BLUE)
        left_title.next_to(left_screen, UP)
        
        right_screen = Rectangle(width=5, height=4, color=GREEN)
        right_screen.shift(RIGHT * 3.5 + DOWN * 1)
        right_title = Text("Symbol World", font_size=24, color=GREEN)
        right_title.next_to(right_screen, UP)
        
        self.play(
            Create(left_screen), Create(right_screen),
            Write(left_title), Write(right_title)
        )
        
        # Left screen: fraction simplification
        left_content = MathTex("\\frac{2^3}{2^3} = \\frac{8}{8} = 1", color=BLUE, font_size=32)
        left_content.move_to(left_screen.get_center())
        
        # Right screen: exponent rule
        right_content = MathTex("\\frac{2^3}{2^3} = 2^{3-3} = 2^0", color=GREEN, font_size=32)
        right_content.move_to(right_screen.get_center())
        
        self.play(Write(left_content), Write(right_content))
        self.wait(1)
        
        # Connect with a beam of light
        connection_line = Line(left_content.get_right(), right_content.get_left(), color=YELLOW, stroke_width=4)
        self.play(Create(connection_line))
        
        # Final revelation
        revelation = MathTex("2^0 = 1", color=BRIGHT_YELLOW, font_size=64)
        revelation.shift(DOWN * 3)
        self.play(Write(revelation))
        
        # General rule
        general_rule = MathTex("a^0 = 1 \\text{ (where } a \\neq 0\\text{)}", color=GOLD, font_size=40)
        general_rule.shift(DOWN * 4)
        self.play(Write(general_rule))
        self.wait(2)

    def negative_exponent_secret(self):
        # Show negative exponent symbol
        negative_symbol = MathTex("3^{-2}", color=RED, font_size=72)
        negative_symbol.shift(UP * 2)
        
        anti_energy_text = Text("Anti-Energy?", font_size=32, color=RED)
        anti_energy_text.next_to(negative_symbol, DOWN)
        
        self.play(Write(negative_symbol), Write(anti_energy_text))
        self.wait(1)
        
        # Show crystal fusion demonstration
        positive_crystal = self.create_crystal("3^2", LEFT * 3)
        negative_crystal = self.create_crystal("3^{-2}", RIGHT * 3)
        negative_crystal.set_color(RED)
        
        self.play(FadeIn(positive_crystal), FadeIn(negative_crystal))
        self.wait(1)
        
        # Show them coming together
        self.play(
            positive_crystal.animate.move_to(LEFT * 1),
            negative_crystal.animate.move_to(RIGHT * 1)
        )
        
        # Show exponent addition
        exponent_calc = MathTex("2 + (-2) = 0", color=YELLOW, font_size=36)
        exponent_calc.shift(UP * 0.5)
        self.play(Write(exponent_calc))
        
        # Result is unit energy
        unit_crystal = self.create_crystal("3^0 = 1", ORIGIN)
        unit_crystal.set_color(GOLD)
        
        self.play(
            FadeOut(positive_crystal),
            FadeOut(negative_crystal),
            FadeIn(unit_crystal)
        )
        
        # Logical deduction
        deduction_text = Text("If 3² × 3⁻² = 1, then 3⁻² must be...", font_size=28, color=WHITE)
        deduction_text.shift(DOWN * 1.5)
        self.play(Write(deduction_text))
        
        # Final answer
        answer = MathTex("3^{-2} = \\frac{1}{3^2} = \\frac{1}{9}", color=BRIGHT_YELLOW, font_size=48)
        answer.shift(DOWN * 2.5)
        self.play(Write(answer))
        
        # General rule
        general_rule = MathTex("a^{-n} = \\frac{1}{a^n}", color=GOLD, font_size=40)
        general_rule.shift(DOWN * 3.5)
        self.play(Write(general_rule))
        self.wait(2)

    def final_revelation(self):
        # Create the complete star map
        star_map = Rectangle(width=12, height=8, color=GOLD, stroke_width=3)
        
        # All the symbols now glowing
        symbols = VGroup(
            MathTex("2^5", color=BRIGHT_YELLOW, font_size=36),
            MathTex("3^4", color=BRIGHT_YELLOW, font_size=36),
            MathTex("a^0 = 1", color=BRIGHT_YELLOW, font_size=32),
            MathTex("a^{-n} = \\frac{1}{a^n}", color=BRIGHT_YELLOW, font_size=28),
            MathTex("a^m \\cdot a^n = a^{m+n}", color=BRIGHT_YELLOW, font_size=28)
        )
        
        # Position symbols around the map
        symbols[0].move_to(star_map.get_center() + LEFT * 4 + UP * 2)
        symbols[1].move_to(star_map.get_center() + RIGHT * 4 + UP * 2)
        symbols[2].move_to(star_map.get_center() + LEFT * 4 + DOWN * 2)
        symbols[3].move_to(star_map.get_center() + RIGHT * 4 + DOWN * 2)
        symbols[4].move_to(star_map.get_center() + UP * 3)
        
        self.play(FadeIn(star_map))
        
        # Light beams from symbols to center
        center = star_map.get_center()
        light_beams = VGroup()
        
        for symbol in symbols:
            beam = Line(symbol.get_center(), center, color=YELLOW, stroke_width=2)
            light_beams.add(beam)
            self.play(Write(symbol), Create(beam), run_time=0.5)
        
        # Create the lost galaxy hologram
        galaxy = self.create_galaxy_hologram()
        galaxy.move_to(center)
        
        self.play(FadeIn(galaxy), run_time=3)
        
        # Final inspirational text
        final_text = VGroup(
            Text("We didn't invent anything...", font_size=28, color=WHITE),
            Text("We discovered the natural patterns", font_size=28, color=WHITE),
            Text("that were always there.", font_size=28, color=WHITE),
            Text("This is the Art of Problem Solving.", font_size=32, color=GOLD)
        )
        
        for i, text in enumerate(final_text):
            text.shift(DOWN * (4 + i * 0.5))
            self.play(Write(text), run_time=1)
        
        self.wait(3)

    def create_crystal(self, text, position):
        """Create a crystal-like container with text"""
        crystal_shape = RegularPolygon(n=6, color=BLUE, fill_opacity=0.3)
        crystal_text = MathTex(text, color=WHITE, font_size=32)
        crystal = VGroup(crystal_shape, crystal_text)
        crystal.move_to(position)
        return crystal

    def create_galaxy_hologram(self):
        """Create a beautiful galaxy hologram effect"""
        galaxy = VGroup()
        
        # Central bright core
        core = Circle(radius=0.3, color=WHITE, fill_opacity=0.8)
        galaxy.add(core)
        
        # Spiral arms
        for i in range(4):
            arm = ParametricFunction(
                lambda t: np.array([
                    (1 + 0.3 * t) * np.cos(t + i * PI/2),
                    (1 + 0.3 * t) * np.sin(t + i * PI/2),
                    0
                ]),
                t_range=[0, 4*PI],
                color=BLUE,
                stroke_width=2
            )
            galaxy.add(arm)
        
        # Add some stars
        for _ in range(20):
            star = Dot(
                radius=0.03,
                color=np.random.choice([WHITE, YELLOW, BLUE]),
                fill_opacity=0.8
            )
            angle = np.random.uniform(0, 2*PI)
            radius = np.random.uniform(0.5, 2)
            star.move_to([
                radius * np.cos(angle),
                radius * np.sin(angle),
                0
            ])
            galaxy.add(star)
        
        return galaxy

# To run this animation, save as a .py file and use:
# manim -pql filename.py AtlantisExponentStory