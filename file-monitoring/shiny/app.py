from shiny import Inputs, Outputs, Session, App, render, ui, reactive
from pathlib import Path
import pandas as pd
from datetime import datetime


@reactive.file_reader(Path(__file__).parent / "logs.csv")
def logs():
    return pd.read_csv(Path(__file__).parent / "logs.csv")


app_ui = ui.page_fillable(
    ui.layout_column_wrap(
        ui.card(ui.output_data_frame("df")),
        ui.card(ui.input_text("txt_in", "Enter text"), ui.output_text("text_out")),
        width=1 / 2,
    )
)


def server(input: Inputs, output: Outputs, session: Session):
    @render.data_frame
    def df():
        out = logs().sort_values("date", ascending=False)
        return render.DataTable(out, width="500px", height="95%")

    @render.text
    def text_out():
        return f"You wrote {input.txt_in()} at {datetime.now().time()}"


app = App(app_ui, server)
