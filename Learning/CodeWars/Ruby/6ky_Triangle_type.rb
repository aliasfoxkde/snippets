# See: https://www.codewars.com/kata/53907ac3cd51b69f790006c5

def triangle_type (a, b, c)
  x, y, z = [a,b,c].sort
  return 0 if x + y <= z
  return 2 if x*x + y*y == z*z
  if x*x+ y*y < z*z; return 3; else return 1 end
end