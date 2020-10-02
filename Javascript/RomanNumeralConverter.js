function convertToRoman(num) {
  var d=[1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1];
  var r=["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V" ,"IV", "I"];
    var roman="";
    for(var i=0; i<d.length; i++) {
      while(d[i]<=num) 
      {
        roman+=(r[i]);
        num-=d[i];
      }
}
return roman;
}

console.log(convertToRoman(prompt("Enter any number: ")));
