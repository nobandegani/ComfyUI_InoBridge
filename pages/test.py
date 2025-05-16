from taipy.gui import Gui
import taipy.gui.builder as tgb


pane_is_visible = False
name = ""

def show_or_hide_pane(state):
    state.pane_is_visible = not state.pane_is_visible

with tgb.Page() as page:
    tgb.button("Show pane", on_action=show_or_hide_pane)

    with tgb.pane(open="{pane_is_visible}"):
        tgb.text("Enter a name:")
        tgb.input("{name}")

Gui(page).run()