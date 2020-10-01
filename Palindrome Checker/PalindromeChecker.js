function palindrome(str) {
  var rev=str.toLowerCase().replace(/[\W_]/g, "").split("").reverse().join("");
  return rev==str.replace(/[\W_]/g, "").toLowerCase();
}



console.log(palindrome(prompt("Enter a string")));
