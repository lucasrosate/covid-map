/**
 * It returns a object with red, green and blue.
 * @param {string} color - The color variable must be 'rgb(red, blue, green)' format.
 */
function getRgb(color: string) {
  const regex = /\d{1,3},\d{1,3},\d{1,3}/;
  let matches = regex.exec(color.replace(/\s/g, ""))[0].split(",");

  return [
    parseInt(matches[0], 10),
    parseInt(matches[1], 10),
    parseInt(matches[2], 10)
  ];
}
/**
 * It returns a object with red, green and blue.
 * @param {string} color - The color variable must be '#ffffff' format.
 */
function getRgbFromHex(color: string) {
  if (color.length !== 7)
    return [0, 0, 0];

  return [
    parseInt(color.slice(1, 3), 16),
    parseInt(color.slice(3, 5), 16),
    parseInt(color.slice(5), 16)
  ];
}

/**
 * Generate a random color based on another color.
 * @param {*} rgbValues - receives an array with r,g,b values, they must be numbers
 * @param {*} deviation - percentage deviation from original color. If empty the value will be 0.5
 */
function generateRandomColor(rgbValues: number[], deviation = 0.5) {
  let random = Math.random();
  let delta = 1 - deviation;

  let min = delta * rgbValues[0];
  let max = rgbValues[0];

  let r = Math.trunc(random * (max - min) + min)
    .toString(16)
    .padStart(2, "0");

  min = delta * rgbValues[1];
  max = rgbValues[1];

  let g = Math.trunc(random * (max - min) + min)
    .toString(16)
    .padStart(2, "0");

  min = delta * rgbValues[2];
  max = rgbValues[2];
  let b = Math.trunc(random * (max - min) + min)
    .toString(16)
    .padStart(2, "0");

  return "#" + r + g + b;
}

/**
 * Generates an array with random color but based on a pallette.
 * @param {string} color - Variable that will be used as reference.
 * @param {number} arrColorLength - Array output length. Let this field empty implies the output to be 1.
 */
export default function getRandomColors(color: string, arrColorLength = 1, deviation = 0.5) {
  let rgbValues;

  if (color.startsWith("#")) {
    rgbValues = getRgbFromHex(color);
  } else if (color.startsWith("rgb")) {
    rgbValues = getRgb(color);
  } else {
    throw Error("wrong Pattern. The color must be hex or rgb");
  }

  let randomColors = [];

  for (let i = 0; i < arrColorLength; i++)
    randomColors.push(generateRandomColor(rgbValues, deviation));

  return randomColors;
}