package com.study.jpa.domain;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Modifying;
import org.springframework.data.jpa.repository.Query;

import javax.transaction.Transactional;
import java.util.List;

public interface BookRepository extends JpaRepository<Book, Long> {

    List<Book> findByAuthor(String author);

    List<Book> findByAuthorAndStatus(String author, int status);

    List<Book> findByDescriptionEndsWith(String desc);

    List<Book> findByDescriptionContains(String desc);

//    Book 是实体名
//    book 是数据库表名， 这里需要设置 nativeQuery=true  才表示使用sql 数据查询
    //    @Query("select b from Book b where length(b.name) > ?1")
    @Query(value = "select * from book where LENGTH(name) > ?1", nativeQuery = true)
    List<Book> findByJPQL(int len);

    @Modifying
    @Query("update Book b set b.status = ?1 where id= ?2")
    int updateByJPQL(int status, long id);

    @Transactional
    @Modifying
    // 错误示范
    // 错误1 用原生sql时，里面不能用对象名称，如下面用到了Book 这是不对的
    // @Query(value = "delete from Book b where b.id = ?1", nativeQuery = true)
    // 错误2 用原生sql 时 不能用表别名，如下是错误形式
    // @Query(value = "delete from book b where b.id = ?1", nativeQuery = true

    // 正确示范
    // @Query("delete from Book b  where b.id = ?1")
    // 用原生sql 时 where子句中可以通过表名.字段名
    // @Query(value = "delete from book where book.id = ?1", nativeQuery = true)
    @Query(value = "delete from book where id = ?1", nativeQuery = true)
    int deleteByJPQL(long id);

}
