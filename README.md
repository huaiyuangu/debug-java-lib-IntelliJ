# debug-RobotFramework-In-IntelliJ
how to debug Robotframework test cases with Jython jar file in IDEA Intellij IDE

#### Create Configuration in IntelliJ
```
Path to JAR:        C:\jython2.7.0\jython.jar              (jython jar file in jython installation directory)
VM options :        -Dlog4j.configuration=log4j.properties (not necessary)
Program arguments : debug_robot.py                         (entry file to debug specific test case filtered by tag name)
Working directory : ...\projectPath                        (current project path)
```

#### Copy debug_robot.py file to your project
change source code path in python file


#### Run/Debug configuration in IntelliJ
