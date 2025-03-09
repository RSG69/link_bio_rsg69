import reflex as rx
import datetime
from prueba.estilos.estilos import Size as Size


def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src="favicon.ico"),
         rx.link(
            f"© 2014-{datetime.date.today().year} Robert69 BY Roberto Sobreviela v0.1",
            href="https://mouredev.com",
            is_external=True,
            font_size=Size.MEDIUM.value,
            margin_top="0px!important"
        ),
        rx.text(
            "BUILDING SOFTWARE WITH ♥ FROM ZARAGOZA TO THE WORLD",
            font_size=Size.MEDIUM.value,
        ),
        margin_bottom=Size.BIG.value,
        align = "center", #Esto lo tengo que poner yo

    )