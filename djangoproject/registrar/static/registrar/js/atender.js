function agregarElemento() {
    const codigoBarraInput = document.getElementById('codigo_barra');
    const codigoBarra = codigoBarraInput.value;

    if (codigoBarra) {
        const form = document.getElementById('accionNose');
        form.submit();
    }
}

function lecturaCorrecta(codigoTexto, codigoObjeto) {
    document.querySelector('input[name="codigo_barra"]').value = codigoTexto;
    document.getElementById('accionNose').submit();
}

function lecturaError(error) {
    console.warn(`Code scan error = ${error}`);
}

let html5QrcodeScanner = new Html5QrcodeScanner(
    "reader",
    { fps: 10, qrbox: {width: 250, height: 250}, },
    /* verbose= */ false);
html5QrcodeScanner.render(lecturaCorrecta, lecturaError);