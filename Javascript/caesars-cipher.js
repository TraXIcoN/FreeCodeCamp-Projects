function rot13(str) {
  var result = "";
  const alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  const alphaShift = alphabet.substring(13) + alphabet.substring(0,13);

  for (var char = 0; char < str.length; char++) {
    if (alphabet.indexOf(str[char]) != -1) {
      var getIndex = alphaShift.indexOf(str[char]);
      result += alphabet[getIndex];
    } else {
      result += str[char];
    }
  }

  return result;
}

rot13("SERR PBQR PNZC");