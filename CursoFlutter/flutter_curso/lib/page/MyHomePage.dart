import 'package:flutter/material.dart';
import 'package:flutter_curso/widget/MyButton.dart';
import 'package:flutter_curso/widget/MyImage.dart';

import '../widget/MyAppBar.dart';
import '../widget/MyFloatingActionButton.dart';
import '../widget/MyIcon.dart';
import '../widget/MyRichText.dart';
import '../widget/MyImage.dart';

class MyHomePage extends StatefulWidget {
  //WIDGET DE TIPO ESTADO
  const MyHomePage({super.key, required this.title});

  final String title;

  @override
  State<MyHomePage> createState() =>
      _MyHomePageState(); //Crear la vista y se llama cuando se hace una actualización
}

class _MyHomePageState extends State<MyHomePage> {
  //SE LLAMA EL WIDGET Y SE LE DA EL TIPO
  int _counter = 0;

  void _incrementCounter() {
    setState(() {
      //NOS AYUDA A ACTUALIZAR EL DISEÑO
      _counter++;
    });
  }

  @override
  Widget build(BuildContext context) {
    //cONSTRUCTOR DL DISEÑO HOMEPAGE

    // ignore: prefer_const_constructors
    return Scaffold(
        backgroundColor: Colors.pink,
        //SE RETORNA EL DISEÑO
        floatingActionButton: MyFloatingActionButton(
          //mostrar boton
          onPressed: () {},
        ),
        floatingActionButtonLocation:
            FloatingActionButtonLocation.centerDocked, //boton al centro
        appBar: const MyAppBar(),

        //CORTAR APPBAR

        // ignore: prefer_const_constructors
        body: SafeArea(
          //Acomodar el diseño
          //child: const MyText(), //Llamamos el widget "text"
          //child: const MyRichText(),
          //child: const MyIcon()
          //child: const MyImage(),
          child: const MyButton(),
        ));
  }
}
