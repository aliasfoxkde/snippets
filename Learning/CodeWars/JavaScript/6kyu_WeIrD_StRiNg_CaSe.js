// See: https://www.codewars.com/kata/52b757663a95b11b3d00062d

const toWeirdCase = function (string){
  return string.toLowerCase().split(' ').map(mapWord).join(' ');
};

const mapWord = function (word) {
  return word.split('').map(mapCharacter).join('');
};

const mapCharacter = function (letter, index) {
  return (index%2 === 0) ? letter.toUpperCase() : letter;
};