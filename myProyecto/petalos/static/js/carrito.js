window.onload = function () {
    // Variables
    let baseDeDatos = [
        {
            id: 1,
            Imagen:'https://i.pinimg.com/originals/f2/b9/5d/f2b95d42f229006ed804a1a18ea5ae9b.jpg',
            nombre: 'flores hombres tula',
            precio: 3000,
            descripcion:'flores hermosas que tienen forma de hombre desnudo',
            estado:true,
            Stock:34
        },
        {
            id: 2,
            Imagen:'https://media.istockphoto.com/photos/purple-flower-close-up-picture-id525320311?k=6&m=525320311&s=612x612&w=0&h=aa3kOBrAiJASuMxhxvXx6gL5wO_SH0ogxSy6ftS1myU=',
            nombre: 'flor de labios',
            precio: 2500,
            descripcion:'curiosa florde atractivo masculino',
            estado:true,
            Stock:15
        }
    
    ]
    let $items = document.querySelector('#items');
    let carrito = [];
    let total = 0;
    let $carrito = document.querySelector('#carrito');
    let $total = document.querySelector('#total');
    // Funciones
    function renderItems() {
        for (let info of baseDeDatos) {
            // Estructura
            let miNodo = document.createElement('div');
            miNodo.classList.add('card', 'col-sm-4');
            // Body
            let miNodoCardBody = document.createElement('div');
            miNodoCardBody.classList.add('card-body');
            // Titulo
            let miNodoTitle = document.createElement('h5');
            miNodoTitle.classList.add('card-title');
            miNodoTitle.textContent = info['nombre'];
            // Imagen 
            let miNodoImg = document.createElement('img');
            miNodoImg.classList.add('card-img');
            miNodoImg.setAttribute("src", miNodoImg.imgContent = info['Imagen']);//las comillas si nada es porque puse solo url en vez de que busque un archivo interno
            // Descripcion
            let miNodoDescripcion = document.createElement('p');
            miNodoDescripcion.classList.add('card-text');
            miNodoDescripcion.textContent = info['descripcion'];
            // Precio
            let miNodoPrecio = document.createElement('p');
            miNodoPrecio.classList.add('card-text');
            miNodoPrecio.textContent = '$' + info['precio'];
            // Stock
            let miNodoStock = document.createElement('p');
            miNodoStock.classList.add('card-text');
            miNodoStock.textContent = 'Stock en bodega: ' + info['Stock'];
            // Boton 
            let miNodoBoton = document.createElement('button');
            miNodoBoton.classList.add('btn', 'btn-danger');
            miNodoBoton.textContent = 'Agregar';
            miNodoBoton.setAttribute('marcador', info['id']);
            miNodoBoton.addEventListener('click', anyadirCarrito);
            // Insertamos
            miNodoCardBody.appendChild(miNodoTitle);//
            miNodoCardBody.appendChild(miNodoImg);//
            miNodoCardBody.appendChild(miNodoDescripcion);//
            miNodoCardBody.appendChild(miNodoPrecio);//
            miNodoCardBody.appendChild(miNodoStock);//
            miNodoCardBody.appendChild(miNodoBoton);
            miNodo.appendChild(miNodoCardBody);
            $items.appendChild(miNodo);
        }
    }
    function anyadirCarrito() {
        // Anyadimos el Nodo a nuestro carrito
        carrito.push(this.getAttribute('marcador'))
        // Calculo el total
        calcularTotal();
        // Renderizamos el carrito 
        renderizarCarrito();  
    }
    
    function renderizarCarrito() {
        // Vaciamos todo el html
        $carrito.textContent = '';
        // Generamos los Nodos a partir de carrito
        carrito.forEach(function (item, indice) {
            // Obtenemos el item que necesitamos de la variable base de datos
            let miItem = baseDeDatos.filter(function (itemBaseDatos) {
                return itemBaseDatos['id'] == item;
            });
            // Creamos el nodo del item del carrito
            let miNodo = document.createElement('li');
            miNodo.classList.add('list-group-item', 'text-right');
            miNodo.textContent = `${miItem[0]['nombre']} : $ ${miItem[0]['precio']}`;
            // Boton de borrar
            let miBoton = document.createElement('button');
            miBoton.classList.add('btn', 'btn-danger', 'mx-5');
            miBoton.textContent = 'X';
            miBoton.setAttribute('posicion', indice);
            miBoton.addEventListener('click', borrarItemCarrito);
            // Mezclamos nodos
            miNodo.appendChild(miBoton);
            $carrito.appendChild(miNodo);
        })
    }
    
    function borrarItemCarrito() {
        // Obtenemos la posicion que hay en el boton pulsado
        let posicion = this.getAttribute('posicion');
        // Borramos la posicion que nos interesa
        carrito.splice(posicion, 1);
        // volvemos a renderizar
        renderizarCarrito();
        // Calculamos de nuevo el precio
        calcularTotal();
    }
    
    function calcularTotal() {
        // Limpiamos precio anterior
        total = 0;
        // Recorremos el array del carrito
        for (let item of carrito) {
            // De cada elemento obtenemos su precio
            let miItem = baseDeDatos.filter(function (itemBaseDatos) {
                return itemBaseDatos['id'] == item;
            });
            total = total + miItem[0]['precio'];
        }
        // Formateamos el total para que solo tenga dos decimales
        let totalDosDecimales = total.toFixed(0);
        // Renderizamos el precio en el HTML
        $total.textContent = totalDosDecimales;
    }
    // Eventos
    
    // Inicio
    renderItems();
    }