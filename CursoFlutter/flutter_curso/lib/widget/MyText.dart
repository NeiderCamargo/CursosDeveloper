// ignore: file_names, unused_import
import 'package:flutter/material.dart';

class MyText extends StatelessWidget {
  const MyText({super.key});

  @override
  Widget build(BuildContext context) {
    // ignore: prefer_const_constructors
    return Text(
      //Creamos el widget text
      "Hola Mundo !!",
      //ATRIBUTOS DE TEXTO
      // ignore: prefer_const_constructors
      style: TextStyle(
          color: Colors.white,
          fontSize: 40,
          fontWeight: FontWeight.bold,
          letterSpacing: 5, //Espacio entre letras
          wordSpacing: 20, //Espacio entre palabras
          backgroundColor: Colors.black12,
          fontFamily: "Montserrat",
          decoration: TextDecoration.underline //Subrayar texto
          ),

      //ALINEAR TEXTO
      textAlign: TextAlign.justify,
      softWrap: true, //TEXTO EN UNA SOLA LINEA
      maxLines: 3, //Numero de lineas del texto
      overflow:
          TextOverflow.ellipsis, //agregar puntos supensivos si hay mas texto
    );
  }
}
