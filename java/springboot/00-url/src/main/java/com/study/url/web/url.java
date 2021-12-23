package com.study.url.web;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/v1")
public class url {

    @GetMapping("/say")
    public String say(){
        return "say SpringBoot";
    }
}
