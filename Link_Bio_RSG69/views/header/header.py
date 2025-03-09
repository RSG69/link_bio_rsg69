import reflex as rx
import reflex_chakra as rc
from prueba.estilos.estilos import Size as Size
from prueba.componentes.link_icon import link_icon
from prueba.componentes.info_text import info_text
from prueba.estilos.estilos import Size as Size

def header()-> rx.Component:
    return rx.vstack(
        rx.hstack(#rto es para que el avatar y las 2 linea esten en la misma linea
            rc.avatar(
                name="Roberto Sobreviela",
                size="xl",
            ),
            rx.vstack(#con esto conseguimos que los texto salgan uno debajo uno del otro
                rx.heading(
                    "Roberto Sobreviela Garces",
                    size="6",
                ),
                rx.text(
                    "69RSG69@gmail.com",
                    margin_top=Size.ZERO.value,#no veo que pegue al texto de arriba
                ),
                rx.hstack(
                    link_icon("https://x.com/mouredev"),
                    link_icon("https://x.com/mouredev"),
                    link_icon("https://x.com/mouredev"),
                ),
                align_items="start",
                #align="center",#esto lo pongo yo
            ),  
            spacing="5",
        ),
        rx.flex(
            info_text("+13+","años de experiencia"),
            rx.spacer(),
            info_text("+100","aplicaciones creadas"),
            rx.spacer(),
            info_text("+1M","seguisores"),
            width="100%",

        ),
        rx.text(
            """Soy ingeniero de software desde hace mas de {experience()} años.
            Actualmente trabajo como freelance full-stack developer iOS y Android.
            Además, creo contenido formativo sobre programación en redes.
            Aquí podrás encontrar todos mis enlaces de interés ¡Bienvenid@!"""
        ),
        spacing="8",#propiedad del compoenete Stack que deja espacios entre los componentes que contienen
        align_items="start",
    )