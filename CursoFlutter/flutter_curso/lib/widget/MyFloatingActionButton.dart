// ignore: file_names, unused_import
import 'package:flutter/material.dart';

class MyFloatingActionButton extends StatelessWidget {
  const MyFloatingActionButton({super.key, required Null Function() onPressed});

  @override
  Widget build(BuildContext context) {
    // ignore: prefer_const_constructors
    return FloatingActionButton.extended(
      //BOTON EXTENDIBLE
      onPressed: () {
        // ignore: avoid_print
        print("FloatingActionButton");
      },
      // ignore: sort_child_properties_last
      icon: const Icon(
        Icons.add,
        size: 40,
        color: Colors.black,
      ),
      label: const Text(
        "Agregar Usuario",
        style: TextStyle(color: Colors.black),
      ),
      backgroundColor: Colors.yellow,
      elevation: 20,
      tooltip: "Agregar Usuario",
    );
  }
}
