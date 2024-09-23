function clearAll() {
  document.getElementById("display").value = " ";
}
function appendNum(num) {
  document.getElementById("display").value += num;
}
function appendOp(op) {
  document.getElementById("display").value += op;
}
function calculate() {
  const display = document.getElementById("display");
  display.value = eval(display.value);
}
