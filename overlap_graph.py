
sequences = {}
submission = open("submission_3.txt","w")
with open("fasta files/rosalind_grph.txt","r") as f:
    line = f.readline().strip()
    seqname = line[1:]
    seq = ""
    line = f.readline().strip()
    while line != "":
        if line[0] == ">":
            sequences[seqname] = seq
            seqname = line[1:]
            seq = ""
        else:
            seq += line
        line = f.readline().strip()
    sequences[seqname] = seq

seqnames = list(sequences.keys())



for seqname in seqnames:
    seq = sequences[seqname]
    # for k in range(len(seq),int(len(seq)/2),-1):
    for k in [3]:
        for nextseqname in seqnames:
            nextseq = sequences[nextseqname]
            if seq == nextseq:
                continue
            if seq[-k:] == nextseq[:k]:
                submission.write("{},{},{}\n".format(seqname,nextseqname,k))
            elif seq[:k] == nextseq[-k:]:
                submission.write("{},{},{}\n".format(nextseqname,seqname,k))


