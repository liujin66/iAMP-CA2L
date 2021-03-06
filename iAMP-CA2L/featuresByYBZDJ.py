from Bio import SeqIO
import cv2
from PIL import Image
import numpy as np
def seq2bin(seq_str):
    dict = {'P': '00001',
            'Q': '00100',
            'R': '00110',
            'Y': '01100',
            'W': '01110',
            'T': '10000',
            'M': '10011',
            'N': '10101',
            'V': '11010',
            'E': '11101',
            'L': '00011',
            'H': '00101',
            'S': '01001',
            'F': '01011',
            'C': '01111',
            'I': '10010',
            'K': '10100',
            'A': '11001',
            'D': '11100',
            'G': '11110',
            'end': '11111'}
    seq =list(seq_str)
    bin_=''
    for j in range(len(seq)):
        stra=str(dict[seq[j]])
        bin_ = bin_ + stra
    bin_info = bin_
    return bin_info

def Cellular_Automata(str_bit,Rule_number):
    rule_nb = ['111','110','101','100','011','010','001','000']
    rule_number  = Rule_number 
    rule_number_bit  = str('{:08b}'.format(rule_number))
    rule_cond =list(rule_number_bit)
    xs=str_bit
    ab=xs[len(xs)-1]+xs+xs[0]
    new_ab=''
    for k in range(len(ab)-2):
        nb = ab[k:k+3]
        index_= rule_nb.index(nb)
        rule_bit = rule_cond[index_]
        new_ab = new_ab + rule_bit
    return new_ab

def Bin2Cellauto(Bin_info,Epochs,Rule_number):
    rule_number  = Rule_number
    bin_info = Bin_info
    epoch=Epochs
    t = 0
    XS=np.zeros(shape=(epoch+1,len(bin_info)), dtype=np.int16)
    cellauto_bin=bin_info
    XS[0]=list(bin_info)
    kkk = 0
    for j in range(epoch):
        cellauto_bin = Cellular_Automata(cellauto_bin,rule_number)
        result = list(cellauto_bin)   
        results = np.array(result, dtype=np.int16)
        XS[j+1]=results
        if j%1000 == 0:
            kkk += 1
            print(kkk)
    return XS

def CA_Img(rule_numbers,epoch):
    result = 0
    for seq_record in SeqIO.parse("static/upload/new_test.fasta", "fasta"):
        seq = str(seq_record.seq)
        bin_info = seq2bin(seq)
        CA = Bin2Cellauto(bin_info,epoch,rule_numbers)
        BBB = CA*255
        BBBB = cv2.resize(BBB, (100,10),Image.ANTIALIAS)
        result = BBBB / 255
    return result

if __name__ == '__main__':
    rule_numbers =184
    epochs = [25]
    file_list = ['Wuhan']
    for epoch in epochs:
        for i in file_list:
            CA_Img(i,rule_numbers)

