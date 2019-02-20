#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import inspect
from robot.run import RobotFramework


root_path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
sys.path.append(root_path)


__author__ = 'huaiyuan.gu@gmail.com'

"""
debug java libraries called from robot test case
"""


if __name__ == '__main__':

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

    base_path = os.path.realpath(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))
    test_path = os.path.join(base_path, "testcases/idmInterop")
    report_path = os.path.join(base_path, "TestResult")

    root = base_path
    rb = os.path.join(test_path, 'mytestcases.robot')

    xmlfile = os.path.join(report_path, 'output.xml')
    logfile = os.path.join(report_path, 'log.html')
    rptfile = os.path.join(report_path, 'report.html')

    bot = RobotFramework()
    bot.main([rb], outputdir=report_path, output=xmlfile, log=None, report=None, include=['debug'],
             # if you have global variables to export to java codes
             variablefile=[os.path.join(root_path, 'variableFile.py')])

    from robot.rebot import Rebot
    bot = Rebot()
    try:
        # put tag debug on test case you want to debug
        bot.main([xmlfile], log=logfile, report=rptfile, include=['debug'])
    except Exception as e:
        print ('=' * 10 + ' Robot report exception %s' % '=' * 10)
        print (e)
