fn levenshtein(x: String, y: String) -> i32 {
    let (m, n, mut cost) = (x.len(), y.len(), 0);
    if m == 0 {return n as i32}
    if n == 0 {return m as i32}

    for i in 0..n {
        if i == n-1 {
            cost += ((m - n) as i32).abs();
            return cost;
        }
        if x.chars().nth(i).unwrap() != y.chars().nth(i).unwrap() {cost += 1}
    }
    return cost;

}

fn main() {

    let y = String::from("kafkjahdfkjhakjdshfksdfkjhasdkjfskahfkjsadkfjhaskdhfhajkfvakhdghasdfauhuiawrhbduabudfajfdnaiuwedhbfnwadiuhbfnkaergfuhbjnadsfhvbhjwadkfjvj");
    let x = String::from("faljkdkjdafhhiusahdjfkadhfkjhadjhfiuahsduifjakljhakdhfkjhajwioendkajsdnjlfiwheadfhakjdfhakjhhajdhfjkahdkfhakdfhakjhdfhakjdfahdf");

    println!("{}", levenshtein(y, x));
}