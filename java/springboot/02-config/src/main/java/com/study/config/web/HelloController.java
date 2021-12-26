package com.study.config.web;

import com.study.config.domain.Book;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.HashMap;
import java.util.Map;

@RestController
@RequestMapping("/v1")
public class HelloController {

    @Autowired
    private Book book;

    @Value("${book.name}")
    private String name;
    @Value("${book.author}")
    private String author;
    // 引用了不存在的字段如book.isbn 则启动会失败;
    @Value("${book.isbn}")
    private String isbn;

    @GetMapping("/books/{id}")
    public Object getOne(@PathVariable long id){
        Map<String, Object> book = new HashMap<>();
        book.put("name", name);
        book.put("isbn", isbn);
        book.put("author", author);
        return book;
    }

    @GetMapping("/books/one/{id}")
    public Object getBook(@PathVariable long id){
        return book;
    }
}
