BAS = ord( 'a' )
################################################################
def off(  ch ): return ord( ch ) - BAS
def cha( off ): return chr(  off + BAS )
################################################################
# Trie 01: 698 / 1102 Time Limit Exceeded
# Trie 02: 256 / 1102 ( After optimization )
# Trie 03: 320 / 1102 Ok let's check the Hint
# Trie 04: 721 / 1102 One last time, before that
################################################################
################################################################
class Trie: #                                     retrieval tree
    # Topological sorting stuff
    succ = None
    pred = None
################################################################
################################################################
def relate( s, t ):
    j = 0
    try:
        while s[j] == t[j]: j += 1
        Trie.succ[ off( s[j] )].add( off( t[j] ))
        Trie.pred[ off( t[j] )].add( off( s[j] ))
    except IndexError: pass
################################################################
################################################################
class Solution:
    def findOrder( self, dict, n, k ): # in this chaos
        Trie.succ = [ set() for j in range( k )]
        Trie.pred = [ set() for j in range( k )]
        for j in range( 1, len( dict )):
            relate( dict[ j - 1 ], dict[ j ])
        return topsort()
###############################################################=
def topsort():
    """ Knuth """
    lst = []
    que = []
    cunt = list( map( len, Trie.pred ))
    for j, c in enumerate( cunt ):
        if not c: que.append( j )
    while len( que ) > 0:
        j = que.pop()
        lst.append( cha( j ))
        for i in Trie.succ[ j ]:
            cunt[ i ] -= 1
            if not cunt[ i ]: que.append( i )
    return "".join( lst )
###############################################################_
