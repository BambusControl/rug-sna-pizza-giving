from collections import namedtuple
from typing import NamedTuple


class PizzaRequest(NamedTuple):
    giver_username_if_known: str
    in_test_set: bool
    number_of_downvotes_of_request_at_retrieval: int
    number_of_upvotes_of_request_at_retrieval: int
    post_was_edited: bool
    request_id: str
    request_number_of_comments_at_retrieval: int
    request_text: str
    request_text_edit_aware: str
    request_title: str
    requester_account_age_in_days_at_request: float
    requester_account_age_in_days_at_retrieval: float
    requester_days_since_first_post_on_raop_at_request: float
    requester_days_since_first_post_on_raop_at_retrieval: float
    requester_number_of_comments_at_request: int
    requester_number_of_comments_at_retrieval: int
    requester_number_of_comments_in_raop_at_request: int
    requester_number_of_comments_in_raop_at_retrieval: int
    requester_number_of_posts_at_request: int
    requester_number_of_posts_at_retrieval: int
    requester_number_of_posts_on_raop_at_request: int
    requester_number_of_posts_on_raop_at_retrieval: int
    requester_number_of_subreddits_at_request: int
    requester_received_pizza: bool
    requester_subreddits_at_request: list[str]
    requester_upvotes_minus_downvotes_at_request: int
    requester_upvotes_minus_downvotes_at_retrieval: int
    requester_upvotes_plus_downvotes_at_request: int
    requester_upvotes_plus_downvotes_at_retrieval: int
    requester_user_flair: str
    requester_username: str
    unix_timestamp_of_request: float
    unix_timestamp_of_request_utc: float
