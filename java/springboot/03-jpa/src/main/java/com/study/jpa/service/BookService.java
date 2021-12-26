package com.study.jpa.service;

import com.study.jpa.domain.Book;
import com.study.jpa.domain.BookDeleteRepository;
import com.study.jpa.domain.BookRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import javax.transaction.Transactional;
import java.util.List;

@Service
public class BookService {

    @Autowired
    private BookRepository bookRepository;

    @Autowired
    private BookDeleteRepository bookDeleteRepository;

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

    // 删除一条书单
    public void delete(long id){
        bookDeleteRepository.deleteById(id);
    }

    // 根据author 查询一个书单列表
    public List<Book> findByAuthor(String author){
        return bookRepository.findByAuthor(author);
    }


    public List<Book> findByAuthorAndStatus(String author, int status){
        return bookRepository.findByAuthorAndStatus(author, status);
    }

    public List<Book> findByDescriptionEndsWith(String desc){
        return bookRepository.findByDescriptionEndsWith(desc);
    }

    public List<Book> findByDescriptionContains(String desc){
        return bookRepository.findByDescriptionContains(desc);
    }

    public List<Book> findByJPQL(int len){
        return bookRepository.findByJPQL(len);
    }

    @Transactional
    public int updateByJPQL(int status, long id){
        return bookRepository.updateByJPQL(status ,id);
    }

    @Transactional
    public int deleteByJPQL(long id){
        return bookRepository.deleteByJPQL(id);
    }

    @Transactional
    public int deleteAndUpdate(long id, int status, long uid){
        int dcount = bookRepository.deleteByJPQL(id);
        int ucount = bookRepository.updateByJPQL(status, uid);
        return dcount + ucount;
    }
}
