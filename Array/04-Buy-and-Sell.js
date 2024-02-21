 //we have to find the best time to buy and sell the stock
//we have the price in array and this is day by day that 1day = 7 , 2day = 1.......
//Now find the best time to buy and then sell the stock that gain max-Profit



// const price = [7,1,5,3,6,4];

// const BuyandSell = (price) =>{

//     const minprice = Infinity;
//     const max_profit = 0;

//     for(let i = 0 ; i < price.lenth; i++){
//         if (price[i] < minprice){
//             minprice = price[i];
//         }else if(price[i] - minprice  > max_profit){
//             max_profit = price[i] - minprice;
//         }
//     }
//     return max_profit;
// }   

// const maxprofit_Value = BuyandSell(price);
// console.log(maxprofit_Value);



const price = [7, 1, 5, 3, 6, 4];

const BuyandSell = (price) => {

    //intialization
    let minPrice = Infinity;
    let max_profit = 0;

    for (let i = 0; i < price.length; i++) {
        if (price[i] < minPrice) {
            minPrice = price[i];
           
        } else if (price[i] - minPrice > max_profit) {
            max_profit = price[i] - minPrice;
           
        }
    }
    return max_profit;
}

const  max_profit = BuyandSell(price);

console.log(max_profit);

