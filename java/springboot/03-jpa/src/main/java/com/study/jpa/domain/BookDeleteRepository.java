package com.study.jpa.domain;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.jpa.repository.support.JpaEntityInformation;
import org.springframework.data.jpa.repository.support.JpaEntityInformationSupport;
import org.springframework.data.jpa.repository.support.SimpleJpaRepository;
import org.springframework.stereotype.Repository;

import javax.persistence.EntityManager;
import javax.transaction.Transactional;
import java.util.Optional;

@Repository
@Transactional
public class BookDeleteRepository extends SimpleJpaRepository<Book, Long> {
    @Autowired
    public BookDeleteRepository(EntityManager em){
        this(JpaEntityInformationSupport.getEntityInformation(Book.class, em), em);
    }

    public BookDeleteRepository(JpaEntityInformation<Book, ?>entityInformation, EntityManager entityManager){
        super(entityInformation, entityManager);
    }

    public BookDeleteRepository(Class<Book> domainClass, EntityManager em){
        super(domainClass, em);
    }

    @Override
    public void deleteById(Long id){
        Optional<Book> rec = findById(id);
        // 判断存在才执行删除操作
        // 使得删除操作幂等
        rec.ifPresent(super::delete);
    }
}
