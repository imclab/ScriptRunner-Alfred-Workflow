# Script Runner

I noticed that I repeatedly write some script, wire it with some keyword or hotkey in Alfred and then forget what it was.

So I created quick workflow that allows you to add scripts to list with **add script** file action and then display and run them with **./** keyword. First word of query is used to filter scripts, you can pass command line arguments after space.

![alfred]

---

At the moment workflow supports python, perl, osascritpt and ruby but new languages can be easily added by adding extension and name of interpreter to extension_interpreter dictionary in scriptsrunner.py.   



[alfred]: http://bvsc.nazwa.pl/img/scriptrunner.png 