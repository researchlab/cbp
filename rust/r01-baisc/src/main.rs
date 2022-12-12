fn main() {
    let penguin_data = "\
    common name, length (cm)
    Little penguin, 33
    Yellow-eyed penguin,65
    Fiordland penguin,60
    Invalid,data
    ";

    let records = penguin_data.lines();
    for (i, record) in records.enumerate() {
        // println!("@record: {} {}", i, record);
        if i == 0 || record.trim().len() == 0 {
            continue;
        }
        // 声明一个fields变量，类型Vec
        // Vec 是vector的缩写，是一个可伸缩的集合类型，可以认为是一个动态数组
        // <_>表示 Vec 中的元素类型由编译器自动推断,
        let fields: Vec<_> = record.split(',').map(|field| field.trim()).collect();
        if cfg!(debug_assertions) {
            //输出到标准错误输出
            eprintln!("debug: {:?} ->{:?}", record, fields);
        }
        let name = fields[0];
        if let Ok(length) = fields[1].parse::<f32>() {
            println!("{},{}cm", name, length);
        }
    }
}
