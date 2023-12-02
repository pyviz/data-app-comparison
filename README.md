# Data App Comparison

This repo illustrates some differences between various web application frameworks.
The purpose is to provide minimal, concrete examples of how to accomplish common development tasks in various python web application frameworks, and to use those examples to help people learn their APIs.
The frameworks we have so far are:

-   [Dash](https://plotly.com/dash/)

-   [Panel](https://panel.holoviz.org/reference/index.html)

-   [Shiny](https://shiny.posit.co/)

-   [Streamlit](https://streamlit.io/)

## Running the examples

Navigate to the example folder and install the dependencies in a virtual environment with

``` bash
pip install -r requirements.txt
```

| Framework | Command                |
|-----------|------------------------|
| Dash      | `python app.py`        |
| Panel     | `panel serve app.py`   |
| Streamlit | `streamlit run app.py` |
| Shiny     | `shiny run app.py`     |

# Submitting a new problem

Please raise an issue to discuss and clarify the problem statement, and then submit a pull request with the problem statement in a README file.
Ideally problems should have the following qualities:

-   Problems should be small and clear

-   Successful apps should stand alone and not require external APIs or system setup

-   Problems should focus on the capabilities of the web framework

-   For inspriation see [7guis](https://eugenkiss.github.io/7guis/) or [TodoMVC](https://todomvc.com/)

# Submitting a new solution

We want only one solution per framework, but please submit PRs with either solutions from a new framework, or improvements to an the existing solution.
Your solution should focus on the framework's capabilities, and ideally have fairly few dependencies.
For example it's not a good idea to include a lot of JavaScript code in your Streamlit solution because that will tell the reader more about how to do something in JavaScript than it will about what they can do in Streamlit.
