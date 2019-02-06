/*
 * Programming Quiz - Checking Your Balance (3-5)
 */

// change the values of `balance`, `checkBalance`, and `isActive` to test your code
var balance = 325.00;
var checkBalance = true;
var isActive = false;

// your code goes here
if(checkBalance === true && isActive === false){
    console.log("Your account is no longer active.");
}else if(checkBalance === true && isActive === true && balance > 0){
    console.log("Your balance is: " + balance.toFixed(2));
}else if(checkBalance === true && isActive === true && balance <= 0){
    console.log("You have no funds. Sorry!");
}else{
    console.log("Exit?");
}