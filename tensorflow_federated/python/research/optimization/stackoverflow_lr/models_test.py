# Copyright 2019, The TensorFlow Federated Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Tests for stackoverflow models."""

import tensorflow as tf

from tensorflow_federated.python.research.optimization.stackoverflow_lr import models


class ModelCollectionTest(tf.test.TestCase):

  def test_lr_model(self):
    tokens = tf.random.normal([4, 1000])
    model = models.create_logistic_model(1000, 10)
    predicted_tags = model(tokens)
    num_model_params = 1000*10 + 10
    self.assertIsNotNone(predicted_tags)
    self.assertEqual(predicted_tags.shape, [4, 10])
    self.assertEqual(model.count_params(), num_model_params)


if __name__ == '__main__':
  tf.test.main()
