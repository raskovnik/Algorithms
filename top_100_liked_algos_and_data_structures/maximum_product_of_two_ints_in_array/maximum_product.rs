fn sort(list: &mut[i32]) {
    for i in 0..list.len() {
        let mut small = i;
        for j in (i + 1)..list.len() {
            if list[j] < list[small] {
                small = j;
            }
        }

        list.swap(small, i);
    }
}

fn find_max(arr: &mut [i32]) {
    sort(arr);
    let n = arr.len();

    if (arr[0] * arr[1]) > (arr[n - 1] * arr[n - 2]) {
        println!("The pair is {} and {}", arr[0], arr[1]);
    } else {println!("The pair is {} and {}", arr[n - 1], arr[n -2])};
}

fn main() {
    let mut arr: [i32;5] = [-10, -3, 5, 6, -20];
    find_max(&mut arr);
}