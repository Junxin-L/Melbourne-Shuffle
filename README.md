# Melbourne Shuffle Implementation in Python

This repository contains a Python implementation of the Melbourne Shuffle, a technique for improving oblivious storage in the cloud, as described in the paper "The Melbourne Shuffle: Improving Oblivious Storage in the Cloud" by K. G. Paterson, E. Shi, and J. Spencer.

## What is the Melbourne Shuffle?

The Melbourne Shuffle is a technique for improving oblivious storage in the cloud, which allows a client to store data on an untrusted server in a way that the server cannot learn anything about the data. Oblivious storage is important because it allows users to store sensitive data in the cloud without worrying about unauthorized access or data leaks.

The Melbourne Shuffle is a shuffle-based construction that uses a combination of encryption and permutation to achieve oblivious storage. In particular, it uses a permutation-based approach to protect the access pattern of the client and an encryption-based approach to protect the contents of the data.

## Implementation Details

The Python implementation of the Melbourne Shuffle in this repository is based on the pseudocode provided in the paper. The implementation uses the PyCryptodome library for the cryptographic operations.

The code is organized as follows:

- `melbourne_shuffle.py`: contains the main implementation of the Melbourne Shuffle algorithm.
- `utils.py`: contains helper functions used by the main implementation.
- `test_melbourne_shuffle.py`: contains unit tests for the implementation.

## Getting Started

You can run the unit tests to ensure that everything is working correctly:

```css
python test_melbourne_shuffle.py
```

If the tests pass, you can then run the Melbourne Shuffle algorithm for your task.

## References

- Paterson, K. G., Shi, E., & Spencer, J. (2015). The Melbourne Shuffle: Improving Oblivious Storage in the Cloud. In Advances in Cryptology – EUROCRYPT 2015 (pp. 285-314). Springer, Berlin, Heidelberg.
