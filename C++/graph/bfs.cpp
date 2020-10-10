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


//this one works only when all nodes are reachable from first node
void Graph::BFS_stronglyConnected(int s)
{
	vector<bool> visited(V, false); //a list of all unvisited vertices
	list<int> q; //a queue of add all unvisited vertices
	
	visited[s]=true;
	q.push_back(s);
	while(!q.empty())
	{
		s=q.front();
		cout<<s<<" ";
		q.pop_front();
		list<int>::iterator i;
		for(i=adj[s].begin();i!=adj[s].end();i++)
		{
			if(!visited[*i]) //adding adjacent vertices only if it is unvisited
			{
				visited[*i]=true;
				q.push_back(*i);
			}
		}
		
	}
	cout<<endl;
	return;
}

//this is performing bfs for all vertices(given a vertex is unvisited from previous bfs traversals)
void Graph::BFS(int s)
{
	vector<bool> visited(V, false);
	BFSUtil(s, visited);
	//return;
	for(int i=0;i<V;i++) //iterating for all vertices
		if(visited[i]!=true) //performing bfs only if current vertex has never been visited
		{
			BFSUtil(i, visited);
			cout<<endl;
		}
}

//this is a utility function which performs bfs to a given vertex
void Graph::BFSUtil(int s, vector<bool> &visited)
{
	if(visited[s]==true)
		return;
	list<int> q;
	visited[s]=true;
	q.push_back(s);
	list<int>::iterator it;
	while(!q.empty())
	{
		s=q.front();
		cout<<s<<" ";
		q.pop_front();
		for(it=adj[s].begin();it!=adj[s].end();it++)
		{
			if(!visited[*it])
			{
				visited[*it]=true;
				q.push_back(*it);
			}
		}
	}
}


int main()
{
    //creating an object of graph class
	Graph g(6); 
    g.addEdge(0, 1); 
    g.addEdge(0, 2); 
    g.addEdge(1, 2); 
    g.addEdge(2, 0); 
    g.addEdge(2, 3);
    g.addEdge(3, 3); 
    g.addEdge(4, 5);
    g.BFS_stronglyConnected(2);
	g.BFS(2);
	return 0;
}
