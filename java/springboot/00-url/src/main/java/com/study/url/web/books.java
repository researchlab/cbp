package com.study.url.web;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class books {
    @GetMapping("/books")
    public String books(){
        return "books";
    }
}

/**
 *  thymeleaf 框架 默认只能识别 resources/templates 下面的.html 文件 不能识别static下的html文件
 *  如上所示， return books 不需要带html后缀;
 *  
 * */