function validate(num) {
  if (num < 1 || num > 9) {
    console.log('Out of range');
  } else if (num !== parseInt(num)) {
    console.log('Not an integer');
  } else {
    console.log('Just right');
    return true;
  }
  return false;
}

console.log(validate(-5));
console.log(validate(15));
console.log(validate(5.2));
console.log(validate(5));