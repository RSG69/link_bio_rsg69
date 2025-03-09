import reflex as rx
from prueba.estilos.estilos import Size as Size
def navbar() -> rx.Component:
    return rx.hstack(
            rx.text(
                   "RSG69",
                ),
                position="sticky",#css -> posicion fija
                bg="lightgray",
                padding_x=Size.DEFAULT.value,
                padding_Y=Size.SMALL.value,
                z_index="999",#css -> indicarle que este siembre el primero (arriba)
                top="0",#css para que la barra no se vaya para arriba
            )