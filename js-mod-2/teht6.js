//Write a function that returns a random dice roll between 1 and 6.
// The function should not have any parameters.
// Write a main program that rolls the dice until the result is 6.
// The main program should print out the result of each roll in an unordered list (<ul>). (2p)

function rolldice() {
    let rullaa6 = false;
    let rollList = [];
    while (!rullaa6) {
        let rullaa = Math.floor(Math.random() * 6) + 1;
        console.log(rullaa);
        rollList.push(rullaa)
        if (rullaa === 6) (rullaa6 = true);

        let html =""
        for(let i=0; i<rollList.length; i++){
            html += "<li>" + rollList[i] + "</li>"
        }
        document.getElementById("rollist").innerHTML = html;
    }
}
rolldice()