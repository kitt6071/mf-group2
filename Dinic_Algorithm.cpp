#include <iostream>
#include <vector>
#include <queue>
#include <limits>

using namespace std;

class Dinic {
private:
    struct Edge {
        int from, to;
        int flow, capacity;
        Edge(int from, int to, int capacity): from(from), to(to), flow(0), capacity(capacity) {}
    };

    vector<Edge> edges;
    vector<vector<int>> adjList;
    vector<int> level, ptr;
    int n, source, sink;

    bool bfs() {
        // stuff
        return false;
    }

    int dfs(int v, int flow) {
        // stuff
        return 0;
    }

public:
    Dinic(int n, int source, int sink): n(n), source(source), sink(sink) {
        adjList.resize(n);
        level.resize(n);
        ptr.resize(n);
    }

    void addEdge(int from, int to, int cap) {
        // stuff
    }

    int maxFlow() {
        // stuff
        return 0;
    }
};