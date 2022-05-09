#
# Copyright 2016 The BigDL Authors.
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

import warnings


def create_hpo_searcher(trainer):
    """Create HPO Search for PyTorch."""
    from bigdl.nano.automl.pytorch import HPOSearcher
    return HPOSearcher(trainer)


def check_hpo_status(searcher):
    """Check the status of hpo."""
    if not searcher:
        warnings.warn(
            'HPO is not properly enabled or required \
                dependency is not installed.', UserWarning)
        return False
    return True


def create_optuna_backend():
    """Create an Optuna Backend."""
    from bigdl.nano.deps.automl.optuna_backend import OptunaBackend
    return OptunaBackend()


def create_optuna_pl_pruning_callback(*args, **kwargs):
    """Create PyTorchLightning Pruning Callback."""
    from optuna.integration import PyTorchLightningPruningCallback
    return PyTorchLightningPruningCallback(*args, **kwargs)


def create_optuna_tfkeras_pruning_callback(*args, **kwargs):
    """Create Tensorflow Keras Pruning Callback."""
    from optuna.integration import TFKerasPruningCallback
    return TFKerasPruningCallback(*args, **kwargs)