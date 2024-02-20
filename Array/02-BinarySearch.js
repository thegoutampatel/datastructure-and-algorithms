

// let arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20];
// let s = 0;
// let l = arr.length;

// const x = 9;

// const BinaryS = (arr,s,l,x)=>{
    
//     // let r = l - 1;     //defined the right boundary
    
//     while(s<=l){
        
//         const mid = s + Math.floor((l-s)/2);

//         if(arr[mid]==x){
//             return mid;
//         }
//         else if(arr[mid] < x){
//             s = mid + 1;
//         }
//         else{
//             l = mid - 1;
//         }
//     }

//     return -1;
// }

// console.log(BinaryS(arr,s,l,x));



let arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20];

const i = 0;
const j = arr.length - 1;
const x = 15;

const BinaryS = (arr, i, j, x) =>{
    
    while(i<=j){
        const mid = i + Math.floor((j-i)/2);
        
        if(arr[mid]==x){
            return mid;
        }else if(arr[mid] < x){

            //Right side of mid 
            // Search space: mid+1 to J
            //use the Recursion : calling same function inside the method defination
            return BinaryS(arr, mid+1 , j, x);
        }else{
            //left side of mid 
            // Search space: i to mid-1

            return BinaryS(arr , i, mid-1 ,x)
        }
    }
    return -1;
}



console.log("Searching location of the present element at : " + BinaryS(arr, i, j, x));