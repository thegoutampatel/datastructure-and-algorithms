
const arr = [20,25,47,56,63,65,79,82];

const target = 82;
let i = 0;
let j = arr.length - 1;

const TernarySearch = (arr,target,i,j)=>{

    while(i<=j){
        let mid1 = i + Math.floor((j-i)/3);
        let mid2 = j - Math.floor((j-i)/3);
        
         
        if(arr[mid1] === target){
            return mid1;
        }
        if(arr[mid2] === target){
            return mid2;    
        }
        else if(target<arr[mid1]){
            return TernarySearch(arr,target,i,mid1-1);
        }
        else if(target>arr[mid2]){
            return TernarySearch(arr,target,mid2+1,j);
        }
        else{
            return TernarySearch(arr,target,mid1+1,mid2-1);
        }
    }
    return -1;

}


const result = TernarySearch(arr,target,i,j)
console.log(result);