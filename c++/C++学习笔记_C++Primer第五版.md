> 主要参考资料为[C++ Primer 中文版（第 5 版）](https://book.douban.com/subject/25708312/);

> 环境为: centos7.6、gcc-7.5.0、g++7.5.0、gdb-10.1、vscode(remote-containers) (https://github.com/researchlab/dbp/tree/master/c%2B%2B)

# 第一章 开始

### 1. hello word

```
#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{
    cout << "Hello World!";
    
    return 0;
}
```

保存为hello.cc, 编译运行
```
g++ hello.cc -o hello
./hello
```

- c++常见的后缀名: .cc、.cxx、.cpp、.cp、.C
- main返回值必须为int

### 2.打印乘法法
```
#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{
    cout << "input a number:" << endl;
    int v1 = 0;
    cin >> v1;         // 接收输入的数字

    /*
       块注释,以下是实现乘法法的代码
    */
    for (int i = 1; i <= v1; i++)
    {
        for (int j = 1; j <= i; j++)
        {
            cout << j << "*" << i << "=" << j*i << " ";
        }
        cout << endl;
        
    }
}
```

- iostream库包含两个基础类型istream和ostream，分别表示输入流和输出流
- 标准库定义了四个IO对象：cin(标准输入)，cout(标准输出)，cerr(标准错误),clog
- cout<<"hello", cin>>v1 类似于shell中的重写向。
- endl的效果是结束当前行，并刷新与设备关联的缓冲区；
- 定义了`using namespace std`,可以直接用 `cout` 而不用 `std::cout`

# 第二章 变量和基本类型

### 1. 数据类型

| 类型 | 含义 | 最小尺寸|
|---|---|---|
| `bool` | 布尔类型  | 8bits |
| `char`| 字符 | 8bits |
| `wchar_t` | 宽字符 | 16bits |
| `char16_t` | Unicode字符 | 16bits |
| `char32_t` | Unicode字符 | 32bits |
| `short` | 短整型 | 16bits |
| `int` | 整型 | 16bits (在32位机器中是32bits) |
| `long` | 长整型 | 32bits |
| `long long` | 长整型 | 64bits （是在C++11中新定义的） |
| `float` | 单精度浮点数 | 6位有效数字 |
| `double` | 双精度浮点数 | 10位有效数字 |
| `long double` | 扩展精度浮点数 | 10位有效数字 |

- short为半字机器字长，int为一个机器字长，而long为二个机器字长
- 对于要用浮点数的情况，几乎总是用double​
- 除去布尔类型和扩展的字符类型之外，其它类型可以划分为带符号的(signed)和无符号的(unsigned)两种；无符号仅能表示大于0的值。

### 2. 类型转换

- 显式转换
  ```c++
  double a = 1.02
  int i = (int)a
  ```
- 隐式转换
    ```c++
    10 / 1.0     //10会转成double类型
    ```

- 非布尔型赋给布尔型，初始值为0则结果为false，否则为true。
- 布尔型赋给非布尔型，初始值为false结果为0，初始值为true结果为1。
- 赋给无符号类型超过表示范围的值，结果是初值对无符号类型表示数值的总个数(比如8位无符号数为256)取余，超过表示范围的值包括负数
- 赋给有符号类型超过表示范围的值，结果是未定义的
- 切勿混用带符号类型和无符号类型

### 3. 字面值常量

- 以0开头表达是8进制，而以0x开头则表示是16进制。
- 字面值后面可以加L和U分别表示是long类型和unsigned类型
- 字符字面值：单引号， 'a'
- 字符串字面值：双引号， "Hello World""
- 布尔字面值。true，false。
- 指针字面值。nullptr

### 4. 变量定义

```c++
int a = 0;
double b;
```

- 初始化不是赋值
- 初始化(initialized):当对象在创建时获得了一个特定的值
- 赋值 = 擦除对象的当前值 + 用新值代替
- 列表初始化：使用花括号{}，如int units_sold{0};
- 定义时没有指定初始值会被默认初始化

### 5. 声明和定义

```c++
extern int i;  // 声明
int j;         // 定义j
```
- 声明规定了变量的类型和名字，定义还申请存储空间，也可能为变量赋初始值
- 变量能且只能被定义一次，但是可以被声明多次

### 6. 变量命名

- 变量名小写，中间可以用下划线，比如student_loan
- 自定义的类名一般以大写字母开头
  
### 7.变量作用域

- 作用域以花括号分隔

### 8. 复合类型-引用

```c++
int ival = 1024;
int &refVal = ival;       // refValu指向ival
```
- 引用仅仅只是对象的别名
- 引用必须初始化,且不可修改

### 9. 复合类型-指针

```c++
int ival = 42;
int *p = &ival   // &取地址， int *p声明一个整形的指针p
int *k = nullptr;   // nullptr表示空指针

```

- 指针存放某个对象的地址。
- 建议：初始化所有指针。
- 空指针不指向任何对象。
- `void *`可以用于存放任意类型对象的地址
- 引用和指针的区别见: [c++中，引用和指针的区别是什么？](https://www.zhihu.com/question/37608201)

### 10. const限定符

```c++
const int bufSize = 512;
const int i = get_size();
```

- const对象必须初始化，且不能被改变
- 除非特别说明，const对象默认为文件的局部变量​，其它文件访问，必须在指定const前加extern。
- [const int、const int *、int *cosnt、const int * const、const int &的区别](https://blog.csdn.net/itworld123/article/details/78967080)

```c++
int age = 80;
const int *pt = &age; // a pointer to const int  const 只能防止修改pt 指向的值 (即不能修改age=80), 而不能防止修改pt的值, 如果pt = &sage;

int sloth =3;
int *const finger = &sloth; // a const pointer to int 
// const 不能给finger 赋新值, 即finger只能指向sloth, 但是可以通过finger 修改sloth的值;

double trouble = 3.0E2.0;
const double * const stick = &trouble; // stick 只能指向trouble, stick 不能用来修改trouble 的值; 
```
### 11. constexpr和常量表达式

```c++
const int max_files=20;//max_files 是常量表达式
const int limit=max_files+1;//limit 是常量表达式
int staff_size=27;//staff_size 不是常量表达式
const int sz=get_size();//运行时才知道值，因此不是常量；

constexpr int mf=20;//20是常量表达式
constexpr int limit=mf+1;//mf+1是常量表达式
constexpr int sz=size();//只有当size是一个constexpr函数时才是一条正确的声明语句
```

- 常量表达式：指值不会改变，且在编译过程中就能得到计算结果的表达式。
- 允许将变量声明为constexpr类型以便由编译器来验证变量的值是否是一个常量的表达式。

### 12. 类型别名

- 传统别名：使用typedef来定义类型的同义词。 typedef double wages; (wages为别名)
- 新标准别名：别名声明（alias declaration）： using SI = Sales_item;（SI为别名）

### 13. auto类型说明符

```c++
int i = 0, &r = i;
auto a = r; // 推断a的类型是int。
```

- auto类型说明符：让编译器自动推断类型。
- 会忽略顶层const。
- 多用于循环迭代中

### 14. decltype类型指示符

从表达式推断定义的变量的类型

### 15. 自定义数据结构

```c++
struct Sales_data {         // 关键字struct开始，紧跟类名和类体
    std::string bookNo;
    unsigned units_sold = 0;
    double revenue = 0.0;
}
```

### 16. 编写自己的头文件

```c++
#ifndef SALES_DATA_H        //仅当SALES_DATA_H未定义时，才执行下面的代码，避免重复定义
#define SALES_DATA_H
strct Sale_data{
    ...
}
#endif
```


# 第三章 字符串、向量和数组

### 1. 命名空间using

```c++
using std::name;  //

```
- 头文件中不应该包含using声明

### 2. 标准库string

```c++
#include <string>
using std::string;
string s1; //默认初始化
string s2(s1); //直接初始化
string s2 = s1; //拷贝初始化,等价于s2(s1)
string s3("value"); //最后的空字符没有拷贝
string s3 = "value"; //最后的空字符没有拷贝
string s4(n, 'c');  //把s4初始化为由连续n个字符c组成的串
```

- 拷贝初始化（copy initialization）：使用等号`=`将一个已有的对象拷贝到正在创建的对象。
- 直接初始化（direct initialization）：通过括号给对象赋值。

**string对象上的操作**

| 操作 | 解释 |
|-----|-----|
| `os << s` | 将`s`写到输出流`os`当中，返回`os` |
| `is >> s` | 从`is`中读取字符串赋给`s`，字符串以空白分割，返回`is` |
| `getline(is, s)` | 从`is`中读取一行赋给`s`，返回`is` |
| `s.empty()` | `s`为空返回`true`，否则返回`false` |
| `s.size()` | 返回`s`中字符的个数 |
| `s[n]` | 返回`s`中第`n`个字符的引用，位置`n`从0计起 |
| `s1+s2` | 返回`s1`和`s2`连接后的结果 |
| `s1=s2` | 用`s2`的副本代替`s1`中原来的字符 |
| `s1==s2` | 如果`s1`和`s2`中所含的字符完全一样，则它们相等；`string`对象的相等性判断对字母的大小写敏感 |
| `s1!=s2` | 同上 |
| `<`, `<=`, `>`, `>=` | 利用字符在字典中的顺序进行比较，且对字母的大小写敏感 |

- string io：
    - 执行读操作`>>`：忽略掉开头的空白（包括空格、换行符和制表符），直到遇到下一处空白为止。
    - `getline`：读取一整行，**包括空白符**。
- 字符串字面值和string是不同的类型。

**处理string对象中的字符**

| 函数 | 解释 |
|-----|-----|
| `isalnum(c)` | 当`c`是字母或数字时为真 |
| `isalpha(c)` | 当`c`是字母时为真 |
| `iscntrl(c)` | 当`c`是控制字符时为真 |
| `isdigit(c)` | 当`c`是数字时为真 |
| `isgraph(c)` | 当`c`不是空格但可以打印时为真 |
| `islower(c)` | 当`c`是小写字母时为真 |
| `isprint(c)` | 当`c`是可打印字符时为真 |
| `ispunct(c)` | 当`c`是标点符号时为真 |
| `isspace(c)` | 当`c`是空白时为真（空格、横向制表符、纵向制表符、回车符、换行符、进纸符） |
| `isupper(c)` | 当`c`是大写字母时为真 |
| `isxdigit(c)` | 当`c`是十六进制数字时为真 |
| `tolower(c)` | 当`c`是大写字母，输出对应的小写字母；否则原样输出`c` |
| `toupper(c)` | 当`c`是小写字母，输出对应的大写字母；否则原样输出`c` |

- 遍历字符串：使用**范围for**（range for）语句： `for (auto c: str)`，或者 `for (auto &c: str)`使用引用直接改变字符串中的字符。 （C++11）

### 3. 标准库vector

```c++
#include <iostream>
#include <vector>

using namespace std;

int main(int argc, char const *argv[])
{
    vector<int> obj;
    for (int i = 0; i < 10; i++)
    {
        obj.push_back(i);
    }

    for (int i = 0; i < obj.size(); i++)
    {
        cout<<obj[i]<<",";
    }
    return 0;
}
```

- vector是一个**容器**，也是一个类模板；暂时当为动态数组去看。

**vector初始化**

| 方法 | 解释 |
|-----|-----|
| `vector<T> v1` | `v1`是一个空`vector`，它潜在的元素是`T`类型的，执行默认初始化 |
| `vector<T> v2(v1)` | `v2`中包含有`v1`所有元素的副本 |
| `vector<T> v2 = v1` | 等价于`v2(v1)`，`v2`中包含`v1`所有元素的副本 |
| `vector<T> v3(n, val)` | `v3`包含了n个重复的元素，每个元素的值都是`val` |
| `vector<T> v4(n)` | `v4`包含了n个重复地执行了值初始化的对象 |
| `vector<T> v5{a, b, c...}` | `v5`包含了初始值个数的元素，每个元素被赋予相应的初始值 |
| `vector<T> v5={a, b, c...}` | 等价于`v5{a, b, c...}` |

- 列表初始化： `vector<string> v{"a", "an", "the"};` （C++11）

**vector操作**
| 操作 | 解释 |
|-----|-----|
| `v.emtpy()` | 如果`v`不含有任何元素，返回真；否则返回假 |
| `v.size()` |  返回`v`中元素的个数|
| `v.push_back(t)` | 向`v`的尾端添加一个值为`t`的元素 |
| `v[n]` | 返回`v`中第`n`个位置上元素的**引用** |
| `v1 = v2` | 用`v2`中的元素拷贝替换`v1`中的元素  |
| `v1 = {a,b,c...}` | 用列表中元素的拷贝替换`v1`中的元素 |
| `v1 == v2` | `v1`和`v2`相等当且仅当它们的元素数量相同且对应位置的元素值都相同 |
| `v1 != v2` | 同上 |

### 4. 迭代器iterator

```c++
#include <iostream>
#include <vector>

using namespace std;

int main(int argc, char const *argv[])
{
    vector<int> obj;
    for (int i = 0; i < 10; i++)
    {
        obj.push_back(i);
    }

    vector<int>::iterator i;  //定义正向迭代器
    for (i = obj.begin(); i != obj.end(); ++i) {  //用迭代器遍历容器
        cout << *i << ",";  //*i 就是迭代器i指向的元素
    }
    return 0;
}

```
- 所有标准库容器都可以使用迭代器。
- 类似于指针类型，迭代器也提供了对对象的间接访问。
- `auto b = v.begin();`返回指向第一个元素的迭代器。
- `auto e = v.end();`返回指向最后一个元素的下一个（哨兵，尾后,one past the end）的迭代器（off the end）。
- 如果容器为空， `begin()`和 `end()`返回的是同一个迭代器，都是尾后迭代器。
- 使用解引用符`*`访问迭代器指向的元素。
- 养成使用迭代器和`!=`的习惯（泛型编程）。
- **容器**：可以包含其他对象；但所有的对象必须类型相同。
- **迭代器（iterator）**：每种标准容器都有自己的迭代器。`C++`倾向于用迭代器而不是下标遍历元素。
- **const_iterator**：只能读取容器内元素不能改变。
- **箭头运算符**： 解引用 + 成员访问，`it->mem`等价于 `(*it).mem`
- **谨记**：但凡是使用了迭代器的循环体，都不要向迭代器所属的容器添加元素。

**迭代器的运算符**

| 运算符 | 解释 |
|-----|-----|
| `*iter` | 返回迭代器`iter`所指向的**元素的引用** |
| `iter->mem` | 等价于`(*iter).mem` |
| `++iter` | 令`iter`指示容器中的下一个元素 |
| `--iter` | 令`iter`指示容器中的上一个元素 |
| `iter1 == iter2` | 判断两个迭代器是否相等 |

**迭代器运算**

| 运算符 | 解释 |
|-----|-----|
| `iter + n` | 迭代器加上一个整数值仍得到一个迭代器，迭代器指示的新位置和原来相比向前移动了若干个元素。结果迭代器或者指示容器内的一个元素，或者指示容器尾元素的下一位置。 |
| `iter - n` | 迭代器减去一个证书仍得到一个迭代器，迭代器指示的新位置比原来向后移动了若干个元素。结果迭代器或者指向容器内的一个元素，或者指示容器尾元素的下一位置。 |
| `iter1 += n` | 迭代器加法的复合赋值语句，将`iter1`加n的结果赋给`iter1` |
| `iter1 -= n` | 迭代器减法的复合赋值语句，将`iter2`减n的加过赋给`iter1` |
| `iter1 - iter2` | 两个迭代器相减的结果是它们之间的距离，也就是说，将运算符右侧的迭代器向前移动差值个元素后得到左侧的迭代器。参与运算的两个迭代器必须指向的是同一个容器中的元素或者尾元素的下一位置。 |
| `>`、`>=`、`<`、`<=` | 迭代器的关系运算符，如果某迭代器 |


### 5. 数组

```c++
int ragnar[3];
int ragnar[3]={}; //全部赋值为0
int ragnar[3]={1,2,3};//分别赋值
int ragnar[]={1,2,3};//自动识别长度
```

**C风格字符串**

```c++
char a [] = "hello";   //C风格
string s1 = "hello"
```

- 少用数组和指针，多用vector和迭代器
- 尽量使用string，而不使用C风格字符串
- C++中没有多维数组，所谓的多级数组其实就是数组的数组​

# 第四章 表达式

- 短路求值​：&&和||操作时，只有当其左操作数无法确定整个逻辑表达式的值时，才会去计算右操作数​。
- 赋值操作具有右结合的性质，而且赋值操作返回的是左值。a = b = 0; 的执行顺序是 b = 0; 返回b，然后a = b;
- 只有在必要的时候才使用后置操作符（后自增，后自减）。​因为前置操作符的性能比后置操作符更好，效率更高​。
- 条件运算符（?:）允许我们把简单的if-else逻辑嵌入到单个表达式中去，按照如下形式：cond? expr1: expr2
- 左值和右值: [C++11 左值、右值、右值引用详解](https://blog.csdn.net/hyman_yx/article/details/52044632)
- `sizeof`返回一条表达式或一个类型名字所占的字节数, 用法: `sizeof(type)` 或 `sizeof expr`

# 第五章 语句

- 空语句：只有一个单独的分号。
- if语句
  ```c++
   if(condition)
   {
       statement
   }
   else if(condition2)
   {
       statement2
   }
  ```
- switch
```c++
  switch(expression){
    case constant-expression  :
       statement(s);
       break; // 可选的,如果case语句不包含break，控制流将会继续后续的case，直到遇到break为止
    case constant-expression  :
       statement(s);
       break; // 可选的
  
    // 您可以有任意数量的 case 语句
    default : // 可选的
       statement(s);
}
```
- while
```c++
while(condition)
{
   statement(s);
}
或
do
{
   statement(s);
}while( condition );
```

- for
```c++
for ( init; condition; increment )
{
   statement(s);
}
或
int my_array[5] = {1, 2, 3, 4, 5};           
// 范围for语句
for (int &x : my_array)
{
    x *= 2;
    cout << x << endl;  
}

```

- break：`break`语句负责终止离它最近的`while`、`do while`、`for`或者`switch`语句，并从这些语句之后的第一条语句开始继续执行。
- continue：终止最近的循环中的当前迭代并立即开始下一次迭代。只能在`while`、`do while`、`for`循环的内部。
- throw：抛出异常
- try语句块：以 `try`关键词开始，以一个或多个 `catch`字句结束。 `try`语句块中的代码抛出的异常通常会被某个 `catch`捕获并处理。 `catch`子句也被称为**异常处理代码**。
```c++
double division(int a, int b)
{
   if( b == 0 )
   {
      throw "Division by zero condition!";
   }
   return (a/b);
}
 
int main ()
{
   int x = 50;
   int y = 0;
   double z = 0;
 
   try {
     z = division(x, y);
     cout << z << endl;
   }catch (const char* msg) {
     cerr << msg << endl;
   }
   return 0;
}
```

# 第6章 函数

```c++
// 计算阶乘 5!=5*4*3*2*1=120    
int fact(int val)              // 函数定义,没有返回值，定义为void
{
    int ret = 1;
    while (val>1)
        ret *= val--;
    return ret;
}

int main(int argc, char const *argv[])
{
    int j = fact(5);              // 函数调用
    cout << "5! is " << j << endl;
    return 0;
}
```
- **函数声明**：函数的声明和定义唯一的区别是声明无需函数体，用一个分号替代。函数声明主要用于描述函数的接口，也称**函数原型**。
- **在头文件中进行函数声明**：建议变量在头文件中声明；在源文件中定义。
- **分离编译**： `CC a.cc b.cc`直接编译生成可执行文件；`CC -c a.cc b.cc`编译生成对象代码`a.o b.o`； `CC a.o b.o`编译生成可执行文件
- 在C++语言中，建议使用引用类型的形参代替指针, 除了引用，其它都是值拷贝，包括指针
- 当我们为函数传递一个数组时，实际上传递的是指向数组首元素的指针, 形参类型const int *, const int[], const int[10]是等价的，数组的大小对函数调用没有影响
- 含有​可变形参​void foo(parm_list, ...); 或者 void foo(...);

**可变形参**
`initializer_list`提供的操作（`C++11`）：

| 操作 | 解释 |
|-----|-----|
| `initializer_list<T> lst;` | 默认初始化；`T`类型元素的空列表 |
| `initializer_list<T> lst{a,b,c...};` | `lst`的元素数量和初始值一样多；`lst`的元素是对应初始值的副本；列表中的元素是`const`。 |
| `lst2(lst)` | 拷贝或赋值一个`initializer_list`对象不会拷贝列表中的元素；拷贝后，原始列表和副本共享元素。 |
| `lst2 = lst` | 同上 |
| `lst.size()` | 列表中的元素数量 |
| `lst.begin()` | 返回指向`lst`中首元素的指针 |
| `lst.end()` | 返回指向`lst`中微元素下一位置的指针 |

- 所有实参类型相同，可以使用 `initializer_list`的标准库类型。
- 实参类型不同，可以使用`可变参数模板`。
- 省略形参符： `...`，便于`C++`访问某些C代码，这些C代码使用了 `varargs`的C标准功能。

**有返回值函数**

- `return`语句的返回值的类型必须和函数的返回类型相同，或者能够**隐式地**转换成函数的返回类型。
- 值的返回：返回的值用于初始化调用点的一个**临时量**，该临时量就是函数调用的结果。
- **不要返回局部对象的引用或指针**。
- **引用返回左值**：函数的返回类型决定函数调用是否是左值。调用一个返回引用的函数得到左值；其他返回类型得到右值。
- **列表初始化返回值**：函数可以返回花括号包围的值的列表。（`C++11`）
- **主函数main的返回值**：如果结尾没有`return`，编译器将隐式地插入一条返回0的`return`语句。返回0代表执行成功。

**返回数组指针**

- `Type (*function (parameter_list))[dimension]`
- 使用类型别名： `typedef int arrT[10];` 或者 `using arrT = int[10;]`，然后 `arrT* func() {...}`
- 使用 `decltype`： `decltype(odd) *arrPtr(int i) {...}`
- **尾置返回类型**： 在形参列表后面以一个`->`开始：`auto func(int i) -> int(*)[10]`（`C++11`）

**函数重载**

- **重载**：如果同一作用域内几个函数名字相同但形参列表不同，我们称之为重载（overload）函数。
- `main`函数不能重载。
- **重载和const形参**：
  - 一个有顶层const的形参和没有它的函数无法区分。 `Record lookup(Phone* const)`和 `Record lookup(Phone*)`无法区分。
  - 相反，是否有某个底层const形参可以区分。 `Record lookup(Account*)`和 `Record lookup(const Account*)`可以区分。
- **重载和作用域**：若在内层作用域中声明名字，它将隐藏外层作用域中声明的同名实体，在不同的作用域中无法重载函数名。


**默认实参**

- `string screen(sz ht = 24, sz wid = 80, char backgrnd = ' ');`
- 一旦某个形参被赋予了默认值，那么它之后的形参都必须要有默认值。


**constexpr**

- 指能用于常量表达式的函数。
- `constexpr int new_sz() {return 42;}`
- 函数的返回类型及所有形参类型都要是字面值类型。
- `constexpr`函数应该在头文件中定义。

**调试帮助**

- `assert`预处理宏（preprocessor macro）：`assert(expr);`

开关调试状态：

`CC -D NDEBUG main.c`可以定义这个变量`NDEBUG`。

```cpp
void print(){
    #ifndef NDEBUG
        cerr << __func__ << "..." << endl;
    #endif
}
```

**函数匹配**

- **候选函数**：选定本次调用对应的重载函数集，集合中的函数称为候选函数（candidate function）。
- **可行函数**：考察本次调用提供的实参，选出可以被这组实参调用的函数，新选出的函数称为可行函数（viable function）。
- **寻找最佳匹配**：基本思想：实参类型和形参类型越接近，它们匹配地越好。

**函数指针**

```
//定义函数function2
bool function2(const string &,const string &);

//定义指针指定输入参数的指针
bool *pf(const string &,const string &);

pf=function2;//将指针pf指向lengthCompare的函数

auto b1=pf("hello","goodbye");//调用函数

auto b2=(*pf)("hello","goodbye");//一个等价的调用

//使用指针函数，方便我们在某些状况下使用指定的重载函数，避免产生隐式转换的错误

void ff(int* )//重载函数1

void ff(unsigned int)//重载函数2

//定义函数指针，并初始化
void (*pf1)(unsigned int )=ff;
```

```c++
double (*pf) (int); // pf points to a function that returns double 
double *pf (int); // pf() a function that returns a pointer-to-double 

double pam(int);
doube (*pf) (int);
pf = pam; // pf now points to the pam() function
```
# 第7章 类

```c++
class Hello
{
private:                    // 私有方法和属性
    string name;
    int age;
public:                    // 公有方法和属性
    Hello(string name, int age);  // 构造函数放在类的public部分,与类同名
    ~Hello();                   //析构函数 与类同名，在前面加了个波浪号（~）
    void say();
};

Hello::Hello(string name, int age):name(name),age(age)
{
    cout << "hello calls, name:" << name << ", age:" << age << endl;
    // self->name = name;
    // self->age = age;
}

Hello::~Hello()
{
    cout << "hello dead!" << endl;
}

void Hello::say()
{
    cout << "hello say, name:" << name <<", age:" << age << endl;
}

int main(int argc, char const *argv[])
{
    Hello h("xiaomu", 20);
    h.say();
    return 0;
}
```

- 使用 `class`：在第一个访问说明符之前的成员是 `priavte`的。
- 使用 `struct`：在第一个访问说明符之前的成员是 `public`的。

**友元**
- 允许特定的**非成员函数**访问一个类的**私有成员**.
- 友元的声明以关键字 `friend`开始。 `friend Sales_data add(const Sales_data&, const Sales_data&);`表示非成员函数`add`可以访问类的非公有成员。
- 通常将友元声明成组地放在**类定义的开始或者结尾**。
- 类之间的友元：
  - 如果一个类指定了友元类，则友元类的成员函数可以访问此类包括非公有成员在内的所有成员。

**聚合类 （aggregate class）**

- 满足以下所有条件：
  - 所有成员都是`public`的。
  - 没有定义任何构造函数。
  - 没有类内初始值。
  - 没有基类，也没有`virtual`函数。
- 可以使用一个花括号括起来的成员初始值列表，初始值的顺序必须和声明的顺序一致。


**类的静态成员**

- 非`static`数据成员存在于类类型的每个对象中。
- `static`数据成员独立于该类的任意对象而存在。
- 每个`static`数据成员是与类关联的对象，并不与该类的对象相关联。
- 声明：
  - 声明之前加上关键词`static`。
- 使用：
  - 使用**作用域运算符**`::`直接访问静态成员:`r = Account::rate();`
  - 也可以使用对象访问：`r = ac.rate();`
- 定义：
  - 在类外部定义时不用加`static`。
- 初始化：
  - 通常不在类的内部初始化，而是在定义时进行初始化，如 `double Account::interestRate = initRate();`
  - 如果一定要在类内部定义，则要求必须是字面值常量类型的`constexpr`。