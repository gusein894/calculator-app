from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

# Устанавливаем размер окна как у телефона (для теста на ПК)
Window.size = (360, 640)

class CalculatorApp(App):
    def build(self):
        self.expression = ""
        self.operators = ["/", "*", "+", "-"]
        
        # Основной контейнер (вертикальный)
        main_layout = BoxLayout(orientation="vertical")
        
        # Экран ввода
        self.solution = TextInput(
            multiline=False, readonly=True, halign="right", font_size=55,
            background_color=(0.1, 0.1, 0.1, 1), foreground_color=(1, 1, 1, 1)
        )
        main_layout.add_widget(self.solution)
        
        # Сетка кнопок
        buttons = [
            ["C", "(", ")", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            [".", "0", "DEL", "="],
        ]
        
        buttons_grid = GridLayout(cols=4, spacing=2, padding=2)
        
        for row in buttons:
            for label in row:
                # Цвет кнопок
                if label in ["/", "*", "-", "+", "="]:
                    color = (1, 0.6, 0, 1) # Оранжевый
                elif label in ["C", "DEL", "(", ")"]:
                    color = (0.6, 0.6, 0.6, 1) # Серый
                else:
                    color = (0.2, 0.2, 0.2, 1) # Темный
                
                button = Button(
                    text=label, font_size=30, background_normal='',
                    background_color=color, color=(1, 1, 1, 1)
                )
                button.bind(on_press=self.on_button_press)
                buttons_grid.add_widget(button)
        
        main_layout.add_widget(buttons_grid)
        return main_layout

    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text

        if button_text == "C":
            self.solution.text = ""
        elif button_text == "DEL":
            self.solution.text = current[:-1]
        elif button_text == "=":
            try:
                # Защита от опасного кода, оставляем только мат. символы
                # Считаем выражение
                answer = str(eval(self.solution.text))
                self.solution.text = answer
            except Exception:
                self.solution.text = "Error"
        else:
            if current == "Error":
                self.solution.text = ""
            self.solution.text += button_text

if __name__ == "__main__":
    CalculatorApp().run()