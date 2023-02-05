import flet
from flet import Container, ElevatedButton, Page, animation

from flet.transform import Scale


def main(page):
    a = Container(width=150, height=150, bgcolor='red', border_radius=10, animate_opacity=3)

    def animate_opacity(e):
        a.opacity = 0 if a.opacity == 1 else 1
        a.update()

    b = Container(width=150, height=150, bgcolor='yellow', border_radius=10, scale=Scale(scale=1),
                  animate_scale=animation.Animation(600, 'bounceOut'))

    def animate(e):
        b.scale = 2 if b.scale == 1 else 1
        b.update()

    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    page.spacing = 30
    page.add(a, ElevatedButton("Animation opacity", on_click=animate_opacity))
    page.add(b, ElevatedButton("Animation scale", on_click=animate))


flet.app(target=main)
