package com.study.thymeleaf.service;

import com.study.thymeleaf.domain.BookRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import com.study.thymeleaf.domain.Book;

import java.util.List;

@Service
public class BookService {
    @Autowired
    private BookRepository bookRepository;

    // 查询所有书单列表
    public List<Book> findAll(){
        return bookRepository.findAll();
    }

    // 新建或更新一个书单信息
    public Book save(Book book){
        return bookRepository.save(book);
    }

    // 获取一条书单信息
    public Book findOne(long id){
        Book book = new Book();
        book.setId(id);
        book.setName("not found");
        return bookRepository.findById(id).orElse(book);
    }


}
