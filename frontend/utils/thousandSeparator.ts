/**
 * 
 * @param {number} value input value
 * @returns {string} String with dot separating it.
 */

export default function thousandSeparator(value: number) {
    return value.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".");
}