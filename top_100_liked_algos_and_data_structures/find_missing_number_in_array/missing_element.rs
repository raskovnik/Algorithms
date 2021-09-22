fn missing_element(list: &[i32]) -> i32 {
    let n = list.len() as i32;
    let total: i32 = list.iter().sum();

    return (n + 1) + n *(n + 1) / 2 - total;
}

fn main() {
    let arr: [i32;5] = [3, 2, 4, 6, 1];
    println!("The missing element is {}", missing_element(&arr))
}