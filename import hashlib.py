import hashlib
hashlib.algorithms_guaranteed
hashlib.algorithms_guaranteed
x=hashlib.algorithms_guaranteed
print(x)
class toping:

    def main(self,text,typehash):
        self.text=text
        self.typehash=typehash
        x=hashlib.new(self.typehash)
       #text=text.incoder("utf-8")
        x.update(text)
        print(x.hexdigest())
y=toping() 
y.main(b"rabeh","sha3_224")
