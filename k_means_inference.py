import numpy as np
from typing import List
from sklearn.metrics.pairwise import cosine_similarity

centroids = np.load("centroids.npy")


def get_clusters(embeddings: np.array) -> List:
    """
    get clusters over computed embeddings
    :param embeddings: BERT Embeddings
    :return: List of clusters upon computed centroids after kmeans
    """

    clusters = []

    for i in range(0, embeddings.shape[0]):
        data = embeddings[i, :]

        cosine_similarities = []
        for cluster in centroids:
            cosine_similarities.append(
                cosine_similarity(data.reshape(1, -1), cluster.reshape(1, -1))
            )

        max_value = max(cosine_similarities)
        clusters.append(cosine_similarities.index(max_value))

    return clusters
