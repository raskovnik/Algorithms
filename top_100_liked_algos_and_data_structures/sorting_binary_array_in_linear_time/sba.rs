fn count<T: std::cmp::PartialEq>(list: &[T], target: T) -> i32 {
    let mut number = 0;

    for c in list.iter() {
        if *c == target { number = number + 1;}
    }
    return number;
}

fn sort(list: &mut [i32]) -> &mut [i32] {
    let  mut zeros = count(list, 0);
    let mut k = 0;
    
    while zeros != 0 {list[k] = 0; zeros = zeros - 1; k = k + 1;}

    while k != list.len() {list[k] = 1; k = k + 1;}
    return list;
    
}

fn main() {
    let mut arr: [i32;8] = [0, 1, 0, 1, 0, 0, 1, 1];
    println!("The new sorted array is {:?}", sort(&mut arr));
}