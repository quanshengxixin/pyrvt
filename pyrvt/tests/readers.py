#!/usr/bin/env python3
# encoding: utf-8

"""Scripts for loading test case data."""

import numpy as np

def load_fourier_spectrum(fname):
    """Load Fourier amplitude spectrum file created by fas_drvr.exe.

    Inputs
    ------
    fname : string
        File name of the data file

    Returns
    -------
    event : dict
        Dictionary containing the event
    """
    assert fname.endswith('_fs.col')
    rows = np.loadtxt(fname, skiprows=2)

    d = dict(
        mag = rows[0, 0],
        dist = rows[0, 1],
        freq = rows[:, 4],
        fourier_amp = rows[:, 8],
    )

    return d

def load_rvt_response_spectrum(fname):
    """Load response spectrum file created by fas_drvr.exe.

    Inputs
    ------
    fname : string
        File name of the data file

    Returns
    -------
    event : dict
        Dictionary containing the event
    """
    assert fname.endswith('_rs.rv.col')
    rows = np.loadtxt(fname, skiprows=2)

    d = dict(
        damping = rows[0, 0],
        mag = rows[0, 3],
        dist = rows[0, 4],
        duration = rows[0, 16],
        freq = rows[:, 2],
        spec_accel = rows[:, 11])

    return d
