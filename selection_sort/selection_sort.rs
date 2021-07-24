#![allow(unused_mut)]
fn main() {
    let mut arr: Vec<i32> = vec![5,6,5,1,5,7,8,1,2,4,6,7,8,9,0];

    for i in 0..arr.len() {
        let mut k = i;
        let mut min_index = k;

        for j in i + 1..arr.len() {
            if arr[min_index] >= arr[j] {
                min_index = j;
            }
        }
        if min_index != k {
            arr.swap(min_index, k);
        }
    }
    println!("{:?}", arr);
}
