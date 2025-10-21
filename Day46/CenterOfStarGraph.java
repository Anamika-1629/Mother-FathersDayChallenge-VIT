import java.util.*;

public class CenterOfStarGraph {
    public int findCenter(int[][] edges) {
        if (edges[0][0] == edges[1][0] || edges[0][0] == edges[1][1]) {
            return edges[0][0];
        } else {
            return edges[0][1];
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("--- 1791. Find Center of Star Graph (Java) ---");
        System.out.print("Enter the number of edges (N-1): ");
        int numEdges = scanner.nextInt();
        
        int[][] edges = new int[numEdges][2];
        System.out.println("Enter the edges, one pair per line (e.g., 1 2):");

        for (int i = 0; i < numEdges; i++) {
            System.out.print("Edge " + (i + 1) + ": ");
            edges[i][0] = scanner.nextInt();
            edges[i][1] = scanner.nextInt();
        }

        CenterOfStarGraph solution = new CenterOfStarGraph();
        int center = solution.findCenter(edges);

        System.out.println("\nInput Edges: " + Arrays.deepToString(edges));
        System.out.println("Output (Center Node): " + center);

        scanner.close();
    }
}