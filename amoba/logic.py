from browser import document as D, html as H
next = "X"
def f(e):
    global next
    e.target <= H.SPAN(next)
    if next == "X":
        next = "O"
        e.target.style.backgroundColor="red"
    else:
        next = "X"
        e.target.style.backgroundColor="green"
D <= H.H1("Amőba")
D <= H.TABLE(H.TR(H.TD(" ").bind("click", f) for j in range(1, 21)) for i in range(1, 21))