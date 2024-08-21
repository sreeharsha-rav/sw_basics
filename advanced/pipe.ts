// Program to demonstrating the concept of piping in TypeScript or JavaScript

type Func<T, R> = (arg: T) => R;    // Define a function type

/**
 * Function to create a pipeline of functions
 * @param fns Array of functions to be executed in sequence
 * @returns A function that takes an input and passes it through the pipeline
 */
function pipe<T>(...fns: Array<Func<any, any>>): Func<T, any> {
  return (x: T) => fns.reduce((v, f) => f(v), x);
}
  
/**
 * Example using strings
 */

// Define our transformation functions
const removeSpaces = (str: string): string => str.replace(/\s/g, '');
const toLowerCase = (str: string): string => str.toLowerCase();
const capitalize = (str: string): string => str.charAt(0).toUpperCase() + str.slice(1);
const addExclamation = (str: string): string => `${str}!`;

// Create our pipeline
const processString = pipe(
  removeSpaces,
  toLowerCase,
  capitalize,
  addExclamation
);

// Use the pipeline
const input = "  HeLLo   WoRLd  ";
const str_result = processString(input);

console.log(str_result);  // Output: "Helloworld!"

// Let's break down the steps:
// 1. Start with "  HeLLo   WoRLd  "
// 2. removeSpaces: "HelloWorld"
// 3. toLowerCase: "helloworld"
// 4. capitalize: "Helloworld"
// 5. addExclamation: "Helloworld!"

/**
 * Another example using numbers
 */

// Define our mathematical operations
const double = (n: number): number => n * 2;
const addTen = (n: number): number => n + 10;
const square = (n: number): number => n * n;

// Create our piped function
const processNumber = pipe(
  double,
  addTen,
  square
);

// Use the piped function
const num_result = processNumber(5);
console.log(num_result);  // Output: 400

// Let's break down the steps:
// 1. Start with 5
// 2. double: 5 * 2 = 10
// 3. addTen: 10 + 10 = 20
// 4. square: 20 * 20 = 400