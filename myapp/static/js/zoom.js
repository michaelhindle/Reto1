var tamanio = 1;

function masZoom(){
    tamanio += 0.1;
    document.body.style.fontSize = tamanio + "em";
}

function menosZoom(){
    tamanio -= 0.1;
    document.body.style.fontSize = tamanio + "em";
}