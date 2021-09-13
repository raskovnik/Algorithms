fn main() {
    let mut sequence:[i32;7] = [9,4,6,7,8,4,3];
    for j in 1..sequence.len() {
        let mut i = j;

        while i > 0 && sequence[i - 1] > sequence[i] {
            sequence.swap(i, i - 1);
            i -= 1;
            
        }
    }
    println!("{:?}", sequence);
}
