# ImportError: attempted relative import with no known parent package

# 相对导入通过使用模块的 __name__ 属性来确定模块在包层次结构中的位置。
# 如果该模块的名称不包含任何包信息（例如，它被设置为 __main__ ），
# 那么相对引用会认为这个模块就是顶级模块，而不管模块在文件系统上的实际位置。

# 我们通过在其中创建一个新的空 __init__.py 文件来将项目目录转换为一个包。就是本文件的作用

# 我们在项目目录的父目录中创建一个主文件 main.py (09.blueprint.py)

# 在主文件 main.py (09.blueprint.py)中导入 import blueprints.test_ping as ping
# 会设置相对引用的包信息（ __name__ 和 __package__ 变量）。
# 现在，python解释器可以成功解析 blueprint\test_ping\views.py 相对引用了。

