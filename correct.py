import queue
from collections import namedtuple

Edge = namedtuple('Edge', ['vertex', 'weight'])

class GraphUndirectedWeighted(object):
    def __init__(self, vertex_count):
        self.vertex_count = vertex_count
        self.adjacency_list = [[] for _ in range(vertex_count)]

    def add_edge(self, source, dest, weight):
        assert source < self.vertex_count
        assert dest < self.vertex_count
        self.adjacency_list[source].append(Edge(dest, weight))
        self.adjacency_list[dest].append(Edge(source, weight))

    def get_edge(self, vertex):
        for e in self.adjacency_list[vertex]:
            yield e

    def get_vertex(self):
        for v in range(self.vertex_count):
            yield v


def dijkstra(graph, source, dest):
    q = queue.PriorityQueue()
    parents = []
    distances = []
    start_weight = float("inf")

    for i in graph.get_vertex():
        weight = start_weight
        if source == i:
            weight = 0
        distances.append(weight)
        parents.append(None)

    q.put(([0, source]))

    while not q.empty():
        v_tuple = q.get()
        v = v_tuple[1]

        for e in graph.get_edge(v):
            candidate_distance = distances[v] + e.weight
            if distances[e.vertex] > candidate_distance:
                distances[e.vertex] = candidate_distance
                parents[e.vertex] = v
                if candidate_distance < -1000:
                    raise Exception("Negative cycle detected")
                q.put(([distances[e.vertex], e.vertex]))

    shortest_path = []
    end = dest
    while end is not None:
        shortest_path.append(end)
        end = parents[end]

    shortest_path.reverse()

    return shortest_path, distances[dest]



vertNames = ['A','B','C', 'D', 'E', 'F', 'G', 'H', 'Z', 'S']
p = dict(zip(vertNames,range(0,10)))
rp = dict(zip(range(0,10),vertNames))

graph = GraphUndirectedWeighted(10)
graph.add_edge(p['A'], p['B'], 40)
graph.add_edge(p['B'], p['C'], 70)
graph.add_edge(p['B'], p['E'], 20)
graph.add_edge(p['C'], p['Z'], 40)
graph.add_edge(p['D'], p['E'], 60)
graph.add_edge(p['E'], p['F'], 100)
graph.add_edge(p['G'], p['F'], 80)
graph.add_edge(p['H'], p['E'], 30)
graph.add_edge(p['H'], p['G'], 90)
graph.add_edge(p['S'], p['A'], 30)
graph.add_edge(p['S'], p['F'], 80)
graph.add_edge(p['S'], p['D'], 100)
graph.add_edge(p['Z'], p['H'], 10)
graph.add_edge(p['E'], p['Z'], 80)


start = p[str(input("Start= ")).upper()]
end =  p[str(input("End= ")).upper()]
#start = p['C']
#end = p['F']
shortest_path, distance = dijkstra(graph, start, end)
print(distance)
path = [rp[i] for i in shortest_path]
print(path)






from PIL import Image,ImageDraw, ImageFont
k = 2
vert = {}
bg = (211,211,211)
lineColor = (0,0,0)

def ellipse(draw, x,y, text,fill=bg):
    x = x + 50
    y = y + 100
    fnt = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', 30)
    draw.ellipse([x-10*k,y-10*k,x+10*k,y+10*k],fill=fill, outline=(0,0,0))
    draw.text((x-10,y-15), text, font=fnt, fill=(0,0,0))
    vert[text] = [x,y]


def line(draw,v1,v2,w,c=lineColor):
    p1 = vert[v1]
    p2 = vert[v2]
    draw.line([*p1,*p2],fill=c)

    mpx = int((p1[0]+p2[0])/2)
    mpy = int((p1[1]+p2[1])/2)
    if w == None:
        return
    fnt = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', 15)
    draw.text((mpx,mpy), str(w), font=fnt, fill=(0,0,0))


def drawEllipses():
    ellipse(draw,0,100,'S')
    ellipse(draw,100,0,'A')
    ellipse(draw,100,100,'D')
    ellipse(draw,100,200,'F')
    ellipse(draw,200,0,'B')
    ellipse(draw,200,100,'E')
    ellipse(draw,200,200,'G')
    ellipse(draw,300,0,'C')
    ellipse(draw,300,100,'Z')
    ellipse(draw,300,200,'H')

im = Image.new("RGB", (430,400), bg)
draw = ImageDraw.Draw(im)
drawEllipses()
line(draw,'A', 'B', 40)
line(draw,'B', 'C', 70)
line(draw,'B', 'E', 20)
line(draw,'C', 'Z', 40)
line(draw,'D', 'E', 60)
line(draw,'E', 'F', 100)
line(draw,'G', 'F', 80)
line(draw,'H', 'E', 30)
line(draw,'H', 'G', 90)
line(draw,'S', 'A', 30)
line(draw,'S', 'F', 80)
line(draw,'S', 'D', 100)
line(draw,'Z', 'H', 10)
line(draw,'E', 'Z', 80)

for i in range(len(path)-1):
    line(draw,path[i],path[i+1],None,c="red")
drawEllipses()
ellipse(draw, vert[rp[start]][0]-50,vert[rp[start]][1]-100, rp[start],"green")
ellipse(draw, vert[rp[end]][0]-50,vert[rp[end]][1]-100, rp[end],"yellow")
fnt = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', 45)
draw.text((130,10), rp[start]+"-"+rp[end]+"="+str(distance), font=fnt, fill=(0,0,0))
im.show()
