# See: https://www.codewars.com/kata/52b757663a95b11b3d00062d

def weirdcase string
  string.split(' ').map do |word|
    word.split('').each_with_index.map do |item, index|
      index.even? ? item.upcase : item.downcase
    end.join('')
  end.join(' ')
end