from taipy.gui import Gui, navigate
import taipy.gui.builder as tgb


def mm_faceswap_pressed(state):
    navigate(state, "faceswap")


if __name__ == "__main__":
    with tgb.Page() as root_page:
        tgb.text("# ComfyUI - Ino Bridge", mode="md")

    with tgb.Page() as menu_page:
        tgb.text("# Menu", mode="md")
        tgb.button("Face swap", on_action=mm_faceswap_pressed)

    with tgb.Page() as faceswap_page:
        tgb.text("# Face swap", mode="md")

    pages = {
        "/": root_page,
        "menu": menu_page,
        "faceswap": faceswap_page,
    }

    gui = Gui()
    gui.add_pages(pages)
    gui.run(title="ComfyUI - Ino Bridge")