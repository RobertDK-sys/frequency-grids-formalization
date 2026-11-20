"""Reproducible fixed-construction checks; requires mpmath."""
import mpmath as mp
mp.mp.dps = 60
L = mp.log(2)
Delta = 2*mp.pi/L

def alpha(t):
    def f(u):
        return u*u - 24*t*t*(1-u)**2*(1+3*u*u-u**3)
    lo, hi = mp.mpf(0), mp.mpf(1)
    # Bisection selects the unique root whose existence is assumed in the question.
    for _ in range(220):
        mid = (lo+hi)/2
        if f(mid) > 0:
            hi = mid
        else:
            lo = mid
    u = (lo+hi)/2
    return mp.asin(mp.sqrt(u))

G = list(map(mp.mpf, [
    '14.134725141734693790',
    '21.022039638771554993',
    '25.010857580145688763',
    '30.424876125859513210',
    '32.935061587739189691']))

print('Delta =',mp.nstr(Delta,30))
print('slopes for M=100: distinct =',mp.nstr(100*L/mp.pi,25),
      'ordered absolute =',mp.nstr(200*L/mp.pi,25))
bands = []
for j in range(1,6):
    bands.extend([(j,'-',(2*mp.pi*j-mp.pi/2)/L,(2*mp.pi*j-mp.pi/3)/L),
                  (j,'+',(2*mp.pi*j+mp.pi/3)/L,(2*mp.pi*j+mp.pi/2)/L)])
for n,g in enumerate(G,1):
    nearest = min((min(abs(g-a),abs(g-b)),a,b,j,s) for j,s,a,b in bands)
    inside = [(j,s) for j,s,a,b in bands if a <= g <= b]
    d,a,b,j,s = nearest
    print('envelope gamma',n,'inside',inside,'nearest band',j,s,
          'endpoint',mp.nstr(a if d == abs(g-a) else b,25),
          'distance',mp.nstr(d,25))

for M in (100,589):
    A = [alpha(t) for t in range(1,M+1)]
    print('M =',M,'alpha_1 =',mp.nstr(A[0],25),'alpha_M =',mp.nstr(A[-1],25))
    for g in G:
        best = None
        for t,a in enumerate(A,1):
            phi = a/L
            for j in range(max(1,int(g/Delta)-2),int(g/Delta)+4):
                for eps in (-1,1):
                    x = j*Delta + eps*phi
                    cand = (abs(g-x),t,j,eps,x)
                    if best is None or cand[0] < best[0]: best = cand
        d,t,j,eps,x = best
        print('gamma',mp.nstr(g,18),'nearest |b|',mp.nstr(x,25),
              'distance',mp.nstr(d,18),'t',t,'j',j,'eps',eps)
