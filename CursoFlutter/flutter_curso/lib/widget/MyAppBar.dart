// ignore: file_names, unused_import
import 'package:flutter/material.dart';

class MyAppBar extends StatelessWidget implements PreferredSizeWidget {
  const MyAppBar({super.key});

  @override
  Widget build(BuildContext context) {
    // ignore: prefer_const_constructors
    //APPBAR
    return AppBar(
      title: const Text("Inicio"),
      backgroundColor: Colors.pinkAccent,
      elevation: 30,
      shadowColor: Colors.white,
      centerTitle: true,
      toolbarOpacity: 0.5,
      leading: const Icon(
        Icons.arrow_back,
        color: Colors.white,
      ),
      // ignore: prefer_const_literals_to_create_immutables
      actions: [
        //ICONO ALINEADO DE LA PARTE DERECHA
        // ignore: prefer_const_constructors
        Icon(
          Icons.search,
          color: Colors.white,
          size: 30,
        ),
        const Icon(
          Icons.more,
          color: Colors.white,
        ),
      ],
      toolbarHeight: 60, //ALTURA
    );
  }

  @override
  // TODO: implement preferredSize
  Size get preferredSize =>
      const Size.fromHeight(kToolbarHeight); //TAMAÑO DEL APP BAR CONSTANTE
}
