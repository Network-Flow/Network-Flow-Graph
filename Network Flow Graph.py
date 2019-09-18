Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class DirectedGraph:
     
    linkCount = 0
     
    class Node:
        def __init__( self, data ):
            self.data = data
            self.links = []
            self.visited = False
        def pointsTo( self, node ):
            self.links.append( node )
            DirectedGraph.linkCount += 1
     
    def __init__( self ):
        self.nodes = []
        self.nodeCount = 0
    def unvisit( self ):
        for node in self.nodes:
            node.visited = False
    def newNode( self, data ):
        node = self.Node( data )
        self.nodes.append( node )
        self.nodeCount += 1
        return node
    def search( self, node, method ):
        self.unvisit()
        # `data` is short for `data structure`
        data = [ node ]
        while True:
            if len( data ) == 0:
                break
            # treat `data` as a stack
            if method == "depth first":
                node = data.pop()
            # treat `data` as a queue
            elif method == "breadth first":
                node = data.pop(0)
            if node.visited == True:
                continue
            node.visited = True
            print "visiting {}".format( node.data )
            for link in node.links:
                data.append( link )
    def depthFirstSearch( self, node ):
        self.search( node, "depth first" )
    def breadthFirstSearch( self, node ):
        self.search( node, "breadth first" )
    def __repr__( self ):
        result = ""
        for node in self.nodes:
            for link in node.links:
                result += "{0} --> {1}\n".format( node.data, link.data )
        return result
