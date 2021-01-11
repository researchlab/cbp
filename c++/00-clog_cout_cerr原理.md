
> 原文出处: https://www.cnblogs.com/xiezhw3/p/4349766.html

clog：控制输出，使其输出到一个缓冲区，这个缓冲区关联着定义在 <cstdio> 的 stderr。

cerr：强制输出刷新，没有缓冲区。

cout：控制输出，使其输出到一个缓冲区，这个缓冲区关联着定义在 <ostream> 的 stdout。

但是我们分别测试如下三个程序的结果如下：

cout：

```c++
#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{
    cout << "ERROR!!";
    while (true);
    return 0;
}
```
输出结果为：
```
$ ./a.out

```
可以理解，因为 cout 输出是有缓冲区的，这里没有输出说明缓冲区还没有刷新。

cerr：
```c++
#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{
    cerr << "ERROR!!";
    while (true);
    return 0;
}
```
输出：
```
$./a.out
ERROR!!
```

可以理解，因为 cerr 没有输出缓冲区，是强制刷新的，所以在循环之前就已经刷新了，所以会打印结果。

clog：
```c++
#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{
    clog << "ERROR!!";
    while (true);
    return 0;
}
```
输出：
```
$./a.out
ERROR!!
```

这个比较奇怪，不是说 clog 是由缓冲区的嘛，为什么它不是像 cout 一样的输出呢？先看下面部分：

对于cout，clog，cerr输出的机制，c跟c++的标准做法是：
```
stderr : 预设没有分配 buffer
stdout ：预设有分配 buffer
cout ：用 stdout 的buffer
clog ：用 stderr 的 buffer
cerr ：用 stderr 的buffer，强制清空 buffer
```
其中，stderr 的 buffer 预设为没有，所以 clog 和 cerr 都是直接在屏幕输出而没有在缓冲区驻留。所以前面 clog 的输出结果也就可以理解了，因为缓冲区是空的，那么输出就不会在缓冲区驻留了。

下面来说说 cout，clog，cerr 的输出顺序，也可作为 clog 一个更深入的理解。

先看下面一段代码：
```c++
#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{
    setbuf(stderr,0);
    cout << "123";
    clog << "456";
    cerr << "789";

    return 0;
}
```
它的输出结果是：
```
　　456123789
```
上面代码中，setbuf 为 0，也就是设置 stderr 的缓冲区为 0，因为 stderr 的值是有可能因为编译器的不同而不同的，前面说的 c++ 机制只是标准机制，编译器实现商可以进行自己的改变的。

现在来理解一下输出的结果，首先 clog 的输出在最前面很容易理解，但是为什么 cout 的输出在 cerr 的前面呢，因为cerr 的输出关联到了 cout，也即 cerr.tie()=&cout，所以当 cerr 要清空时，会先清空前面的 cout 的缓冲区。[注意只是 cerr 前面的 cout ]

看另一段代码：
```c++
#include <iostream>

using namespace std;

char buf[10];
int main(int argc, char const *argv[])
{
    setbuf(stderr,buf);
    cout << "123";
    clog << "456";
    cerr << "789";

    return 0;
}
```
此时的输出是：
```
123456789
```
在这里给 stderr 的缓冲区设为了 buf，不再是 0 了，所以这里输出结果按顺序输出。

下面取消 cerr 和 cout 的关联：
```c++
#include <iostream>

using namespace std;

char buf[10];
int main(int argc, char const *argv[])
{
    cerr.tie(0);
    setbuf(stderr, buf);
    cout << "123";
    clog << "456";
    cerr << "789";

    return 0;
}
```
输出结果为：
```
456789123
```
这里 clog 在 cout 前面输出，因为 cerr 输出的时候强制刷新了 stderr 缓冲区。

