/*
 * Programming Quiz: Murder Mystery (3-4)
 */

// change the value of `room` and `suspect` to test your code
var room = "dining room";
var suspect = "Mr. Parkes";

var weapon = "";
var solved = false;

if (room == "dining room" && suspect == "Mr. Parkes") {
    weapon = "knife";
    solved = true;
} else if (room == "ballroom" && suspect == "Mr. Kalehoff") {
     weapon = "poison";
     solved = true;
} else if (room == "gallery" && suspect == "Ms. Van Cleve") {
    weapon == "trophy";
    solved = true;
} else if (room == "billards room" && suspect == "Mrs. Sparr") {
    weapon = "pool stick";
    solved = true;
}else{
    console.log("You have guessed in correctly!");
}

if (solved) {
    console.log(suspect + " did it in the " + room + " with the " + weapon);
}
