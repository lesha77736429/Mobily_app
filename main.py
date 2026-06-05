import flet as ft

def main(page: ft.Page):
    page.title = "Симулятор"
    page.theme_mode = ft.ThemeMode.DARK
    
    # Координаты передач (в процентах от ширины/высоты контейнера)
    positions = {
        'R': (0.1, 0.1), '1': (0.35, 0.1), '3': (0.6, 0.1), '5': (0.85, 0.1),
        'N': (0.6, 0.5), '2': (0.35, 0.9), '4': (0.6, 0.9), '6': (0.85, 0.9),
    }

    current_gear_text = ft.Text("N", size=60, weight=ft.FontWeight.BOLD)
    
    # Функция обновления визуализации
    def update_gear_visuals(gear_key):
        current_gear_text.value = gear_key
        shift_knob.content.value = gear_key
        
        # Меняем цвет всех кнопок на белый, активную на синий ("#42A5F5")
        for gear in gear_containers:
            gear.content.color = "#42A5F5" if gear.data == gear_key else "white"
        page.update()

    # Создание кнопок передач
    gear_containers = []
    for key, (x, y) in positions.items():
        gear_btn = ft.Container(
            content=ft.Text(key, size=30, weight=ft.FontWeight.BOLD, color="white"),
            left=x * 300, top=y * 500,
            data=key, # храним имя передачи внутри объекта
            on_click=lambda e: update_gear_visuals(e.control.data)
        )
        gear_containers.append(gear_btn)

    # Визуализация линий (H-схема)
    lines = [
        ft.Container(bgcolor="white", width=2, height=450, left=45, top=50), # R
        ft.Container(bgcolor="white", width=2, height=450, left=120, top=50), # 1-2
        ft.Container(bgcolor="white", width=2, height=450, left=195, top=50), # 3-4
        ft.Container(bgcolor="white", width=2, height=450, left=270, top=50), # 5-6
        ft.Container(bgcolor="white", width=250, height=2, left=45, top=275), # N-line
    ]

    # Ручка КПП
    shift_knob = ft.Container(
        content=ft.Text("N", size=20, color="black", weight=ft.FontWeight.BOLD),
        # ИСПОЛЬЗУЕМ НОВЫЙ СПОСОБ ВЫРАВНИВАНИЯ:
        alignment=ft.Alignment(0, 0), 
        width=60, height=60,
        bgcolor="#E0E0E0", # Светло-серый цвет
        border_radius=30,
        left=175, top=245,
    )

    gearbox_area = ft.Container(
        content=ft.Stack([*lines, *gear_containers, shift_knob]),
        width=320, height=550,
        bgcolor="#222222", # Темно-серый цвет фона коробки
        border_radius=20,
    )

    page.add(
        ft.Column([
            ft.Text("Симулятор КПП", size=24),
            current_gear_text,
            gearbox_area
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    )

if __name__ == "__main__":
    ft.app(target=main)