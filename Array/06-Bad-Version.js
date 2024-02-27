
// const arr = [0,0,0,1,1,1,1,1];

// const BadVersion = (arr) => {

//     for(let i=0; i<arr.length; i++){
//         if(arr[i] === 1){
//             return i;
//             break;
//         }
//     }
// }

const  arr = [0,0,0,1,1,1,1,1];
const BadVersion = (arr) => {
    let i = 0;
    let j = arr.length - 1;
    let mid = i + Math.floor((j-i)/2);

    while(i<j){
        if(arr[mid] === 1){
             j = mid;
        }else{
            i = mid + 1;
        }
    }

    return i;
}

let result = BadVersion(arr);
console.log("Since the Bad Version Comes from : " + result);