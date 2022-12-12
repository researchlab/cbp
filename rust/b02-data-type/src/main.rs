// 数值类型: 有符号整数 (i8, i16, i32, i64, isize)、 无符号整数 (u8, u16, u32, u64, usize) 、浮点数 (f32, f64)、以及有理数、复数
// 字符串：字符串字面量和字符串切片 &str
// 布尔类型： true和false
// 字符类型: 表示单个 Unicode 字符，存储为 4 个字节
// 单元类型: 即 () ，其唯一的值也是 ()
fn main() {
    // date type error
    // let guess = "42".parse().expect("Not a number!");
    // method1 
    let _guess:i32 = "42".parse().expect("Not a number!");
    // method2
    let _guess = "42".parse::<i32>().expect("Not a number!");
    // range()
    complex();
}

fn range(){
    // [1,2,3,4,5]
    for i in 1..=5{
        println!("{}",i);
    }
    // [1,2,3,4]
    for i in 1..5{
        println!("{}",i);
    }
    for i in 'a'..='z'{
        println!("{}",i);
    }
}

use num::complex::Complex;

fn complex(){
    let a = Complex{re:2.1, im:-1.2};
    let b = Complex::new(11.1,22.2);
    let result=a+b;
    println!("{}+{}i",result.re, result.im);
}
