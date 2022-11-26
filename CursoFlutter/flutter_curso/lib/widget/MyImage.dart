// ignore: file_names, unused_import
import 'package:flutter/material.dart';

class MyImage extends StatelessWidget {
  const MyImage({super.key});

  @override
  Widget build(BuildContext context) {
    // ignore: prefer_const_constructors
    return Image(
      image: const AssetImage("assets/image/Cody.jpeg"),
      width: 50,
      height: 200,
      fit: BoxFit.fill, //Agrandar el contenedor de la imagen
      //cover //aplica el tañño mas grande de la imagen
      //ScaleDown  // se adapata a la imagen mas pequeña dependiendo de heigth
      //fitwidth // la iamagen toma el valor de heidght
      //fill //Tomar el ancho de la imagen
      color: Colors.white, //color blanco a la imagen, solo png

      //MENSAJE PARA MOSTRAR SI NO MUESTRA LA IMAGEN
      errorBuilder:
          (BuildContext context, Object error, StackTrace? stracTrace) {
        return const Text("Error al cargar la imagen");
        //PONER IMAGEN POR DEFECTO
        // ignore: dead_code
        return Image.asset("assets/image/Cody.jpeg");
      },
    );
  }
}
