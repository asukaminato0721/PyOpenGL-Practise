# PyOpenGL-Practise

---

## 起因

这学期学了计算机图形学，结果教材写得无比佶屈聱牙。老师给的工具是 C++ 的 GLUT，98 年停止更新。就抱着试试的心态搜了下 PyOpenGL pdf，发现了这本书。

书里的代码是 Python2.x 的，经过简单修改就可以在 3.x 运行了。里面的 `glFlush()` 函数最好移到循环外面，可以有效提高渲染速度。 

---

## 运行书里代码需要

1. 安装 PyOpenGL 库
2. 安装 numpy 库

其中 PyOpenGL 库有注意事项。

> 报错：OpenGL.error.NullFunctionError: Attempt to call an undefined function glutInit, check for bool(glutInit) before calling
>
> 原因：貌似是只有 64bit 系统会有这个问题
>
> 方法：下载 64bit 的 PyOpenGL 安装包（原来是 pip install 自动安装的版本不对）
>
> 下载地址：（选择适合自己的版本）http://www.lfd.uci.edu/~gohlke/pythonlibs/#pyopengl
> 下载下来的 whl 文件，用 pip install file_name.whl 进行安装后，问题解决。
>
>（如果有需要，还可以将 PyOpenGL_accelerate 也安装了）
>
> 参考：http://www.cnblogs.com/gamesun/p/5837142.html

> https://hansimov.github.io/#PyOpenGL%20%E7%9A%84%E5%87%A0%E4%B8%AA%E9%97%AE%E9%A2%98

由于时间有限，没有把书里的代码全敲一遍，只能看到有用的就练练手了。

---

### 使用体验

Python 的实践体验简直起飞，和 C++ 不是一个级别的。而且基本不需要配置环境。

这书写得很循循善诱，就是扔个程序，然后说：亲，千万别怕，我慢慢解释给你看。一句句拆开来解释。

里面会有：那 ![](http://latex.codecogs.com/svg.latex?a) 改成 ![](http://latex.codecogs.com/svg.latex?b) 会怎么样？这个会在练习题里遇到。练习题也是很友善，说，我们会画 ![](http://latex.codecogs.com/svg.latex?\sin(x)) 了，那试试画 ![](http://latex.codecogs.com/svg.latex?\sin(3x))，画 ![](http://latex.codecogs.com/svg.latex?\cos(x))，试试怎么画多个函数


---

### 写在最后

1. 关于标题栏怎么打中文：

    https://stackoverflow.com/questions/62264357/how-to-make-pyopengls-title-show-chinese/62372487#62372487

    ```Python
    glutCreateWindow("一二三四".encode("gb2312"))
    ```

2. 右键菜单怎么显示中文

    > 别问，问就是不知道

3. 重点篇目

    1. 第一章,熟悉 `glVertex2f()` 的使用方法
    2. 倒数几章，熟悉右键菜单怎么写（或者直接修改源程序）
    3. 第x章，会提供后续使用的模板
