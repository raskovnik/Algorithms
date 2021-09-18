fn linear_search(list: [i32;7], item: i32) -> bool {
    let (mut index, mut found) = (0, false);
    while index < list.len() && found == false {
        if list[index] == item {
            found = true;
        }
        else{index = index + 1}
    }
    return found;
}

fn linear_search2(list: [i32;7], item: i32) -> bool {
    for c in list.iter() {
        if *c == item {
            return true;
        }
    }
    return false;
}

fn main() {
    let list: [i32;7] = [1, 2, 3, 4, 5, 6, 7];
    let result = linear_search2(list, 5);
    println!("{:?}", result);
}