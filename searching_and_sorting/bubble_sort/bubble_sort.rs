fn main() {
    let mut sequence:[i32;7] = [9,4,6,7,8,4,3];

    for i in 0..sequence.len() {
        for j in (i + 1..sequence.len()).rev() {
            if sequence[j] < sequence[j - 1] {
                sequence.swap(j, j - 1);
            }
        }
    }
    println!("{:?}", sequence);
}