cerr 和 clog 位置调换，结果为：
```c++
#include <iostream>

using namespace std;

char buf[10];
int main(int argc, char const *argv[])
{
    cerr.tie(0);
    setbuf(stderr, buf);
    cout << "123";
    cerr << "789";
    clog << "456";

    return 0;
}
```
输出结果：
```
　789123456
```
此时 cerr 最先输出，因为强制刷新，而 clog 因为缓冲区不为空，所以会在程序结束的时候执行 flush。

再来说说 clog 和 cerr 的重定向问题。

直接对 cerr 和 clog 的输出使用重定向符 > 是无效的，这两个的输出一定会打印在终端上，但是如果一定要进行重定向，那么可以用  rdbuf 函数，如下：
```c++
ofstream ofs("logfile");
clog.rdbuf(ofs.rdbuf());
clog << "Goes to file." << endl;
```

以上测试结果都是在mac g++4.2.1 测试的结果，输出结果在mac的终端。在windows下面测试的结果可能不同。 

具体的区别可以参考如下内容：【以下内容来源：http://tieba.baidu.com/p/937433213 】

1.该物件所用的stream是否按照规定分配buffer
全缓冲:buffer满了才执行fflush()
行缓冲:buffer满了or碰到换行字元才执行fflush()
无缓冲:不管buffer有没有满都执行fflush()


console下
||标准|windows|linux|
|---|---|---|---|
stdout| 行/无缓冲|全缓冲   |行缓冲    |
stderr| 行/无缓冲|全缓冲   |无缓冲    |

非console
||标准|windows|linux|
|---|---|---|---|
stdout|  全缓冲    |全缓冲   |全缓充    |
stderr|  行/无缓冲|全缓冲   |无缓冲    |

以上是预设值，有一点要厘清，全/行/无缓冲只是该stream的特性，
与它有没有buffer并没有关系，拿windows来说，
乍看之下会等到buffer满才输出，但实际上是直接输出，
因为没有分配buffer，你也可以对无缓冲的stream分配buffer，
虽然一样直接跑fflush()就是了

如果要分配buffer给stream，可以用setbuf()和setvbuf()，
用前者时要注意，一但用它分配buffer后，行缓冲的特性会消失，
且buffer不能是局部变量，因为最后一次fflush()是在exit()里执行
那时局部变量已经被释放


2.该物件是否按照规定设置ios::unitbuf
如果有设ios::unitbuf，就直接执行fflush()，
即使底下stream设成全缓冲跟分配buffer也一样，
除非手动设定，否则只有cerr才有设ios::unitbuf

如果要修改物件的ios::unitbuf，可用setf()或unsetf()设定


3.该物件的是否按照规定绑定别的物件

||标准|windows|linux|
|---|---|---|---|
clog.tie()| null |&cout|   null |
cerr.tie()|&cout|&cout|  &cout|
cout.tie()|null  | null  |    null |

如果有绑别的物件，当自己准备要跑fflush()时，
会先让被绑定的物件执行fflush()，然后才换自己跑fflush()

如果要修改绑定的物件，就用tie()来设，传0代表不绑定

虽然下列网站写cin、cerr、clog都绑定cout, 
http://www.cplusplus.com/reference/iostream/ios/tie/
但是C++的规格书上，其实没规定clog要绑cout

4.换行字元跟endl
前者只能让行缓冲的物件跑fflush()，
后者则强迫cout、cerr、clog跑fflush()

5.如果一直到main()结束都没有跑fflush()
那么stdout会先输出，接著才是stderr

7.main()结束后，不可再用cout、cerr、clog来输出
首先来看exit()的标准流程

A.摧毁thread物件
B.摧毁global物件/摧毁函式里的static物件/执行atexit注册函式
C.让所有的C stream执行fflush()，接著关闭它们
D.砍掉暂存档
E.归还控制权给OS


在执行dtor/atexit注册函式时，无法保证cout、cerr、clog这些物件还在

总结：
没分配buffer、无缓冲、ios::unitbuf!=0、buffer已满、行缓冲碰到'\n'、endl
以上只要有一个成立就会跑fflush()