package com.study.hello.web;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController  // 使变成一个控制器让外部可以访问
public class SayController {
    @RequestMapping("/") // 定义路由
    public String say(){
        return "Hi SpringBoot!";
    }
}
