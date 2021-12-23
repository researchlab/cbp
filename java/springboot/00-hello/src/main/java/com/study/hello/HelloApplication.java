package com.study.hello;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

// 放置在Springboot启动类上，表明该类是开启Springboot容器的入口，它是一个复合注解。里面包含了包扫描，自动注入，配置注入的功能，下面就给大家介绍里面的注解
/**
 * 【1】@SpringBootConfiguration
 * 它表示的是该类会作为Springboot的一个配置类，进入该注解，发现里面包含@Configuration注解，@Configuration注解是Spring里面的注解，在Spring里，它表示该类也是一个配置类。进入@Configuration注解，我们发现他是被@Component所修饰的，所以该配置类也是一个组件。
 *
 * 【2】@EnableAutoConfiguration
 * 它表示开启自动配置功能。进入@EnableAutoConfiguration中，发现它仍然是一个组合注解。里面包含以下两个注解
 *
 * 【3】@ComponentScan
 * 用来将指定包(如果未指定就是将当前类所在包及其子孙包)加入SpringIOC的包扫描，本质上等于<context:component-scan>配置
 * */
@SpringBootApplication
public class HelloApplication {

    public static void main(String[] args) {
        SpringApplication.run(HelloApplication.class, args);
    }

}
