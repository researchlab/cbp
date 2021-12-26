package com.study.params.web;

import org.springframework.web.bind.annotation.*;

import java.util.*;

// 给这个类用@RestController注解， 表示RestFULL风格返回格式
@RestController
@RequestMapping("/api/v1")
public class HelloController {
    private Object book(Map<String, Object> input){
//        System.out.println("input:" + input);
        UUID uuid = UUID.randomUUID();
        Map<String, Object> book = new HashMap<>();
        book.put("name", "互联网世界观");
        book.put("isbn", uuid.toString());
        book.put("author", "李善友");
        book.put("input", input);
        return book;
    }

    // @PathVariable  注解路由中的变量id;
    // 默认 路由中的变量名(此处是{id}中的id) 应和参数中的变量名一致(long id中的id)
    @RequestMapping(value="/books/{id}", method = RequestMethod.GET)
    public Object getOne(@PathVariable long id){
            Map<String, Object> input = new HashMap<>();
            input.put("id", id);
            return book(input);
    }

    // 通过指定@PathVariable("id") long bid 修改参数中的变量名为bid
    @GetMapping("/books/another/{id}")
    public Object GetAnotherOne(@PathVariable("id") long bid){
            Map<String, Object> input = new HashMap<>();
            input.put("id", bid);
            return book(input);
    }

    // 可以提取路由中的多个变量;
    // 变量在路由的顺序可以随意，只需要变量名对上即可;
    // @PathVariable(name="username", value="username", required=ture/false)
    // 这里name和value只需要写一个即可，如果都写则它们的值应该相同如上，否则报错，还有required似乎没有什么用途
//    @GetMapping("/{id}/books/{username}")
    @GetMapping("/books/{id}/{username}")
    public Object getOneWithUsername(@PathVariable("id") long bid,
                         @PathVariable(name="username") String username){
        Map<String, Object> input = new HashMap<>();
        input.put("bid", bid);
        input.put("username", username);
        return book(input);
    }

    // 正则表达式 {参数名: 正则表达式}
    // 如下示例 username 只接收由小写字符a-z,数字0-9及下划线组成的变量名，其它会报错400;
    // 这里要注意 路由不要和上面重复了 如 /books/{username} 与 /books/{id} 是重复的路由
    // 会冲突的, 要修改成不相同
    @GetMapping("/books/regex/{username:[a-z0-9_]+}")
    public Object getOneWithRegex(@PathVariable String username){
        Map<String, Object> input = new HashMap<>();
        input.put("username", username);
        return book(input);
    }

    // @RequestParam 接收post 请求, body 应该设置为x-www-form-urlencoded
    @PostMapping("/books")
    public Object post(@RequestParam("name") String name,
                       @RequestParam("author") String author,
                       @RequestParam("isbn") String isbn){
        Map<String, Object> input = new HashMap<String, Object>();
        input.put("name", name);
        input.put("author", author);
        input.put("isbn", isbn);
        return book(input);
    }

    @GetMapping("/books")
    public Object getAll(@RequestParam("pageNumber") int pageNumber,
                         @RequestParam(value="pageSize", defaultValue = "100") int pageSize){
        Map<String, Object> book1 = new HashMap<>();
        book1.put("name", "互联网世界观");
        book1.put("isbn", "10201020111");
        book1.put("author", "李善友");
        Map<String, Object> book2 = new HashMap<>();
        book2.put("name", "程序猿的思维修炼");
        book2.put("isbn","201002222");
        book2.put("author", "程序猿");

        List<Map> contents = new ArrayList<>();
        contents.add(book1);
        contents.add(book2);

        Map<String, Object> response = new HashMap<>();
        response.put("pageNumber", pageNumber);
        response.put("pageSize", pageSize);
        response.put("content", contents);

        return response;
    }
}
