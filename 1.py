Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # hello.py
... print("Hello World")
Hello World
>>> "I ate %d apples. So I was sick for %s days." %(10, "three")
... "%10s" % "hi"
... "%-10s" %"hi"
... "%-10sjane" %"hi"
... "%0.4f" %3.42134234
... "%10.4f" % 3.123456543
SyntaxError: multiple statements found while compiling a single statement
>>> "I ate %d apples. So I was sick for %s days." %(10, "three")
'I ate 10 apples. So I was sick for three days.'
>>> "%10s" % "hi"
'        hi'
>>> "%-10s" %"hi"
'hi        '
>>> "%-10sjane" %"hi"
'hi        jane'
>>> "%0.4f" %3.42134234
'3.4213'
>>> "%10.4f" % 3.123456543
'    3.1235'
