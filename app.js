// Block copy on right click
document.addEventListener("contextmenu", function (event) {
  event.preventDefault();
});

// Disable text selection
document.addEventListener("selectstart", function (event) {
  event.preventDefault();
});

// Disable drag-and-drop
document.addEventListener("dragstart", function (event) {
  event.preventDefault();
});

document.querySelector("body").style.backgroundColor = "#c0c0c0";
// End of block



function greet() {
  const name = prompt('What is your name?\n');
  const christmasTree = '🎄'; // Christmas tree emoji
  alert(`Happy Christmas! ${christmasTree}\n${name}`);
}

greet();
