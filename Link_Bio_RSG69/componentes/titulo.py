import reflex as rx
import Link_Bio_RSG69.estilos.estilos as estilos

def titulo(text: str) -> rx.Component:
    return rx.heading(
        text,
        style=estilos.title_style,   
        size="6",                                                                                                                                                                                                                                                                                                                                                   
    )
