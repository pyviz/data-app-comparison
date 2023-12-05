from shiny import Inputs, Outputs, Session, App, render, ui, reactive
from pathlib import Path
import pandas as pd


@reactive.file_reader(Path(__file__).parent / "logs.csv")
def logs():
    return pd.read_csv(Path(__file__).parent / "logs.csv")


app_ui = ui.page_fillable(
    ui.card(ui.output_data_frame("df")),
)


def server(input: Inputs, output: Outputs, session: Session):
    @render.data_frame
    def df():
        out = logs().sort_values("date", ascending=False)
        return render.DataTable(out, width="500px", height="95%")


app = App(app_ui, server)
