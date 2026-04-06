//  COLOCAR FOOTER CON BASE A SU UBICACIÓN EN LA PÁGINA   ------------------------
function ubicacionFooter(){
    const elemento = document.querySelector('footer');
    const rect = elemento.getBoundingClientRect();

    let posicionEnPagina =  rect.top + window.scrollY;
    if (posicionEnPagina < 500) {
        elemento.style.position = 'relative';
        elemento.style.top = '213';
    } else {
        // Opcional: restaurar estilos si ya no cumple
        elemento.style.position = '';
        elemento.style.bottom = '';
    }
}

ubicacionFooter()