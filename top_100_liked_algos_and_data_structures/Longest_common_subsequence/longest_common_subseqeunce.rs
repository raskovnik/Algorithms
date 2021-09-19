use std::cmp;

fn lcs(x: String, y: String, m: &mut usize, n: &mut usize) -> i32 {
    if *m == 0 || *n == 0 {return 0;}
    if x.chars().nth(*m - 1).unwrap()  == y.chars().nth(*n - 1).unwrap() { return lcs((*x).to_string(), (*y).to_string(), &mut (*m - 1), &mut (*n - 1)) + 1;}

    return cmp::max(lcs((*x).to_string(), (*y).to_string(), m, &mut (*n - 1)), lcs(x, y, &mut (*m - 1), n));
}

fn main() {
    let x = "ABCBDAB";
    let y = "BDCABA";
    let mut x_l = x.len();
    let mut y_l = y.len();

    println!("The length of the LCS of {} and {} is {}", &x, &y, lcs((*x).to_string(), (*y).to_string(), &mut x_l, &mut y_l));
}