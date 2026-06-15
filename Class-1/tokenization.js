/**npm init-y
npm install js-tiktoken */

import { getEncoding } from "js-tiktoken";
// Load tokenizer
const enc = getEncoding("cl100k_base");

// Original text
const text = "cat sat on the mat";

// Encode
const tokenIds = enc.encode(text);

console.log("Original Text:", text);
console.log("Encoded Token IDs:", tokenIds);

// Decode
const decodedText = enc.decode(tokenIds);

console.log("Decoded Text:", decodedText);