#
# Copyright 2018 Analytics Zoo Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import sys

from bigdl.util.common import callBigDlFunc
from ..engine.topology import ZooKerasLayer

if sys.version >= '3':
    long = int
    unicode = str


class Embedding(ZooKerasLayer):
    """
    Turn positive integers (indexes) into dense vectors of fixed size.
    The input of this layer should be 2D.

    This layer can only be used as the first layer in a model, you need to provide the argument
    input_length (an integer) or input_shape (a shape tuple, does not include the batch dimension).

    # Arguments
    input_dim: Size of the vocabulary. Int > 0.
    output_dim: Dimension of the dense embedding. Int >= 0.
    init: String representation of the initialization method for the weights of the layer.
          Default is 'uniform'.
    W_regularizer: An instance of [[Regularizer]], (eg. L1 or L2 regularization),
                   applied to the embedding matrix. Default is None.
    input_length: Positive int. The sequence length of each input.
    name: String to set the name of the layer.
          If not specified, its name will by default to be a generated string.

    >>> embedding = Embedding(1000, 32, input_length=10, name="embedding1")
    creating: createZooKerasEmbedding
    """
    def __init__(self, input_dim, output_dim, init="uniform", input_length=None,
                 W_regularizer=None, input_shape=None, **kwargs):
        if input_length:
            input_shape = (input_length,)
        super(Embedding, self).__init__(None,
                                        input_dim,
                                        output_dim,
                                        init,
                                        W_regularizer,
                                        list(input_shape) if input_shape else None,
                                        **kwargs)


class WordEmbedding(ZooKerasLayer):
    """
    Embedding layer with pre-trained weights for words.
    Turn non-negative integers (indices) into dense vectors of fixed size.
    Currently only GloVe embedding is supported.
    The input of this layer should be 2D.

    This layer can only be used as the first layer in a model, you need to provide the argument
    input_length (an integer) or input_shape (a shape tuple, does not include the batch dimension).

    # Arguments
    embedding_file: The path to the embedding file.
                    Currently only the following GloVe files are supported:
                    "glove.6B.50d.txt", "glove.6B.100d.txt", "glove.6B.200d.txt"
                    "glove.6B.300d.txt", "glove.42B.300d.txt", "glove.840B.300d.txt".
                    You can download them from: https://nlp.stanford.edu/projects/glove/.
    word_index: Dictionary of word (string) and its corresponding index (int).
                The index is supposed to start from 1 with 0 reserved for unknown words.
                During the prediction, if you have words that are not in the word_index
                for the training, you can map them to index 0.
                Default is None. In this case, all the words in the embedding_file will
                be taken into account and you can call
                WordEmbedding.get_word_index(embedding_file) to retrieve the dictionary.
    trainable: To configure whether the weights of this layer will be updated or not.
               Only False is supported for now.
    input_length: Positive int. The sequence length of each input.
    name: String to set the name of the layer.
          If not specified, its name will by default to be a generated string.
    """
    def __init__(self, embedding_file, word_index=None, trainable=False, input_length=None,
                 input_shape=None, **kwargs):
        if input_length:
            input_shape = (input_length, )
        super(WordEmbedding, self).__init__(None,
                                            embedding_file,
                                            word_index,
                                            trainable,
                                            list(input_shape) if input_shape else None,
                                            **kwargs)

    @staticmethod
    def get_word_index(embedding_file, bigdl_type="float"):
        """
        Get the full wordIndex map from the given embedding_file.

        # Arguments
        embedding_file: The path to the embedding file.
                        Currently only the following GloVe files are supported:
                        "glove.6B.50d.txt", "glove.6B.100d.txt", "glove.6B.200d.txt"
                        "glove.6B.300d.txt", "glove.42B.300d.txt", "glove.840B.300d.txt".
                        You can download them from: https://nlp.stanford.edu/projects/glove/.

        # Returns
        Dictionary of word (string) and its corresponding index (int) obtained from
        the given embedding file.
        """
        return callBigDlFunc(bigdl_type, "wordEmbeddingGetWordIndex",
                             embedding_file)
