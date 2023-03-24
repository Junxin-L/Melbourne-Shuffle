#!/usr/local/bin/python3
# coding=utf-8
from math import sqrt
import random
from multiprocessing import Queue
import base64
from Crypto.Cipher import AES
# default config parameter


MAX = 10000

blockNumber = 25
k_new = "fhakghfjgwqufjndmnvkjk"
k_pre = "dfjhfkjahkfjfaffffaf"

block_list = ['000', '111', '222', '333', '444', '555', '666', '777', '888', '999']

bucket_size = int(sqrt(len(block_list)))
dummy_size = bucket_size


def generate_each_random_block(blocksize=32):
    '''
    Generate a random block.
    :param blocksize: the length of a block, default 1M
    :return key, type of string
    '''

    str = ''
    base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
    length = len(base_str) - 1
    for i in range(blocksize):
        str += base_str[random.randint(0, length)]
    return str


def generate_random_block(self, blocksize=32):
    '''
    Randomize the block list.
    :param blocksize: the length of a block, default 1M
    :return: None
    '''
    self.block_list = [self.generate_each_random_block(blocksize) for _ in range(self.blockNumber)]
    self.bucket_size = int(sqrt(len(self.block_list)))
    self.dummy_size = self.bucket_size


def generate_random_key(randomlength=16):
    '''
    Generate a random key.
    :param randomlength: the length of key, default 16-length
    :return key, type of string
    '''

    str = ''
    base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
    length = len(base_str) - 1
    for i in range(randomlength):
        str += base_str[random.randint(0, length)]
    return str


def aes_encrypt(message, key):
    '''
    Aes encryption for each slice.
    :param message:
    :param key:
    :return: ciphertext
    '''
    key = key.encode('utf-8')
    key = key[:16]
    message = message.encode('utf-8')
    message = message + b"\0" * (16 - len(message) % 16)
    des = AES.new(key, AES.MODE_ECB)
    ciphertext = des.encrypt(message)
    return base64.b64encode(ciphertext).decode()


def aes_decrypt(ciphertext, key):
    '''
    Aes decryption for each slice.
    :param ciphertext:
    :param key:
    :return: plaintext
    '''
    key = key[:16].encode('utf-8')
    ciphertext = base64.b64decode(ciphertext)
    des = AES.new(key, AES.MODE_ECB)
    message = des.decrypt(ciphertext)
    return message.rstrip(b"\0").decode()


def encrypt(k, i):
    '''
    Aes encryption for blocks.
    :param k:
    :param i:
    :return: ciphertext
    '''
    for j in range(len(i)):
        i[j] = aes_encrypt(str(i[j]), k)
    return i


def decrypt(k, i):
    '''
    Aes decryption for blocks.
    :param k:
    :param i:
    :return: plaintext
    '''
    for j in range(len(i)):
        i[j] = aes_decrypt(str(i[j]), k)
    return i
