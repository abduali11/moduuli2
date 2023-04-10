function rollDice(numSides) {
  let rollList = [];
  let maxNum = parseInt(prompt("Enter the maximum number on the dice:"));

  while (true) {
    let roll = Math.floor(Math.random() * numSides) + 1;
    console.log(roll);
    rollList.push(roll);

    let html ="";
    for(let i=0; i<rollList.length; i++){
      html += "<li>" + rollList[i] + "</li>"
    }
    document.getElementById("rollist").innerHTML = html;

    if (roll === maxNum) {
      console.log("You rolled the maximum number!");
      break;
    }
  }
}
rollDice(12)
