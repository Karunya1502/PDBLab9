
 
class parse_fastfile: 
    
    def __init__(self,id, seq, filepath) :
        self._id = id
        self._seq = seq.upper()
        self._filepath = filepath
    
    @property
    def id(self):
        return self._id 
    
        # getter and setter for seq
    @property
    def seq(self):
        return self._seq
    @property    
    def filepath(self):
        return self._filepath
    
    def get_record(self) : 
        
        with open(self.filepath) as Input : 
            for line in Input : 
                if line.startswith('>') : 
                   line = line.lstrip('>')
                   line = line.rstrip('\n')
                   id = line
                   seq = Input.readline().rstrip() 
                   yield id,seq
                   
                             



