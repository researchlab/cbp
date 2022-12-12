fn main() {
    clone();
    fuzhi();
    owner();
 }

fn clone(){
    let s1 = String::from("hello");
    let s2 = s1.clone();
    println!("s1={}, s2={}",s1,s2);
}

fn fuzhi(){
    let s1 = String::from("hello");
    let s2 = s1;
    // s1 error 
    // println!("s1={}, s2={}",s1,s2);
    println!("s2={}", s2);
}


fn owner(){
    let s = String::from("hello");
    takes_ownership(s);
    // error:- move occurs because `s` has type `String`, which does not implement the `Copy` trait
    // println!("{}",s);
    
    let x = 5;
    makes_copy(x);
    println!("x={}",x);
}

fn takes_ownership(some_string: String){
    println!("{}",some_string);
}

fn makes_copy(some_integer:i32){
    println!("{}",some_integer);
}
