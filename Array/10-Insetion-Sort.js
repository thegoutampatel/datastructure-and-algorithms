const arr = [75,90,100,95,85,80];

const InsertionSort = (arr) =>{
    
    for(let i = 1; i < arr.length; i++){
        let key = arr[i];
        let j;
        
        for(j = i - 1; j>=0 && arr[j] > key; j--){
            arr[j + 1] = arr[j];
        }
        arr[j + 1] = key;
    }

    return arr;
}
console.log(InsertionSort([75,90,100,95,85,80]));