在Python中，一个.py文件就称之为一个模块（Module）。
使用模块还可以避免函数名和变量名冲突。相同名字的函数和变量完全可以分别存在不同的模块中，因此，我们自己在编写模块时，不必考虑名字会与其他模块冲突。但是也要注意，尽量不要与内置函数名字冲突。
你也许还想到，如果不同的人编写的模块名相同怎么办？为了避免模块名冲突，Python又引入了按目录来组织模块的方法，称为包（Package）。
现在，假设我们的abc和xyz这两个模块名字与其他模块冲突了，于是我们可以通过包来组织模块，避免冲突。方法是选择一个顶层包名，比如mycompany
引入了包以后，只要顶层的包名不与别人冲突，那所有模块都不会与别人冲突。现在，abc.py模块的名字就变成了mycompany.abc，类似的，xyz.py的模块名变成了mycompany.xyz。
请注意，每一个包目录下面都会有一个__init__.py的文件，这个文件是必须存在的，否则，Python就把这个目录当成普通目录，而不是一个包。__init__.py可以是空文件，也可以有Python代码，因为__init__.py本身就是一个模块，而它的模块名就是mycompany。
类似的，可以有多级目录，组成多级层次的包结构
自己创建模块时要注意命名，不能和Python自带的模块名称冲突。
例如，系统自带了sys模块，自己的模块就不可命名为sys.py，否则将无法导入系统自带的sys模块。

在Python中，安装第三方模块，是通过包管理工具pip完成的。
注意：Mac或Linux上有可能并存Python 3.x和Python 2.x，因此对应的pip命令是pip3。

Python Imaging Library，这是Python下非常强大的处理图像的工具库。
一般来说，第三方库都会在Python官方的pypi.python.org网站注册，要安装一个第三方库，必须先知道该库的名称，可以在官网或者pypi上搜索，比如Pillow的名称叫Pillow，因此，安装Pillow的命令就是：
pip install Pillow
You are using pip version 8.1.1, however version 9.0.1 is available.
You should consider upgrading via the 'python -m pip install --upgrade pip' command.

其他常用的第三方库还有MySQL的驱动：mysql-connector-python，用于科学计算的NumPy库：numpy，用于生成文本的模板工具Jinja2，等等。

模块搜索路径
当我们试图加载一个模块时，Python会在指定的路径下搜索对应的.py文件，如果找不到，就会报错
默认情况下，Python解释器会搜索当前目录、所有已安装的内置模块和第三方模块，搜索路径存放在sys模块的path变量中：
>>>import sys
>>>sys.path
['', 'C:\\Users\\Peter\\AppData\\Local\\Programs\\Python\\Python35\\python35.zip', 'C:\\Users\\Pe
ter\\AppData\\Local\\Programs\\Python\\Python35\\DLLs', 'C:\\Users\\Peter\\AppData\\Local\\Progra
ms\\Python\\Python35\\lib', 'C:\\Users\\Peter\\AppData\\Local\\Programs\\Python\\Python35', 'C:\\
Users\\Peter\\AppData\\Local\\Programs\\Python\\Python35\\lib\\site-packages']

如果我们要添加自己的搜索目录，有两种方法：
一是直接修改sys.path，添加要搜索的目录
>>>sys.path.append('/Users/michael/my_py_scripts')
这种方法是在运行时修改，运行结束后失效。

第二种方法是设置环境变量PYTHONPATH，该环境变量的内容会被自动添加到模块搜索路径中。设置方式与设置Path环境变量类似。注意只需要添加你自己的搜索路径，Python自己本身的搜索路径不受影响。

