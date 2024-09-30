import networkx as nx

from data import read_data


def main(
        data_path: str
):
    data = read_data(data_path)

    # use requester_username and giver_username_if_known to create a networkx graph
    g = nx.DiGraph()

    # create a set of usernames for both requester and giver
    usernames = set()
    usernames.add(row.requester_username for row in data)
    usernames.add(row.giver_username_if_known for row in data)

    # delete None values
    usernames.discard(None)

    # add nodes to the graph
    g.add_nodes_from(usernames)

    # add edges between requester and giver
    g.add_edges_from(
        (row.giver_username_if_known, row.requester_username)
        for row in data
        if row.giver_username_if_known is not None
    )

    # print the number of nodes and edges
    print(f"Number of nodes: {g.number_of_nodes()}")
    print(f"Number of edges: {g.number_of_edges()}")


if __name__ == "__main__":
    main("./dataset/pizza_request_dataset.json")
