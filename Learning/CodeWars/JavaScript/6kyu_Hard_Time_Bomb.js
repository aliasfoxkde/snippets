// See: https://www.codewars.com/kata/52532cc8e9ea83b89b000008

for(var name in this) {
  if((name.toString()).match(/boom\d/)) {
    Bomb.CutTheWire(this[name]);
  }
}