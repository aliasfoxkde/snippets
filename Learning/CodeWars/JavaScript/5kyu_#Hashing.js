// See: https://www.codewars.com/kata/52ae2db783f47875d0000064

const getHashtags = post => {
  const regex = /\B#+(\w+)(\s|$)/g;
  let output = [], res = '';
  while(res = regex.exec(post)) {
    output.push(res[1]);
  }
  return output;
};