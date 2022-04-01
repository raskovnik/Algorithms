fn first_occurrence(list: &[i32], target: i32) -> i32  {
    let (mut left, mut right) = (0, list.len() - 1);
    let mut result: i32 = -1;

    while left <= right {
        let mid = (left + right) / 2;
        if *&list[*&mid] == *&target {
            result = *&mid as i32;
            right = *&mid - 1 as usize;
        } else if *&list[*&mid] < *&target {
            left  = *&mid + 1 as usize;
        } else {
            right = *&mid - 1 as usize;
        }
    }

    return result;
}

fn last_occurrence(list: &[i32], target: i32) -> i32 {
    let (mut left, mut right) = (0, list.len() - 1);
    let mut result: i32 = -1;

    while left <= right {
        let mid = (left + right) / 2;

        if *&list[*&mid] == *&target {
            result = *&mid as i32;
            left = *&mid + 1 as usize;
        }
        else if *&list[*&mid] < *&target {
            right = *&mid - 1 as usize;
        }
        else {
            left = *&mid + 1 as usize;
        }
    }

    return result;
}

fn main() {
    let arr: [i32;13] = [2, 2, 2, 3, 3, 4, 5, 5, 6, 6, 7, 7, 7];
    println!("{}", first_occurrence(&arr, 5));
}