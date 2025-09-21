Write a short explanation describing how their solution upholds confidentiality, integrity, and availability

-- this folder includes several common ways to generate encypted data and several ways to ensure data validity.

-- by running main you will have 7 options, Ceasar Chipher text encryption/decryption, RSA encryption/decryption, SHA256 hashes (not optimized but produces the same results as the public library SHA256), data signiture creation/verification.

Explain the role of entropy and key generation in their implementation

-- keys for the Ceasar Cipher are choosen by the user, for RSA the keys are created from 2 prime numbers chosen randomly from any prime between 100 and 1000 and an standard e = 65537, I also fixed several issues including an integer overflow that was making most usage attempts invalid.