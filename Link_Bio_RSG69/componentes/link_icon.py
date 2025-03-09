import reflex as rx
import prueba.estilos.estilos as estilos

def link_icon(url: str)-> rx.Component:
    return rx.link(
        rx.icon(
            tag="link",
        ),
        href=url,
        is_external=True,
    )