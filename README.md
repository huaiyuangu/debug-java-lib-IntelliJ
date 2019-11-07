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
```
# set classpath for jar file libraries
JAVA_LIB = os.path.join(root_path, 'lib')
cp = ''
for lib in os.listdir(JAVA_LIB):
    if lib.endswith(".jar"):
        s = os.path.join(JAVA_LIB, lib)
        cp += s + ':'
        sys.path.append(s)
# build java source code to output
sys.path.append(os.path.join(root_path, 'output'))

```

#### Run/Debug configuration in IntelliJ
