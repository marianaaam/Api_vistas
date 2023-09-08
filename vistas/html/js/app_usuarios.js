function getUsuarios(hola){
    const resultado = fetch("http://127.0.0.1:5000/usuarios");

    resultado
        .then(responder => responder.json())
        .then(datos => {
            hola(datos);
        });
}

getUsuarios(datos => {
    /*console.log(datos);*//*inspeccionamos la pagina y vemos el arry de objetos*/
    datos.forEach(usuario => {
        let tabla = document.getElementById("datos");
        tabla.innerHTML+=`
        <tr>
            <td>${usuario.id}</td>
            <td>${usuario.nombre_usuario}</td>
            <td>${usuario.contrasena}</td>
        </tr>
        `;
    });
});