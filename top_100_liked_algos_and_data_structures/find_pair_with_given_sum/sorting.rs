fn sort(list: &mut[i64]) {
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

fn find_pair(list: &mut[i64], target: i64) -> (i64, i64) {
    sort(list);
    let mut high = list.len() - 1;
    let mut low = 0;

    while low < high {
        if list[low] + list[high] == target {
            return (list[low], list[high]);
        }

        if list[low] + list[high] < target {low = low + 1;}
        else {high = high - 1;}
    }

    return (0, 0);
}

fn main() {
    let mut list = vec![1, 2, 45, 6, 7, 3,47, 8, 3, 5, 8, 3, 6, 8, 3];
    let result = find_pair(&mut list, 10);
    println!("{:?}", result);

}