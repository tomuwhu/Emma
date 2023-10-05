function f() {
    document.getElementById("x").innerHTML = ''
    n = Number(document.getElementById("i1").value)
    while (n != 1) {
        document.getElementById("x").innerHTML += `<div>${n}</div>`
        n = n % 2 ? 3 * n + 1 : n / 2
    }
    document.getElementById("x").innerHTML += `<div>1</div>`
}
