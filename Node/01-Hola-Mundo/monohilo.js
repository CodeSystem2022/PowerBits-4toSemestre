
console.log('Hola a todo el grupo de PowerBits')

var i = 0;
setInterval(function() {
    console.log(i);
    i++;
    
    if(i === 5){
        console.log('Forzamos un error');
        var a = 3 + z;
    }
}, 1000);
