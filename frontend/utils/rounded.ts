/**
 * This function manipulates numbers to return the quantity with unit.
 * @param {number} num The number input
 * @returns {string} String
 */
export default function rounded(num: number): string {
    if (num > 1000000000) {
        return Math.round(num / 100000000) / 10 + " Bi";
    } else if (num > 1000000) {
        return Math.round(num / 100000) / 10 + " Mi";
    } else {
        return Math.round(num / 100) / 10 + " K";
    }
};