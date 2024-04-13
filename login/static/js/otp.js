function limitInputLength(input) {
  if (input.value.length > 5) {
      input.value = input.value.slice(0, 5); // Keep only the first 5 characters
  }
}