
class Sequence: 
    
    def __init__(self, id, seq) : 
        self._id = id
        self._seq = seq.upper()

    def __len__(self) : 
        return int(len(self.seq))
    
    def __str__(self) :
        return f'ID: {self.id}, Sequence: {self.seq}'
    
    def __iter__(self) : 
        return print(self.__iter__)

        
    @property
    def id(self):
        return self._id 
    
        # getter and setter for seq
    @property
    def seq(self):
        return self._seq

    def write_fasta (self) : 
        return f'>{self.id}\n{self.seq}\n'
         
    
    


class DNASequence(Sequence):

    
    # gc content method
    def calc_gc_content(self, dp=2):
        c_count = self.seq.count('C')
        g_count = self.seq.count('G')
        gc_content = (c_count + g_count) / len(self.seq)
        return round(gc_content, dp)

    def translation(self) : 
        translate = ''
        bases = "tcag".upper()
        codons = [a + b + c for a in bases for b in bases for c in bases]
        amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
        codon_table = dict(zip(codons, amino_acids))
        for num in range(0,len(self.seq),3) : 
            codon = (self.seq[num:num+3])
            aa = codon_table[codon]
            translate += aa 
        return translate
    
    def get_Protein_len(self) : 
        return len(self.seq)//3
    
  

class ProteinSequence(Sequence) : 
    #Task2 
    
       
    def cal_hydrophobic(self, dp=2) :
        hydrophobic = 0
        for amino_acid in 'AILMFWYV' : 
            if amino_acid in self.seq : 
                hydrophobic += self.seq.count(amino_acid)
            hydrophobic_content = hydrophobic/len(self.seq)
        return round(hydrophobic_content,dp)
    
    def get_Protein_len(self) : 
        return len(self.seq)


   
    

                             



