package com.study.jpa.web;

import com.study.jpa.domain.Book;
import com.study.jpa.service.BookService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/v1")
public class BookApp {

    @Autowired
    private BookService bookService;

    @GetMapping("/books")
    public List<Book> getAll(){
        return bookService.findAll();
    }

    @PostMapping("/books")
    public Book post(@RequestParam String name,
                     @RequestParam String author,
                     @RequestParam String description,
                     @RequestParam int status){
        Book book = new Book();
        book.setName(name);
        book.setAuthor(author);
        book.setDescription(description);
        book.setStatus(status);

        return bookService.save(book);
    }

    // 获取一条书单
    @GetMapping("/books/{id}")
    public Book getOne(@PathVariable long id){
        return bookService.findOne(id);
    }

//    @PutMapping("/books")
//    public Book update(@RequestParam long id,
//                       @RequestParam String name,
//                       @RequestParam String author,
//                       @RequestParam String description,
//                       @RequestParam int status){
//        Book book = new Book();
//        book.setId(id);
//        book.setName(name);
//        book.setAuthor(author);
//        book.setDescription(description);
//        book.setStatus(status);
//
//        return bookService.save(book);
//    }

    // 更新一本书单的方法二
    @PutMapping("/books")
    public Book update(Book book){
        return bookService.save(book);
    }

    // 删除一条书单
    @DeleteMapping("/books/{id}")
    public void deleteById(@PathVariable long id){
        bookService.delete(id);
    }

    @PostMapping("/books/by/author")
    public List<Book> findByAuthor(@RequestParam String author){
        return bookService.findByAuthor(author);
    }

    @PostMapping("/books/by/author/status")
    public List<Book> findByAuthorAndStatus(@RequestParam String author,
                                            @RequestParam int status){
        return bookService.findByAuthorAndStatus(author, status);
    }

    @PostMapping("/books/by/description")
    public List<Book> findByDescriptionEndsWith(@RequestParam String description){
        return bookService.findByDescriptionEndsWith(description);
    }

    @PostMapping("/books/by/description/contains")
    public List<Book> findByDescriptionContains(@RequestParam String description){
        return bookService.findByDescriptionContains(description);
    }

    @PostMapping("/books/by/length")
    public List<Book> findByLength(@RequestParam int len){
        return bookService.findByJPQL(len);
    }

    @PostMapping("/books/update/by/id")
    public int updateStatusById(@RequestParam int status, @RequestParam long id){
        return bookService.updateByJPQL(status, id);
    }

    @PostMapping("/books/delete")
    public int deleteByJPQL(@RequestParam long id){
        return bookService.deleteByJPQL(id);
    }

    @PostMapping("/books/delete/and/update")
    public int deleteAndUpdate(@RequestParam long id,
                               @RequestParam int status,
                               @RequestParam long uid){
        return bookService.deleteAndUpdate(id, status, uid);
    }
}
