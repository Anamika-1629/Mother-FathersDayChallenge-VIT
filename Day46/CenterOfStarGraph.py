class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        if edges[0][0] == edges[1][0] or edges[0][0] == edges[1][1]:
            return edges[0][0]
        else:
            return edges[0][1]

def main():
    print("--- 1791. Find Center of Star Graph (Python) ---")
    
    try:
        num_edges = int(input("Enter the number of edges (N-1): "))
    except ValueError:
        print("Invalid number of edges.")
        return

    edges = []
    print("Enter the edges, one pair per line (e.g., 1 2):")

    for i in range(num_edges):
        try:
            edge_input = input(f"Edge {i + 1}: ").split()
            u = int(edge_input[0])
            v = int(edge_input[1])
            edges.append([u, v])
        except (IndexError, ValueError):
            print("Invalid edge input. Please enter two space-separated integers.")
            return

    solution = Solution()
    center = solution.findCenter(edges)

    print(f"\nInput Edges: {edges}")
    print(f"Output (Center Node): {center}")

if __name__ == "__main__":
    main()