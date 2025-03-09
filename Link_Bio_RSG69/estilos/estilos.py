import reflex as rx
import reflex_chakra as rc
from enum import Enum

MAX_WIDTH = "560px",

class Size(Enum):
    ZERO = "0px !important"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    LARGE = "1.5em"
    BIG = "2em"
    VERY_BIG = "4em"

BASE_STYLE = {
     rc.button: {
        "width": "100%",
        "height": "100%",
        "display":"block",#css alinear todo lo del boton a izquierda
        "padding": Size.SMALL.value,#css poner margen dentro del boton        
        "border_radius": Size.DEFAULT.value,#css
     },

     rx.link: {
        #"color": TextColor.BODY.value,
        "text_decoration": "none",
        "_hover": {},
    },
}

title_style = dict(
    width="100%",
    padding_top=Size.DEFAULT.value,
)

button_title_style = dict(
    font_size=Size.DEFAULT.value,
)

button_body_style = dict(
    font_size=Size.MEDIUM.value,
)

  