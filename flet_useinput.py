# import flet
# from flet import IconButton,Page,Row,TextField,icons

# def main(page:Page):
#     page.title = 'Example'
#     page.vertical_alignment = 'center'
#     txt_number = TextField(value='0',text_align='right',width=100)

#     def mines(e):
#         txt_number.value = int(txt_number.value)-1
#         page.update()
#     def add(e):
#         txt_number.value = int(txt_number.value)+1
#         page.update()

#     page.add(
#         Row([IconButton(icons.REMOVE,on_click=mines),
#         txt_number,
#         IconButton(icons.ADD_A_PHOTO,on_click=add)
#     ],
#         alignment = 'center'
#     )
#     )
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

import flet as ft
from flet.matplotlib_chart import MatplotlibChart

matplotlib.use("svg")


def main(page: ft.Page):
    # Fixing random state for reproducibility
    np.random.seed(19680801)

    dt = 0.01
    t = np.arange(0, 30, dt)
    nse1 = np.random.randn(len(t))  # white noise 1
    nse2 = np.random.randn(len(t))  # white noise 2

    # Two signals with a coherent part at 10Hz and a random part
    s1 = np.sin(2 * np.pi * 10 * t) + nse1
    s2 = np.sin(2 * np.pi * 10 * t) + nse2

    fig, axs = plt.subplots(2, 1)
    axs[0].plot(t, s1, t, s2)
    axs[0].set_xlim(0, 2)
    axs[0].set_xlabel("time")
    axs[0].set_ylabel("s1 and s2")
    axs[0].grid(True)

    cxy, f = axs[1].cohere(s1, s2, 256, 1.0 / dt)
    axs[1].set_ylabel("coherence")

    fig.tight_layout()

    page.add(MatplotlibChart(fig, expand=True))


ft.app(target=main)
