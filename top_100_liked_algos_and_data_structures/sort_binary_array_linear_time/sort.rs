fn ssort(list: &mut [i32]) {
    let mut k = 0;
    for i in 0..list.len() {
        if *&list[i] == 0 {
            list[k] = 0;
            k+=1;
        }
    }

    for i in k..list.len() {
        list[i] = 1;
    }

    println!("{:?}", list);
}

fn main() {
    let mut arr: [i32;14] = [1, 0, 1, 1,1, 0, 0, 0, 0, 1, 1, 0, 1, 0];
    ssort(&mut arr);
}