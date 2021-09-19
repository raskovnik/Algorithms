fn bruteforce(list: Vec<i32>, target: i32) -> (i32, i32) {
    for c in list.iter() {
        for j in list[1..].iter() {
            if *c + *j == target {return (*c, *j)}
        }
    }
    return (0, 0);
}

fn main() {
    let list = vec![1, 4, 54, 2, 6, 345, 56 , 3];
    let result = bruteforce(list, 12);
    println!("{:?}", result);
}