"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
import Link_Bio_RSG69.estilos.estilos as styles
from Link_Bio_RSG69.estilos.estilos import Size as Size
from Link_Bio_RSG69.views.links.links import links


from rxconfig import config


class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    return rx.box(
        #navbar(),
        rx.center(
            rx.vstack( 
                #header(),
                links(),
                #stylos css usando pyton
                max_width = styles.MAX_WIDTH,
                width = "100%",
                margin_y = Size.BIG.value,
                #stylos del componenete vstack
                align = "center", #Esto lo tengo que poner yo
            ),
        ),
        #footer(),
    )


app=rx.App(
    style=styles.BASE_STYLE
)
app.add_page(index)

