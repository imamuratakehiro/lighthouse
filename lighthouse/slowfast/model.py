"""
Copyright $today.year LY Corporation

LY Corporation licenses this file to you under the Apache License,
version 2.0 (the "License"); you may not use this file except in compliance
with the License. You may obtain a copy of the License at:

  https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
License for the specific language governing permissions and limitations
under the License.
"""
# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved.
"""Build a video classification model."""

import lighthouse.slowfast.slowfast.utils.checkpoint as cu
from lighthouse.slowfast.slowfast.models import model_builder


def slowfast_model_loader(model_weight_path, device):
    """
    Build slowfast model
    Args:
        cfg (CfgNode): configs. Details can be found in
            slowfast/config/defaults.py
    """
    # Build the video model and print model statistics.
    model = model_builder.build_model()
    cu.load_checkpoint(model_weight_path, model,
                       data_parallel=False, optimizer=None,
                       convert_from_caffe2=True)
    model.to(device)
    return model
