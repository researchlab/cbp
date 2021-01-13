# C++ Best Practices 

Best C++ Practices along with the detailed samples.

References

> C++ Primer, 5th Edition, [source files](https://www.informit.com/store/c-plus-plus-primer-9780321714114)

一、基础

1.1 一个项目入门 C++ 足以：CPlusPlusThings

CPlusPlusThings 是国人开源一个 C++ 学习项目。它系统地将 C++ 学习分为了【基础进阶】、【实战系列】、【C++2.0 新特性】、【设计模式】和【STL 源码剖析】、【并发编程】、【C++ 惯用法】、【学习课程】、【工具】、【拓展】。

作为一个全面系统的 C++ 学习项目，CPlusPlusThings 是优秀的，它合理地安排了 10 Days 的实战部分，在实战中了解语法和函数用法，唯一不足的是，在注释部分有些不尽人意，对部分新手程序员并不是很友好。

GitHub 地址: https://github.com/Light-City/CPlusPlusThings

1.2 基础部分之算法：C-Plus-Plus

C-Plus-Plus 是收录用 C++ 实现的各种算法的集合，并按照 MIT 许可协议进行授权。这些算法涵盖了计算机科学、数学和统计学、数据科学、机器学习、工程等各种主题。除外，你可能会发现针对同一目标的多个实现使用不同的算法策略和优化。

GitHub 地址: https://github.com/TheAlgorithms/C-Plus-Plus

二、进阶

2.1 现代 C++：modern-cpp-tutorial

modern-cpp-tutorial 是现代 C++ 教程，它的目的是提供关于现代 C++（2020 年前）的相关特性的全面介绍。除了介绍了代码之外，它还尽可能简单地介绍了其技术需求的历史背景，这对理解为什么会出现这些特性提供了很大的帮助。

GitHub 地址: https://github.com/changkun/modern-cpp-tutorial


2.2 进阶指南：CppTemplateTutorial

CppTemplateTutorial 为中文的 C++ Template 的教学指南。

与知名书籍 C++ Templates 不同，该系列教程将 C++ Templates 作为一门图灵完备的语言来讲授，以求帮助读者对 Meta-Programming 融会贯通。

本项目写作初衷，就是通过 “编程语言” 的视角，介绍一个简单、清晰的 “模板语言”。

我会尽可能地将模板的诸多要素连串起来，用一些简单的例子帮助读者学习这门 “语言”，让读者在编写、阅读模板代码的时候，能像 if(exp) { dosomething(); } 一样的信手拈来，让 “模板元编程” 技术成为读者牢固掌握、可举一反三的有用技能。

适合熟悉 C++ 的基本语法、使用过 STL、熟悉一些常用的算法，以及递归等程序设计方法的 C++ 学习者阅读。虽然项目章节文章写的深入浅出，不过唯一的遗憾是尚未完成所有章节内容。进度如下：

0.前言

1.Template 的基本语法

2.模板元编程基础

3.深入理解特化与偏特化

4.元编程下的数据结构与算法 （尚未开始）

5.模板的进阶技巧（尚未开始）

6.模板的威力：从 foreach, transform 到 Linq（尚未开始）

7.结语：讨论有益，争端无用（尚未开始）

GitHub 地址: https://github.com/wuye9036/CppTemplateTutorial

三、动手实战

3.0 源码阅读: Tinyhttpd

Tinyhttpd 是J. David Blackstone在1999年写的一个不到 500 行的超轻量型 Http Server，用来学习非常不错，可以帮助我们真正理解服务器程序的本质。

GitHub 地址: https://github.com/EZLippi/Tinyhttpd

3.1 来实践一下：MyTinySTL

当你学习完 C++ 的“书本”知识后，是不是有些手痒了呢？MyTinySTL 这个注释详细、实践夯实基础的项目便是你 C++ 学习之旅的下一站。

作为新手练习用途，MyTinySTL 的作者 Alinshans 用 C++11 重新复写了一个小型 STL（容器库＋算法库）。代码结构清晰规范、包含中文文档与注释，并且自带一个简单的测试框架，适合 C++ 新手来实践一番。

GitHub 地址: https://github.com/Alinshans/MyTinySTL

3.2 源码阅读: leveldb

LevelDB is a fast key-value storage library written at Google that provides an ordered mapping from string keys to string values.

GitHub 地址: https://github.com/google/leveldb
