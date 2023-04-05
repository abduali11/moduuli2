//Write a program that asks the user for an integer and tells if the number is a
//prime number. (2p)
//Prime numbers are numbers that are only divisible by 1 and itself.
//For example, number 13 is a prime number as it can only be divided by 1 or 13 so
//that the result is an integer.
//On the other hand, number 21 for example is not a prime number as it can be also
//be divided by numbers 3 and 7.
//Print the result on the HTML document.

let number = prompt("Anna numero");

alkuluku = true

for(let i = 2; i<number;i++){
    if(number%i===0){
        alkuluku = false;
        break;
    }
}

if(alkuluku){
    document.querySelector("#target").innerHTML= number + " luku on alkuluku"
}

else{
    document.querySelector("#target").innerHTML = number + " luku ei ole alkuluku"
}




