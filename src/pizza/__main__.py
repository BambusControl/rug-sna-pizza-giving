from data import read_data


def main(
        data_path: str
):
    data = read_data(data_path)
    datapoint = data[0]
    print(datapoint)
    print(datapoint.number_of_downvotes_of_request_at_retrieval)
    print(datapoint.requester_subreddits_at_request[0])


if __name__ == "__main__":
    main("./dataset/pizza_request_dataset.json")
