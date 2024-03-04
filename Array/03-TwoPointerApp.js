// if we have an arry of n number of elements 
// so we have to find out the a+b = 210 
// and the a and b are the two elements of that arry
// so we have to find out the output 
// in very less time complexity so we can going with two pointer approch
//G: We don't use recursion in this question

const arr = [20,40,60,80,90,120,240];

const sum_value = 100;

const TwoPonter = (arr,sum_value) =>{

    let l = 0;
    let r = arr.length - 1;     

    while(l<=r){

        // console.log(arr[r] + arr[l]);

        if((arr[l]+ arr[r]) == sum_value){
            return [l,r];
        }
        else if((arr[l]+ arr[r] > sum_value)){
            // return TwoPonter(arr,l,r-1,sum_value);
            r = r - 1;
        }
        else{
            // return TwoPonter(arr,l+1,r,sum_value);
            l = l + 1;
        }
    }
    return -1, -1;
}

console.log(TwoPonter(arr,sum_value));



// const arr = [20, 40, 60, 80, 9, 120, 240];
// const sum_value = 210;

// const TwoPonter = (arr, sum_value) => {
//     let l = 0;
//     let r = arr.length - 1;

//     while (l < r) {
//         const current_sum = arr[l] + arr[r];

//         console.log(current_sum);

//         if (current_sum === sum_value) {
//             return [arr[l], arr[r]];
//         } else if (current_sum < sum_value) {
//             // Move left pointer (l) forward to increase sum
//             l++;
//         } else { // current_sum > sum_value
//             // Move right pointer (r) backward to decrease sum
//             r--;
//         }
//     }

//     return []; // No elements found if loop completes
// };

// console.log(TwoPonter(arr, sum_value));
