import reflex as rx
import reflex_chakra as rc
from  Link_Bio_RSG69.componentes.link_button import link_button
from Link_Bio_RSG69.componentes.titulo import titulo as titulo
import Link_Bio_RSG69.constantes as const

def links()-> rx.Component:
    return rx.vstack(
        #utilizo chakra para que sea igual que el tutorial
        titulo("Comunidad"),
        link_button(
            "Twitch",
            "Directos de Lunes a Viernes",
            const.TWITCH_URL,
        ),
        link_button(
            "YouTube",
            "Tutoriales Semanales",
            "https://youtube.com/@mouredev",
        ),
        link_button(
            "Tutoriales Semanales",
            "Tutoriales Semanales",
            "https://youtube.com/@mouredevtv",
        ), 
        link_button (
            "Discord",
            "El chat de  la comunidad",
            "https://discord.gg/mouredev",
        ),
        titulo("Comunidad"),
        link_button(
            "Twitch",
            "Directos de Lunes a Viernes",
            "https://twitter.com/mouredev",
        ),
        link_button(
            "YouTube",
            "Tutoriales Semanales",
            "https://youtube.com/@mouredev",
        ),
        link_button(
            "Tutoriales Semanales",
            "Tutoriales Semanales",
            "https://youtube.com/@mouredevtv",
        ), 
        link_button (
            "Discord",
            "El chat de  la comunidad",
            "https://discord.gg/mouredev",
        ),
        width = "100%",#esto es para que ocupen los botones todo el ancho
        spacing="3",
        #align="center",#esto lo pongo yo
    )