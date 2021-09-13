#![allow(unused_mut)]
fn main() {

    let arr: Vec<i32> = vec![0, 1, 1, 2, 4, 5, 5, 5, 6, 6, 7, 7, 8, 8, 9];
    bin_search(arr, 9)
}
fn bin_search(arr: Vec<i32>, number: i32) {
    let (mut start, mut end) = (0, arr.len());

    while start <= end {
        let mut midpoint = start + (end - start) / 2;

        if arr[midpoint] == number {
            println!("{} found at index {}", number, midpoint);
            break;
        }
        else {
            if arr[midpoint] <= number {
                start = midpoint + 1;
            }
            if arr[midpoint] >= number {
                end = midpoint - 1;
            }
        }
        println!("{} not found", number);
    }
}