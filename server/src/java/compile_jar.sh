#!/bin/bash
#Compile and create jar from java files

javac *.java
jar cf ../jar/symbolicPerseusIR.jar *.class
