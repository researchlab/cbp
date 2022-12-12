struct Struct {
    e: i32
}
fn main() {
    let (a,b,c,d,e);

    (a,b)= (1,2);
    [c,..,d,_]=[1,2,3,4,5];
    // Struct{e} = Struct{e:5};
    Struct{e,..}=Struct{e:5};
    assert_eq!([1,2,1,4,5],[a,b,c,d,e]);
    shadowing();
}

fn shadowing(){
    let x = 5;
    // 对之前的x 进行遮蔽
    let x = x+1;
    {
        let x = x*2;
        println!("The value of x in the inner scope is:{}",x);
    }
    println!("The value of x is: {}", x);
}

//变量遮蔽的用处在于，如果你在某个作用域内无需再使用之前的变量（在被遮蔽后，无法再访问到之前的同名变量），就可以重复的使用变量名字，而不用绞尽脑汁去想更多的名字。 不建议使用
