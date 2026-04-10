//                            SLIDER                         -----------------------------
const imagenes = document.querySelectorAll("#slider img")
let imagenTamaño = document.querySelector("#slider img").width
document.querySelector("#slider").style.Width = imagenTamaño-3  

const imagen1 = imagenes[0];
const imagen2 = imagenes[1];
const imagen3 = imagenes[2];
const imagen4 = imagenes[3];
const imagen5 = imagenes[4];

let movimiento1 = 0;
let movimiento2 = 0;
let movimiento3 = 0;
let movimiento4 = 0;
let movimiento5 = 0;
let intervalo;

function iniciarMovimiento() {
    intervalo = setInterval(() => {
        movimiento1 +=5
        movimiento2 +=5
        movimiento3 +=5
        movimiento4 +=5
        movimiento5 +=5
        imagen1.style.right = movimiento1;
        imagen2.style.right = movimiento2;
        imagen3.style.right = movimiento3;
        imagen4.style.right = movimiento4;
        imagen5.style.right = movimiento5;

        // Si llegó a un múltiplo de 800 (800, 1600, 2400, etc.)
        if (movimiento1 % imagenTamaño === 0) {
            if(movimiento1 === imagenTamaño){
                movimiento1=-imagenTamaño*4
            }
            if(movimiento2 === imagenTamaño*2){
                movimiento2=-imagenTamaño*3
            }
            if(movimiento3 === imagenTamaño*3){
                movimiento3=-imagenTamaño*2
            }
            if(movimiento4 === imagenTamaño*4){
                movimiento4=-imagenTamaño*1
            }
            if(movimiento5 === imagenTamaño*5){
                movimiento5=-imagenTamaño*0
            }
            clearInterval(intervalo); // detener movimiento
            // Pausar 3 segundos y continuar
            setTimeout(() => {
                iniciarMovimiento();
            }, 3000);
        }
    }, 1);
}

// Iniciar después de 3 segundos
setTimeout(() => {
    iniciarMovimiento();
}, 3000);