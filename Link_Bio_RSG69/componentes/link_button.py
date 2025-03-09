from turtle import width
import reflex as rx
import reflex_chakra as rc
import Link_Bio_RSG69.estilos.estilos as estilos

def link_button(title: str, body: str, url: str)-> rx.Component:
    return rx.link(
        rc.button(#esto lo pongo yo para que sea igual que el tutorial y ademas sale la mano en el cursor
            rx.hstack(
                rx.icon(
                    tag="arrow-right",
                    width=estilos.Size.BIG.value,
                    height=estilos.Size.BIG.value,
                ),
                rx.vstack(
                    rx.text(
                        title,
                        style=estilos.button_title_style,
                    ),
                    rx.text(
                        body,
                        style=estilos.button_body_style,
                    ),
                    align_items="star",
                ),
                align="center",# esto lo pongo yo para que se centre todo y el icono se ponga entre los 2 textos
            ),
        ),
        href=url,
        is_external=True,
        width = "100%",#(1) - css hace que el link sea igual de ancho que esl texto mas ancho
    )
    