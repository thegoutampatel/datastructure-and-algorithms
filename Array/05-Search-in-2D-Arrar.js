
const arr = [[1,3,5,7],[10,11,16,20],[23,30,34,60]];

const target = 3;

const Search2DArr = (arr, target) =>{
    const m = arr.length;
    const n = arr[0].length;

    let left = 0;
    let right =  m * n - 1;

    //Binary Tree Implimentation

    while(left <= right){
        
        let mid = Math.floor(left + right / 2);
        let row_num = Math.floor(mid / n);
        let colm_num = mid % n;
        // const mid_element = arrMath.floor([mid/n])[mid%n];
        let mid_element = arr[row_num][colm_num];

        if(target === mid_element){
            return true;
        }
        else if(target < mid_element){
            right = mid - 1;
        }
        else{
            left = mid + 1;
        }
    }

    return false;

}



const result = Search2DArr(arr,target);

console.log(result);