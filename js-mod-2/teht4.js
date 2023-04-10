//Write a program that asks the user for numbers until he gives zero.
//The given numbers are printed in the console from the largest to the smallest. (2p)

let numbers = []

while(true){
    let luku = prompt("syötä numero: (0 ohjelma pysäytetään)")
    if (luku == 0){
        break;
    }else{
        numbers.push(parseInt(luku))
    }
}

numbers.sort((a,b) => b-a);

console.log(numbers)