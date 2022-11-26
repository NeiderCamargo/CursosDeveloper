// ignore: file_names, unused_import
import 'package:flutter/material.dart';

class MyButton extends StatelessWidget {
  const MyButton({super.key});

  @override
  Widget build(BuildContext context) {
    // ignore: prefer_const_constructors
    return MyOutLineBotton();
  }

  //METODOS
  myElevetedButton() {
    return ElevatedButton.icon(
      icon: const Icon(
        Icons.menu,
        color: Colors.red,
      ),
      label: const Text("Guardar"),
      style: ElevatedButton.styleFrom(
        // ignore: deprecated_member_use
        primary: Colors.white, //transparent //COLOR DEL BOTON
        // ignore: deprecated_member_use
        onPrimary: Colors.black, //COLOR DEL TEXTO
        shadowColor: Colors.yellow, //transparent //Sombra
        elevation: 20, //spmbra elevada
      ),
      onLongPress: () {
        //Detecta cuando el usuario tarda en presionar el boton
        // ignore: avoid_print
        print("ElevatedButton onLongPress");
      },
      onPressed: () {
        //Al presionar el boton se ejecuta
        // ignore: avoid_print
        print("ElevatedButton");
      },
      //child: const Text("Guardar"),
    );
  }

  //BOTON TRANSPARENTE
  myTextButton() {
    return TextButton(
        onPressed: () {
          // ignore: avoid_print
          print("TextButton");
        },
        child: const Text("Guardar"));
  }

  //BOTON CON BORDE
  // ignore: non_constant_identifier_names
  MyOutLineBotton() {
    return OutlinedButton(
        style: OutlinedButton.styleFrom(
            side: const BorderSide(color: Colors.yellow, width: 10),
            // ignore: deprecated_member_use
            primary: Colors.white, //COLOR DEL TEXTO
            // ignore: prefer_const_constructors
            shape: RoundedRectangleBorder(
                borderRadius: const BorderRadius.all(Radius.circular(30)))),
        onPressed: () {
          // ignore: avoid_print
          print("TextButton");
        },
        child: const Text("Guardar"));
  }
}
