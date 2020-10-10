#include<bits/stdc++.h>
using namespace std;

//Creating a graph class
class Graph{
	int V;
	list<int> *adj;
	public:
		Graph(int V);
		void addEdge(int u, int v);
		void BFS(int root);
		void BFSUtil(int s, vector<bool> &v);
		void BFS_stronglyConnected(int s);
		void DFS(int s);
		void DFSUtil(int s, vector<bool> &v);
		void DFS_stronglyConnected(int root);
		void DFS_iterative(int root);
};

 //Create a graph with V number of vertices
Graph::Graph(int V){
	this->V=V;
	this->adj=new list<int>[V];
}

//Adding an edge (u, v) to graph, since graph is undirected so edge is from u to v and vice-versa
void Graph::addEdge(int u, int v)
{
	adj[u].push_back(v);
}

//this function works only when all nodes are reachable from first node
void Graph::DFS_stronglyConnected(int root)
{
	vector<bool> visited(V, false); //a list of all unvisited vertices
	DFSUtil(root, visited);
	cout<<endl;
}

//this function does dfs from given vertex
void Graph::DFSUtil(int root, vector<bool> &visited)
{
	if(visited[root])
		return;
	visited[root]=true; //it current vertex is not visited then mark it as visited
	cout<<root<<" ";
	for(list<int>::iterator it=adj[root].begin();it!=adj[root].end();it++) //check for all adjacent vertices
	{
		if(!visited[*it]) //do DFS on adjacent vertices if and only if they are unvisited
		{
			DFSUtil(*it, visited);
		}
	}
}

//this function is similar to DFS_stronglyConnected just it does DFS for all vertices so it visits every vertex even in case of disconnected graph
void Graph::DFS(int root)
{
	vector<bool> visited(V, false);
	DFSUtil(root, visited);
	cout<<endl;
	for(int i=0;i<V;i++)
	{
		if(!visited[i])
		{
			DFSUtil(i, visited);
			cout<<endl;
		}
	}	
}


//this function does DFS traversal of graph in an iterative manner
void Graph::DFS_iterative(int root)
{
	vector<bool> visited(V, false);
	stack<int> st; //use this stack in same way as function stack
	st.push(root);
	visited[root]=true;
	while(!st.empty())
	{
		root=st.top();
		st.pop();
		cout<<root<<" ";
		for(list<int>::reverse_iterator it=adj[root].rbegin();it!=adj[root].rend();it++)
		{
			if(!visited[*it])
			{
				st.push(*it);
				visited[*it]=true;
			}
		}
	}
}

int main()
{
	Graph g(6); 
    g.addEdge(0, 1); 
    g.addEdge(0, 2); 
    g.addEdge(1, 2); 
    g.addEdge(2, 0); 
    g.addEdge(2, 3);
    g.addEdge(3, 3); 
    g.addEdge(4, 5);
    g.DFS_stronglyConnected(2);
    g.DFS_iterative(2);
	return 0;
}
