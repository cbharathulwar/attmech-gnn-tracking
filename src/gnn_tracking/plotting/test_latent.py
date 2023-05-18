from __future__ import annotations

import numpy as np
import pytest
from matplotlib import pyplot as plt

from gnn_tracking.plotting.latent import SelectedPidsPlot


@pytest.fixture()
def selected_pids_test_data() -> dict[str, np.ndarray]:
    kwargs = {}
    for key in ["condensation_space", "input_node_features"]:
        kwargs[key] = np.random.uniform(size=(100, 5))
    for key in ["particle_id", "labels"]:
        kwargs[key] = np.random.randint(0, 10, size=100)
    kwargs["ec_hit_mask"] = np.ones(100, dtype=bool)
    print({k: v.shape for k, v in kwargs.items()})
    return kwargs


def test_draw_selected_pids(selected_pids_test_data):
    spp = SelectedPidsPlot(**selected_pids_test_data)
    fig, axs = plt.subplots(ncols=2, figsize=(10, 5))
    spp.plot_other_hit_latent(axs[0])
    spp.plot_selected_pid_latent(axs[0])
    spp.plot_collateral_latent(axs[0])
    spp.plot_other_hit_ep(axs[1])
    spp.plot_selected_pid_ep(axs[1])
    spp.plot_collateral_ep(axs[1])
