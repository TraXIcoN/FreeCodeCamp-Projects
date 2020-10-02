import 'package:flutter/material.dart';
import 'package:audioplayers/audio_cache.dart';

void main(List<String> args) => runApp(XylophoneApp());

class XylophoneApp extends StatelessWidget {
  void changeSound(int SoundNumber)
  {
    final player=AudioCache();
    player.play('note$SoundNumber.wav');
  }
  Expanded colorchange({int number,Color color})
  {
    return(
      Expanded(
            child:FlatButton(
            color: color,
            onPressed: () {
              changeSound(number);
            },
          ),
      )
    );
  }
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        backgroundColor: Colors.black,
        body: SafeArea(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.stretch,
                children: <Widget>[
          colorchange(number:1, color: Colors.red),
          colorchange(number:2, color: Colors.orange),
          colorchange(number:3,color: Colors.yellow),
          colorchange(number:4,color: Colors.green),
          colorchange(number:5,color: Colors.green[800]),
          colorchange(number:6,color: Colors.blue),
          colorchange(number:7,color: Colors.purple),
        ])),
      ),
    );
  }
}
