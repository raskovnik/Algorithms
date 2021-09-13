fn main() {
    let mut sequence:Vec<i32> = vec![5,6,5,1,5,7,8,1,2,4,6,7,8,9,0];
    quick_sort(&mut sequence);

}

fn quick_sort(sequence: &mut Vec<i32>) {

    let mut items_greater:Vec<i32> = Vec::new();
    let mut less_than:Vec<i32> = Vec::new();

    if sequence.len() <= 1 {
        println!("{:?}", sequence);
    
    }
    else {
        let mut pivot = sequence.remove(sequence.len() - 1);
        println!("pivot : {:?}", pivot);

        for i in sequence.iter() {
            if i > &pivot {
                items_greater.push(*i);
            
            }
            else {
                less_than.push(*i);
            }
        }
        println!("items greater: {:?}, items less: {:?}", items_greater, less_than);
        quick_sort(&mut items_greater);   
        quick_sort(&mut less_than);
    }
    
    
}