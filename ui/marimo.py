import marimo

__generated_with = "0.23.6"
app = marimo.App(width="full")


@app.cell
def _():
    import pandas as pd
    df = pd.DataFrame(
        {
            "Name": ["Hydrogen", "Helium", "Lithium"],
            "Type": ["Gas", "Gas", "Metal"],
            "Description": [
                "Lightest element",
                "Noble gas",
                "Alkali metal",
            ],
        }
    )
    return (df,)


@app.cell
def _():
    return


@app.cell
def _(df):
    import marimo as mo
    table = mo.ui.dataframe(df)
    return (table,)


@app.cell
def _(table):
    table
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
