package com.study.url.web;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

import java.util.HashMap;
import java.util.Map;

@RestController
@RequestMapping("/api/v2")
public class url_v2 {

    @RequestMapping(value="/books/{id}", method = RequestMethod.GET)
    public Object books(){
        Map<String, Object> books = new HashMap<>();
        books.put("name", "springboot");
        books.put("code", 72);
        return books;
    }
}
