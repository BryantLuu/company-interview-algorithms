const fibWithCounter = () => {
  let count = 0
  const cache = {
    0: 0,
    1: 1,
    2: 1,
  }
  const fib = (n) => {
      if (cache[n]) {
        return cache[n];
      }
      if (n <= 0) {
        return 0
      }
      if (n <= 2) {
        return 1
      }
      cache[n] = fib(n-1) + fib(n-2)
      return cache[n]
  }
  return (n) => {
    count++
    return [fib(n), count]
  }
}

const fibInstance = fibWithCounter()
console.log(fibInstance(0))
console.log(fibInstance(1))
console.log(fibInstance(2))
console.log(fibInstance(3))
console.log(fibInstance(4))
console.log(fibInstance(5))
