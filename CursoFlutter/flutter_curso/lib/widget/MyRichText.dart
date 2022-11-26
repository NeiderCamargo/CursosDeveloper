// ignore: file_names, unused_import
import 'package:flutter/material.dart';

class MyRichText extends StatelessWidget {
  const MyRichText({super.key});

  @override
  Widget build(BuildContext context) {
    // ignore: prefer_const_constructors
    return RichText(
      text:
          // ignore: prefer_const_constructors
          TextSpan(
              text: "Tienes una cuenta novia? ",
              style: const TextStyle(color: Colors.black, fontSize: 20),
              // ignore: prefer_const_literals_to_create_immutables
              children: [
            // ignore: prefer_const_constructors
            TextSpan(
                text: "Inicia sesión:",
                // ignore: prefer_const_constructors
                style: TextStyle(
                    color: Colors.white,
                    fontWeight: FontWeight.bold,
                    decoration: TextDecoration.underline,
                    fontSize: 20))
          ]),
    );
  }
}
