pi =  3.141592653589793

def sin(opp, hyp):
    sin = opp / hyp 
    return sin 

def cos(adj, hyp):
    cos = adj / hyp 
    return cos 

def tan(opp, adj):
    tan = opp / adj 
    return tan 

def csc(hyp, opp):
    csc = hyp / opp
    return csc 

def sec(hyp, adj):
    sec = hyp / adj
    return sec  

def cot(adj, opp):
    cot = adj / opp
    return cot 

def sinθ(angle):
    sinAngle = angle / 60 # approx
    return sinAngle

def tsinθ(angle):
    tsinAngle = 40 * (180-angle) / (40500-angle)*(180-angle ) # approx
    return tsinAngle 


print(tan(8,8.6))
print(cot(28,21)) 
print(sin(2.12,3))

print(sinθ(30)) 
print(tsinθ(30))