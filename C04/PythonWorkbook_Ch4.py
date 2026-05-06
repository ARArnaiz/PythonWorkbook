import marimo

__generated_with = "0.23.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #Chapter 4: List and Tuples
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Exercise 9: First-last
    """)
    return


@app.cell
def _():
    astring = 'abcdefghijklmnopqrstuvwxyz'
    alist = [1,2,3,4,5,6,7,8,9,0]
    atuple = (0,2,4,6,8,10,"x","y","z")
    adict = {}

    def first_last(seq: str | list | tuple) -> str | list| tuple:
        newstr = ""
        newlst = []
        newtuple = ()
        if isinstance(seq, str):
            newstr = f'{seq[0]}{seq[-1]}'
            return newstr
        elif isinstance(seq, list):
            newlst.append(seq[0])
            newlst.append(seq[-1])
            return newlst
        elif isinstance(seq, tuple): 
            newtuple = seq[0], seq[-1]
            return newtuple
        else:
            return 'None'

    print(first_last(astring))
    print(first_last(alist))
    print(first_last(atuple))
    return alist, astring, atuple


@app.cell
def _(alist, astring, atuple):
    # Lerner's - slices preserve type
    def fl(sequence):
        return sequence[:1] + sequence[-1:]

    print(fl(astring))
    print(fl(alist))
    print(fl(atuple))
    return


if __name__ == "__main__":
    app.run()
