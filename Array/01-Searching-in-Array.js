const arr = [10, 20, 30, 40, 50, 60];
let found = false;

for (let i = 0; i < arr.length; i++) {
    if (arr[i] === 50) {
        console.log(arr[i]);
        found = true;
        break;
    }
}

if (!found) {
    console.log("not found");
}
