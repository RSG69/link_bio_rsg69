import reflex as rx
import reflex_chakra as rc
from prueba.estilos.estilos import Size as Size

def info_text(title: str, body:str)-> rx.Component:
    return rx.box(
        rc.span(
            title,
            font_weight="bold",
            color="blue",
        ),
        f" {body}",
        font_size=Size.MEDIUM.value,

    )