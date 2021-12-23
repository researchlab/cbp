package com.study.url.web;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

@Controller
public class homepage {
    @RequestMapping(value="/", method=RequestMethod.GET)
    public String home(){
        return "index";
    }
}
