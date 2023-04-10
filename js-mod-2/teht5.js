//Write a program that prompts the user for numbers.
// When the user enters one of the numbers he previously entered,
// the program will announce that the number has already been given and stops
// its operation and then prints all the given numbers to the console in ascending order.

const numbers = [];

while (true) {
    const luvut = prompt("Syötä luku (lopeta syöttämällä 'sama luku kaksi kertaa '):")
    const sama_luku = parseInt(luvut)
    if(numbers.includes(sama_luku)){
        break;
    }

    numbers.push(sama_luku)
}

numbers.sort((a,b) => a-b);

console.log(numbers)


