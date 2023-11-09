// this === global = true

//Mostrar algo en consola
//console.log();

//Mostrar un mensaje en forma de error
//console.error();

//Ejecutar un código despues de un intervalo de tiempo
//setTimeout(() => {});

//Ejecutar un código cada intervalo de tiempo
//setInterval(() => {});

//Da prioridad de ejecución a una funcion asincronica
//setImmdiate(() => {});

//console.log(setInterval)

let i = 0;
let intervalo = setInterval(() => {
    console.log('Hola');
    if (i === 3) {
        clearInterval(intervalo); //Detenemos la función
    }
    i++;
}, 1000); 

setImmediate(() => {
    console.log('Saludo inmediato')
});

//requiere();

console.log(__filename);

global.miVariable = 'mi variable global';
console.log(miVariable);