/*Accessing elements in the DOM with JS
**You have nodes, the dom an the document to understand
**Tag-token-nodes-DOM
**You can access elements by ID, Class or Tag
*/
//Methods
document.getElementById('id'); //no need for #id
document.getElementsByClassName('class');//
document.getElementsByTagName('tag');
document.querySelector('#id');// to get id
document.querySelectorAll('.class');//gets all classes
document.querySelector('header');// returns first element
//get the first paragragh of a class callout
document.querySelector('p.callout');
//get all of the p elements that are decendants of articles
document.querySelectorAll('.articles p');
//creating elements
document.createElement('p');
// create a brand new <span> element
const newSpan = document.createElement('span');

// select the first (main) heading of the page
const mainHeading = document.querySelector('h1');

// add the the <span> element as the last child element of the main heading
mainHeading.appendChild(newSpan);
//creating text nodes
onst myPara = document.createElement('p');
const textOfParagraph = document.createTextNode('I am the text for the paragraph!');

myPara.appendChild(textOfParagraph);
//Remove  elements
const mainHeading = document.querySelector('h1');

mainHeading.parentElement.removeChild(mainHeading);

const mainHeading = document.querySelector('h1');

mainHeading.remove();

//style pages usising classList
const mainHeading = document.querySelector('#main-heading');

// store the list of classes in a variable
const listOfClasses = mainHeading.classList;
//Methods: .add(), .remove(), .toggle(), .contains()

// logs out ["ank-student", "jpk-modal"]
console.log(listOfClasses);