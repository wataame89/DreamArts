import sys
from collections import defaultdict

def parse_input():
    
    # 標準入力を受け取る
    edges = []
    for line in sys.stdin:
        line = line.strip()
        if line:
            parts = line.split(',')
            start = int(parts[0].strip())
            end = int(parts[1].strip())
            distance = float(parts[2].strip())
            edges.append((start, end, distance))
    return edges

def find_longest_path(edges):
    # グラフ構造を作成
    graph = defaultdict(list)
    for start, end, distance in edges:
        graph[start].append((end, distance))
    
    # 再帰関数の定義
    def search_path(node, current_path, current_distance):
        current_path.append(node)

        longest_path = current_path
        max_distance = current_distance
        
        for neighbor_node, neighbor_distance in graph[node]:
            if neighbor_node not in current_path:
                path, distance = search_path(neighbor_node, current_path, current_distance+neighbor_distance)
                if distance > max_distance:
                    max_distance = distance
                    longest_path = path[:]
        
        return longest_path, max_distance
    
    longest_path = []
    max_distance = 0
    
    # グラフ内のすべてのノードを始点として探索
    for start_node in graph:
        path, distance = search_path(start_node, [], 0)
        if distance > max_distance:
            max_distance = distance
            longest_path = path[:]
        
    return longest_path

if __name__ == "__main__":
    edges = parse_input()
    longest_path = find_longest_path(edges)
    for node in longest_path:
        print(node)

# "cat input.txt |  python cording_test.py" によりシェルから実行可能